from fastapi import FastAPI
from database import Base, SessionLocal, engine

from models import user, admin, checkout, utility

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello world'}


@app.get('/favicon.ico')
def ico():
    return {'message': 'No favicon/ico'}
