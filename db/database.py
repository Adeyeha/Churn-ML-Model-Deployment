from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import cx_Oracle


user = 'businessobjects'
pwd = 'Password123'

cx_Oracle.init_oracle_client(lib_dir=r"db/instantclient_21_3/")
dsn=cx_Oracle.makedsn('10.236.8.101', '1521', service_name='ghadbp')

engine = create_engine(f'oracle+cx_oracle://{user}:{pwd}@{dsn}', echo=True, max_identifier_length=128)

# ora_engine.connect()

# connect_url = URL(
#     "oracle+cx_oracle",
#     username="",
#     password="",
#     host="",
#     port="",
#     database=""
# )

# engine = create_engine(connect_url, max_identifier_length=128)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()