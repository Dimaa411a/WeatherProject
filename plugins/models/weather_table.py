from sqlalchemy import Table, Column, Integer, String, Float, MetaData, DateTime

metadata = MetaData()

weather = Table(
    "weather", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("city", String(50)),
    Column("temp", Float),
    Column("description", String(100)),
    Column("dt", DateTime),
    Column("sunrise", DateTime),
    Column("sunset", DateTime),
)
