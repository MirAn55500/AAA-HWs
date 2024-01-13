# !/usr/bin/env python
"""
Bot for playing tic tac toe game with multiple CallbackQueryHandlers.
"""
import logging
import os
import random
from copy import deepcopy

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# set higher logging level for httpx
# to avoid all GET and POST requests being logged
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# get token using BotFather
TOKEN = os.getenv('TG_TOKEN')

CHOOSE_SYMBOL, CONTINUE_GAME, FINISH_GAME = range(3)

FREE_SPACE = '.'
CROSS = 'X'
ZERO = 'O'


DEFAULT_STATE = [[FREE_SPACE for _ in range(3)] for _ in range(3)]


def get_default_state():
    """Helper function to get default state of the game"""
    return deepcopy(DEFAULT_STATE)


def generate_keyboard(state: list[list[str]])\
        -> list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyboard 3x3 (telegram buttons)"""
    return [
        [
            InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
            for r in range(3)
        ]
        for c in range(3)
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    context.user_data['keyboard_state'] = get_default_state()
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f'Cross ({CROSS})', callback_data=CROSS)],
        [InlineKeyboardButton(f'Zero ({ZERO})', callback_data=ZERO)]
    ])
    user_name = update.message.from_user.first_name
    hello_text = f'Привет, {user_name}! Выбери своего бойца:'
    await update.message.reply_text(hello_text, reply_markup=reply_markup)
    return CHOOSE_SYMBOL


async def initial_step(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> int:
    """Set the chosen symbol and start the game."""
    query = update.callback_query
    player_symbol = context.user_data['player_symbol'] = query.data
    bot_symbol = CROSS if player_symbol == ZERO else ZERO
    keyboard_state = context.user_data['keyboard_state']
    if player_symbol == ZERO:
        bot_move_x, bot_move_y = get_bot_move(keyboard_state)
        keyboard_state[bot_move_x][bot_move_y] = bot_symbol
    keyboard = generate_keyboard(keyboard_state)
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = (f'{player_symbol} ваш ход! Пожалуйста, выберите '
                 f'свободное поле, куда хотите поставить {player_symbol}')
    await query.message.reply_text(reply_msg, reply_markup=reply_markup)
    return CONTINUE_GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Main processing of the game"""
    query = update.callback_query
    x, y = map(int, list(query.data))
    player_symbol = context.user_data['player_symbol']
    bot_symbol = CROSS if player_symbol == ZERO else ZERO
    keyboard_state = context.user_data['keyboard_state']
    if keyboard_state[x][y] == FREE_SPACE:
        keyboard_state[x][y] = player_symbol
        if won(keyboard_state, player_symbol):
            keyboard = generate_keyboard(keyboard_state)
            reply_markup = InlineKeyboardMarkup(keyboard)
            reply_text = ('Вы победили! '
                          'Если хотите начать заново, введите: /start')
            await query.message.reply_text(reply_text,
                                           reply_markup=reply_markup)
            return await end(update, context)
        elif not any(FREE_SPACE in row for row in keyboard_state):
            keyboard = generate_keyboard(keyboard_state)
            reply_markup = InlineKeyboardMarkup(keyboard)
            reply_text = 'Ничья! Если хотите начать заново, введите: /start'
            await query.message.reply_text(reply_text,
                                           reply_markup=reply_markup)
            return await end(update, context)

        # Bot's move
        bot_move_x, bot_move_y = get_bot_move(keyboard_state)
        keyboard_state[bot_move_x][bot_move_y] = bot_symbol

        keyboard = generate_keyboard(keyboard_state)
        reply_markup = InlineKeyboardMarkup(keyboard)
        if won(keyboard_state, bot_symbol):
            reply_text = ('Вы проиграли... Повезёт в следующий раз! '
                          'Если хотите начать заново, введите: /start')
            await query.message.reply_text(reply_text,
                                           reply_markup=reply_markup)
            return await end(update, context)

        elif not any(FREE_SPACE in row for row in keyboard_state):
            reply_text = 'Ничья! Если хотите начать заново, введите: /start'
            await query.message.reply_text(reply_text,
                                           reply_markup=reply_markup)
            return await end(update, context)

        reply_text = (f'{player_symbol} ваш ход! Пожалуйста, выберите '
                      f'свободное поле, куда хотите поставить {player_symbol}')
        await query.message.reply_text(reply_text,
                                       reply_markup=reply_markup)

    else:
        keyboard = generate_keyboard(context.user_data['keyboard_state'])
        reply_markup = InlineKeyboardMarkup(keyboard)
        reply_text = (f'Это место занято. Пожалуйста, выберите свободное поле,'
                      f' куда хотите поставить {player_symbol}')
        await query.message.reply_text(reply_text, reply_markup=reply_markup)

    return CONTINUE_GAME


def get_bot_move(state: list[list[str]]) -> tuple[int, int]:
    """Get a random move for the bot"""
    available_moves = [(r, c) for r in range(3) for c in range(3)
                       if state[r][c] == FREE_SPACE]
    return random.choice(available_moves)


def won(state: list[list[str]], symbol: str) -> bool:
    """Check if crosses or zeros have won the game"""
    for row in state:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(state[row][col] == symbol for row in range(3)):
            return True

    if (all(state[i][i] == symbol for i in range(3)) or
            all(state[i][2 - i] == symbol for i in range(3))):
        return True

    return False


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    # reset state to default so you can play again with /start
    context.user_data['keyboard_state'] = get_default_state()
    return ConversationHandler.END


def main() -> None:
    """Run the bot"""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Setup conversation handler with the states CHOOSE_SYMBOL,
    # CONTINUE_GAME and FINISH_GAME
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSE_SYMBOL: [
                CallbackQueryHandler(initial_step,
                                     pattern=f'^[{CROSS}{ZERO}]$')
            ],
            CONTINUE_GAME: [
                CallbackQueryHandler(game, pattern=f'^{r}{c}$')
                for r in range(3)
                for c in range(3)
            ],
            FINISH_GAME: [
                CallbackQueryHandler(end, pattern='^' + f'{r}{c}' + '$')
                for r in range(3)
                for c in range(3)
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to application
    # that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
