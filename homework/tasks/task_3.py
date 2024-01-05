import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    tasks = await asyncio.gather(*coros)
    results = sorted(tasks, key=lambda x: x.number)
    return ''.join(ticket.key for ticket in results)
