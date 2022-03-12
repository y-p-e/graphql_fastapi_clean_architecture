from fastapi import FastAPI
from models import Base
from database import engine
from entities.user_entitiy import UserBaseModel
from graphql_query import graphql_app
from entities.user_entitiy import UserBaseModel
from controllers.rest_controller import RestUserController


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/user/", response_model=UserBaseModel)
def get_user(user_id: int):
    return RestUserController().get_user(user_id)
