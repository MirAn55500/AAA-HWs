async def magic_func() -> int:
    return 42


async def fix_this_code() -> int:
    return await magic_func()
