import pytest
from telegram import (InlineKeyboardButton, Update,
                      Message, User, Chat, CallbackQuery)
from telegram.ext import ContextTypes

from tg_bot import (get_default_state, generate_keyboard,
                    start, initial_step, won, game)


FREE_SPACE = '.'
CROSS = 'X'
ZERO = 'O'


def test_default_state():
    actual = get_default_state()
    expected = [['.' for _ in range(3)] for _ in range(3)]
    assert actual == expected


def test_generate_keyboard():
    state = [['.' for _ in range(3)] for _ in range(3)]
    actual = generate_keyboard(state)
    expected = [
        [
            InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
            for r in range(3)
        ] for c in range(3)
    ]
    assert actual == expected


@pytest.fixture
def get_update_context():
    user = User(1, first_name='Avito', is_bot=False)
    chat = Chat(1, type='PRIVATE')
    message = Message(1, date='2011-11-04', from_user=user, chat=chat)
    update = Update(1, message=message)
    context = ContextTypes(user_data=dict())
    return update, context


@pytest.mark.asyncio
async def test_start(mocker, get_update_context):
    update, context = get_update_context
    mocker.patch.object(Message, 'reply_text', return_value=None)
    actual = await start(update, context)
    assert actual == 0
    assert (context.user_data['keyboard_state'] ==
            [[FREE_SPACE for _ in range(3)] for _ in range(3)])


@pytest.mark.asyncio
async def test_initial_step_cross(mocker, get_update_context):
    update, context = get_update_context
    query = CallbackQuery(data=CROSS, id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    context.user_data['keyboard_state'] = \
        [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await initial_step(update, context)
    assert (context.user_data['keyboard_state'] ==
            [[FREE_SPACE for _ in range(3)] for _ in range(3)])
    assert res == 1


@pytest.mark.asyncio
async def test_initial_step_zero(mocker, get_update_context):
    update, context = get_update_context
    query = CallbackQuery(data=ZERO, id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    context.user_data['keyboard_state'] = \
        [['.' for _ in range(3)] for _ in range(3)]
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await initial_step(update, context)
    count_cross = ''.join([''.join(row) for row in
                           context.user_data['keyboard_state']]).count(CROSS)
    assert count_cross == 1
    assert res == 1


def test_won_cross_row():
    state = [[CROSS for _ in range(3)],
             [FREE_SPACE for _ in range(3)], [CROSS, ZERO, ZERO]]
    assert won(state, CROSS) is True
    assert won(state, ZERO) is False


def test_won_zero_diagonal():
    state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    for i in range(3):
        state[i][2 - i] = ZERO
    assert won(state, ZERO) is True
    assert won(state, CROSS) is False


def test_won_zero_column():
    state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    for i in range(3):
        state[i][0] = ZERO
    assert won(state, ZERO) is True
    assert won(state, CROSS) is False


@pytest.mark.asyncio
async def test_game_cross_continue(mocker, get_update_context):
    state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    update, context = get_update_context
    context.user_data['player_symbol'] = CROSS
    context.user_data['keyboard_state'] = state
    query = CallbackQuery(data=(0, 1), id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await game(update, context)
    assert res == 1
    joined_data = ''.join([''.join(row) for row in
                           context.user_data['keyboard_state']])
    assert joined_data.count(CROSS) == 1
    assert joined_data.count(ZERO) == 1


@pytest.mark.asyncio
async def test_game_zero_continue(mocker, get_update_context):
    state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    state[0][0] = CROSS
    update, context = get_update_context
    context.user_data['player_symbol'] = ZERO
    context.user_data['keyboard_state'] = state
    query = CallbackQuery(data=(0, 1), id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await game(update, context)
    assert res == 1
    joined_data = ''.join([''.join(row) for row in
                           context.user_data['keyboard_state']])
    assert joined_data.count(CROSS) == 2
    assert joined_data.count(ZERO) == 1


@pytest.mark.asyncio
async def test_game_zero_won(mocker, get_update_context):
    state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    state[0] = [FREE_SPACE, ZERO, ZERO]
    update, context = get_update_context
    context.user_data['player_symbol'] = ZERO
    context.user_data['keyboard_state'] = state
    query = CallbackQuery(data=(0, 0), id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await game(update, context)
    assert res == -1


@pytest.mark.asyncio
async def test_game_zero_draw(mocker, get_update_context):
    state = [[CROSS, FREE_SPACE, CROSS],
             [CROSS, ZERO, CROSS],
             [ZERO, CROSS, ZERO]]
    update, context = get_update_context
    context.user_data['player_symbol'] = ZERO
    context.user_data['keyboard_state'] = state
    query = CallbackQuery(data=(0, 1), id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await game(update, context)
    init_state = [[FREE_SPACE for _ in range(3)] for _ in range(3)]
    assert res == -1
    assert context.user_data['keyboard_state'] == init_state


@pytest.mark.asyncio
async def test_game_zero_not_empty(mocker, get_update_context):
    state = [[CROSS, FREE_SPACE, CROSS],
             [CROSS, ZERO, CROSS],
             [ZERO, CROSS, ZERO]]
    update, context = get_update_context
    context.user_data['player_symbol'] = ZERO
    context.user_data['keyboard_state'] = state
    query = CallbackQuery(data=(0, 0), id=1,
                          from_user=update.message.from_user,
                          chat_instance='', message=update.message)
    update = Update(1, message=update.message, callback_query=query)
    mocker.patch.object(Message, 'reply_text', return_value=None)
    res = await game(update, context)
    assert res == 1
    assert state == context.user_data['keyboard_state']
