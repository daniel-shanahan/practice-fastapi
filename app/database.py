from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg
# from psycopg.rows import dict_row
# import time

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# To connect to the database directly, without SQLAlchemy

# while True:
#     try:
#         # Equivalent to URI
#         # conninfo="postgresql://postgres:postgres@localhost/fastapi"
#         conn = psycopg.connect(
#             conninfo="host=localhost dbname=fastapi user=postgres password=postgres",
#             row_factory=dict_row,
#         )
#         cursor = conn.cursor()
#         print("database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed.")
#         print("Error: ", error)
#         time.sleep(2)
