from typing import AsyncIterator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from core.settings import settings

DATABASE_ENGINE = AsyncEngine(create_engine(
    settings.db_url,
    future=True,
    pool_size=100,
    max_overflow=0,
    pool_timeout=30,
    pool_recycle=900,
))

SESSIONMAKER = async_sessionmaker(
    bind=DATABASE_ENGINE,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with SESSIONMAKER() as session:
        yield session
