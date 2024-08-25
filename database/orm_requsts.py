from database.data import db
from database.models import User, Info, Category
from sqlalchemy import select, update,delete


class OrmRequsts:

    async def check_user(self, user_id):
        async with db.session() as session:
            return await session.scalar(select(User).where(User.id == user_id))

    async def create_user(self, data):
        async with db.session() as session:
            query = User(
                id=data['id'],
                username=data['username'],
                name=data['name'],
                phonenumber=data['phone'],
                email=data['email']
            )
            session.add(query)
            await session.commit()

    async def upload_file(self, data):
        async with db.session() as session:
            query = Info(
                category=data['category'],
                photo_id=data['photo']
            )
            session.add(query)
            await session.commit()

    async def get_files(self, category):
        async with db.session() as session:
            query = await session.execute(select(Info.photo_id).where(Info.category == category))
            return query.scalars().all()

    async def get_files_admin(self, category):
        async with db.session() as session:
            query = await session.execute(select(Info.photo_id, Info.id).where(Info.category == category))
            # print(f'Запрос в БД {query.all()}')
            return query.all()

    async def get_categories(self):
        async with db.session() as session:
            query = await session.execute(select(Category.category, Category.id))
            return query.all()

    async def change_file_admin(self, data):
        async with db.session() as session:
            await session.execute(update(Info).values({'photo_id': f'{data["file"]}'}).where(Info.id == data['id']))
            await session.commit()

    async def get_file_by_admin(self):
        async with db.session() as session:
            data = await session.execute(select(User.username,
                                                User.name,
                                                User.phonenumber,
                                                User.email))
            return data.all()

    async def admin_add_button(self, data):
        async with db.session() as session:
            query = Category(
                category=data
            )
            session.add(query)
            await session.commit()

    async def admin_change_button(self, data):
        async with db.session() as session:
            await session.execute(update(Category).values(
                {'category': f'{data["button_name"]}'}).where(
                Category.id == data['button_idx']))
            await session.commit()
    async def admin_delete_button(self, idx):
        async with db.session() as session:
            await session.execute(delete(Category).where(Category.id == f"{idx}"))
            await session.commit()



orm = OrmRequsts()
