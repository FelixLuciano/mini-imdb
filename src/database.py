import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_USERNAME = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
DB_DATABASE = os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        # "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
