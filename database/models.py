from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column)
from sqlalchemy import String, VARCHAR, INT


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    username: Mapped[str] = mapped_column(String(150), nullable=False, default="Неизвестный")
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    phonenumber: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)


class Info(Base):
    __tablename__ = 'info'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    photo_id: Mapped[str] = mapped_column(VARCHAR(255))


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(150), nullable=False)


class Visa(Base):
    __tablename__ = 'visa_price'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    visa_country: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[int] = mapped_column(INT, nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=False)
