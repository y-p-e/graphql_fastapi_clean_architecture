import uvicorn
from fastapi import FastAPI
from models import Base
from database import engine
from entities.user_entitiy import UserBaseModel
from entities.user_entitiy import UserBaseModel
from controllers.rest_controller import RestUserController
import strawberry
from strawberry.fastapi import GraphQLRouter
from entities.user_entitiy import UserType
from strawberry import ID
from controllers.graphql_controller import GrapqlUserController


Base.metadata.create_all(bind=engine)


#GraphQL
@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, user_id: ID) -> UserType:
        return GrapqlUserController().get_user(user_id)

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


#REST
@app.get("/user/", response_model=UserBaseModel)
def get_user(user_id: int):
    return RestUserController().get_user(user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)