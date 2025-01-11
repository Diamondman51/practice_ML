from sqlalchemy import ForeignKey, MetaData, Table, bindparam, create_engine, Column, Integer, String, delete, insert, select, text, update
# import psycopg2


database = 'school management'
host = 'localhost'
user = 'postgres'
password = 'Zshavkatov61'
port = '5432'

engine = create_engine(f"sqlite:///my_db.db", echo=True)

meta = MetaData()

user_table = Table(
    'users',
    meta,
    Column("id", Integer, autoincrement=True, unique=True, primary_key=True),
    Column("first_name", String),
    Column("last_name", String(30))
)

address_table = Table(
    'address',
    meta,
    Column('email', String),
    Column('user_id', ForeignKey('users.id'))
)

meta.create_all(engine)


# After executing engine.begin() there is no need for commitment. However for engine.connect() needed commitment
with engine.begin() as conn:
    meta.create_all(engine)
    res = conn.execute(
        insert(user_table),
        [
            {'first_name': 'Javohir', 'last_name': "Shavkatov"},
            {'first_name': 'Ahmed', 'last_name': "Shavkatov"},
            {'first_name': 'Suhrob', 'last_name': "Shavkatov"},
        ]
    )

    conn.execute(
        insert(address_table),
        [
            {'email': 'email_1', 'user_id': 1},
            {'email': 'email_2', 'user_id': 2},
            {'email': 'email_3', 'user_id': 3},
        ]
    )
    # conn.commit()
    # conn.close()


with engine.begin() as conn:
    conn.execute(
        update(user_table).where(user_table.c.first_name == bindparam('oldname')).values(first_name=bindparam("newname")),
        [
            {'oldname': 'Java', 'newname': 'Javohir'},
            {'oldname': 'Ahmed', 'newname': 'Axmed'},
            {'oldname': 'Suhrob', 'newname': 'Suhrobjon'},
        ]
        )
    


    # TODO it is used for deleting linked tables only on MySQL and PostGres, not on SQLite 
    # conn.execute(
    #     delete(user_table).where(user_table.c.id == address_table.c.user_id)
    #     .where(address_table.c.email == 'email_1')
    # )

    res = conn.execute(
        delete(user_table).where(user_table.c.id.in_([2, 3, 1])).returning(user_table.c.id)
    )
    print('Deleted', res)
    # print(conn.execute(select(user_table)).all())
    # conn.commit()
# with engine.begin() as conn:
#     res = conn.execute(
#         select(
#             address_table.c.email,
#             (user_table.c.first_name + ' ' +  user_table.c.last_name).label('fullname')).where(user_table.c.id.in_([1, 2, 3])).join(user_table).order_by('fullname')
#     )

# print(res.mappings().all())
# print(res.all())

# for re in res:
#     print(re.fullname)

