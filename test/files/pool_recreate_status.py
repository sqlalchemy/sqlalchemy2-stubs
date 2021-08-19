import sqlalchemy
import sqlalchemy.pool

engine = sqlalchemy.create_engine("postgresql://scott:tiger@localhost/test")
status: str = engine.pool.status()
other_pool: sqlalchemy.pool.Pool = engine.pool.recreate()
