from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

# Correct connection string without 'jdbc:'
engine = create_engine('postgresql+psycopg2://postgres:Zshavkatov61@localhost:5432/', echo=True)

session = Session(engine)


class Base(DeclarativeBase):
    pass
    # metadata = MetaData()


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(unique=True, autoincrement=True, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(unique=True, autoincrement=True, primary_key=True)
    location: Mapped[str] = mapped_column(nullable=True)


Base.metadata.create_all(engine)
