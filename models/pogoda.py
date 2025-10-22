from sqlalchemy import Table,Column,Integer,Float,String,TIMESTAMP,MetaData

metadataobj = MetaData()

pogoda = Table(
    'pogoda1',
    metadataobj,
    Column('Data',TIMESTAMP),
    Column('city_name',String),
    Column('temperature',Integer),
)
