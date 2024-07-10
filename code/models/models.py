from sqlalchemy import Integer, String, MetaData, Table, Column, Boolean, ForeignKey

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

post = Table(
    'post',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('content', String, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
)

comment = Table(
    'comment',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('content', String, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
    Column('post_id', Integer, ForeignKey('post.id'), nullable=False),
)
