from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String, Float
from . import db


class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[int] = mapped_column(Integer, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(400), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250))
