import asyncio
from typing import Coroutine


async def limit_execution_time(
        coro: Coroutine, max_execution_time: float) -> None:
    task = asyncio.create_task(coro)
    return await asyncio.wait_for(task, max_execution_time)


async def limit_execution_time_many(
        *coros: Coroutine, max_execution_time: float) -> None:
    tasks = [asyncio.create_task(coro) for coro in coros]
    done, pending = await asyncio.wait(tasks, timeout=max_execution_time)
    results = [task.result() for task in done]
    for task in pending:
        task.cancel()
    return results
