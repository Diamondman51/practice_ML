# import email
# from io import SEEK_END
# from sqlalchemy import Column, ForeignKey, Integer, Table, select, create_engine
# from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, Session, joinedload

# engine = create_engine('sqlite:///SQLAlchemy//orm.db', echo=True)

# session = Session(engine, expire_on_commit=True, autoflush=False)


# class Base(DeclarativeBase):
#     pass




# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
#     name: Mapped[str]
#     age: Mapped[int]
#     # If uselist=True in both models in our case User and Address it would be Many to many. Now it is One to one
#     # address: Mapped['Address'] = relationship(back_populates='user', uselist=False)
    
#     # It is one to many relationship
#     # Lazy joined better when we have less than 10,000 data, subquery better when the data is coming close to 10,000 and selectin is better when we have 'where' and similar requirements
#     addresses: Mapped[list['Address']] = relationship(back_populates='user', uselist=True, lazy='joined')

#     def __repr__(self):
#         return f'{self.id} {self.name}'
    

# class Address(Base):
#     __tablename__ = "addresses"
#     email: Mapped[str] = mapped_column(primary_key=True, unique=True)
#     # If uselist=True in both models in our case User and Address it would be Many to many. Now it is One to one
#     user: Mapped[User] = relationship(back_populates='addresses', uselist=False)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='cascade'))

#     def __repr__(self):
#         return f'Email: {self.email}. User id: {self.user_id}'


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# user = User(name='Java', age=19)
# address1 = Address(email='zshavkatov51@gmail.com')
# address2 = Address(email='zshavkatov61@gmail.com')
# user.addresses.append(address1)
# user.addresses.append(address2)
# session.add(user)
# session.commit()

# # userr = session.scalar(select(User))
# # addr = session.query(Address.user).filter(Address.user == 1)
# # addr = session.query(User, Address.email).filter(Address.user.id==1).all()


# user = select(User).where(User.id == 1)
# res = session.execute(user)
# user = res.scalar()

# print('Res', res, 'User', user)

# # print(userr)
# # print(userr.addresses)
# # print(userr.age)
# # print(addr)
# # for i in addr:
# #     print(i, '\t',)








# # # Many to Many relationship
# # class User(Base):
# #     __tablename__ = "users"
# #     id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
# #     name: Mapped[str]
# #     age: Mapped[int]
# #     addresses: Mapped[list['Address']] = relationship(back_populates='users', uselist=True, secondary='user_address')

# #     def __repr__(self):
# #         return f'{self.id} {self.name}'
    

# # class Address(Base):
# #     __tablename__ = "addresses"
# #     email: Mapped[str] = mapped_column(primary_key=True, unique=True)
# #     users: Mapped[list['User']] = relationship(back_populates='addresses', uselist=True, secondary='user_address')

# #     def __repr__(self):
# #         return f'Email: {self.email}. User id: {self.users}'


# # class UserAddress(Base):
# #     __tablename__ = 'user_address'
# #     user_id = mapped_column(ForeignKey('users.id'), primary_key=True)
# #     address_id = mapped_column(ForeignKey('addresses.email'), primary_key=True)

# #     def __repr__(self):
# #         return f"UserAddress: {self.user_id=}, {self.address_id=}"


# # Base.metadata.create_all(engine)

# # user_1 = User(name='Javohir', age=19)
# # user_2 = User(name='Axmed', age=16)
# # address_1 = Address(email='zshavkatov51@gmail.com')
# # address_2 = Address(email='zshavkatov61@gmail.com')
# # address_3 = Address(email='zshavkatov71@gmail.com')
# # user_1.addresses.append(address_1)
# # user_1.addresses.append(address_2)
# # user_1.addresses.append(address_3)
# # user_2.addresses.append(address_1)
# # user_2.addresses.append(address_2)
# # session.add(user_1)
# # session.add(user_2)
# # session.commit()

# # user1 = session.scalars(select(User)).all()
# # user_ = session.scalars(select(User).options(joinedload(User.addresses))).unique().all()
# # user = session.scalar(select(User))
# # user_secondary = session.scalars(select(UserAddress)).all()
# # # addresses = session.scalars(select(Address)).all()

# # print()
# # print()
# # print(user.addresses, '\n')
# # print(user_, '\n')
# # print(user_secondary, '\n')

ls = [True, False, False, False, False, False,]

print(any(ls), all(ls))
