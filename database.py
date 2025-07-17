import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://todo:todo@localhost:5432/todo_db")
DB_USER = os.getenv("username", "")
DB_PASS = os.getenv("password", "")
DB_HOST = os.getenv("host", "")
DB_PORT = os.getenv("port", "")
DB_DB = os.getenv("dbname", "")

KUBE_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DB}"
DATABASE_URL = os.getenv("DATABASE_URL", KUBE_DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
