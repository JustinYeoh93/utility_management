from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings
import os

from starlette.graphql import GraphQLApp
from starlette.datastructures import Secret

from graphql_repo.mutation import Mutation
from graphql_repo.schema import Query

import graphene
import uvicorn

app = FastAPI()


app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

