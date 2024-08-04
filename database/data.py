from create_bot import DB_CONN
from database.models import Base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class Database:
    def __init__(self) -> None:
        self.connect = DB_CONN
        self.engine = create_async_engine(url=self.connect)
        self.session = async_sessionmaker(bind=self.engine, class_=AsyncSession)
        if self.session:
            print('DataBase connected ok!!!')

    async def create_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = Database()
