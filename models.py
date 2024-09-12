import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
from database import metadata


tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String),
    Column("status", Boolean, default=False),
    Column("priority", Integer, default=0)
)
