from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import Session

# async engine
async_engine: AsyncEngine = create_async_engine("")
async_engine.clear_compiled_cache()
async_engine.update_execution_options()
async_engine.get_execution_options()
async_engine.url
async_engine.pool
async_engine.dialect
async_engine.engine
async_engine.name
async_engine.driver
async_engine.echo

# async connection
async def go_async_conn() -> None:
    async_conn: AsyncConnection = await async_engine.connect()
    async_conn.closed
    async_conn.invalidated
    async_conn.dialect
    async_conn.default_isolation_level


# async session
AsyncSession.object_session(object())
AsyncSession.identity_key()
async_session: AsyncSession = AsyncSession(async_engine)
"foo" in async_session
list(async_session)
async_session.add(object())
async_session.add_all([])
async_session.expire(object())
async_session.expire_all()
async_session.expunge(object())
async_session.expunge_all()
async_session.get_bind()
async_session.is_modified(object())
async_session.in_transaction()
async_session.in_nested_transaction()
async_session.dirty
async_session.deleted
async_session.new
async_session.identity_map
async_session.is_active
async_session.autoflush
async_session.no_autoflush
async_session.info

# async scoped session
async_scoped_session.object_session(object())
async_scoped_session.identity_key()
async_scoped_session.close_all()
async_ss = async_scoped_session(AsyncSession, lambda: 42)
"foo" in async_ss
list(async_ss)
async_ss.add(object())
async_ss.add_all([])
async_ss.begin()
async_ss.begin_nested()
async_ss.close()
async_ss.commit()
async_ss.connection()
async_ss.delete(object())
async_ss.execute(text("select 1"))
async_ss.expire(object())
async_ss.expire_all()
async_ss.expunge(object())
async_ss.expunge_all()
async_ss.flush()
async_ss.get(object, 1)
async_ss.get_bind()
async_ss.is_modified(object())
async_ss.merge(object())
async_ss.refresh(object())
async_ss.rollback()
async_ss.scalar(text("select 1"))
async_ss.bind
async_ss.dirty
async_ss.deleted
async_ss.new
async_ss.identity_map
async_ss.is_active
async_ss.autoflush
async_ss.no_autoflush
async_ss.info

# scoped session
scoped_session.object_session(object())
scoped_session.identity_key()
scoped_session.close_all()
ss = scoped_session(Session)
"foo" in ss
list(ss)
ss.add(object())
ss.add_all([])
ss.begin()
ss.begin_nested()
ss.close()
ss.commit()
ss.connection()
ss.delete(object())
ss.execute(text("select 1"))
ss.expire(object())
ss.expire_all()
ss.expunge(object())
ss.expunge_all()
ss.flush()
ss.get(object, 1)
ss.get_bind()
ss.is_modified(object())
ss.bulk_save_objects([])
ss.bulk_insert_mappings(object, [])
ss.bulk_update_mappings(object, [])
ss.merge(object())
ss.query(object),
ss.refresh(object())
ss.rollback()
ss.scalar(text("select 1"))
ss.bind
ss.dirty
ss.deleted
ss.new
ss.identity_map
ss.is_active
ss.autoflush
ss.no_autoflush
ss.info
ss.autocommit
