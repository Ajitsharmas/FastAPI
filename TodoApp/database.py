from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://deploy_database_0lp4_user:o1aURhQOYrm6miajFcipfCRBesM2EiY1@dpg-d0aue8hr0fns73cuhle0-a/deploy_database_0lp4'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
