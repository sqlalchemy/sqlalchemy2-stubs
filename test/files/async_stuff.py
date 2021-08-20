from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_async_engine(...)
async_session = sessionmaker(engine, class_=AsyncSession)
