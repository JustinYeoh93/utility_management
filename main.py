from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello world'}


@app.get('/favicon.ico')
def ico():
    return {'message': 'No favicon/ico'}
