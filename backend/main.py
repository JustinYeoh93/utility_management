from fastapi import FastAPI

import models.admin_repository.schema
import models.checkout_repository.schema
import models.user_repository.schema
import models.utility_repository.schema

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings
import os

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware()
