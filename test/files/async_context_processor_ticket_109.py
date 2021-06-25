from sqlalchemy import literal
from sqlalchemy import select
from sqlalchemy.ext import asyncio


async def test() -> None:
    database = asyncio.create_async_engine("", future=True)

    trans_ctx = database.begin()
    async with trans_ctx as connection:
        await connection.execute(select(literal(1)))
