from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String, Float
from . import db


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[str] = mapped_column()