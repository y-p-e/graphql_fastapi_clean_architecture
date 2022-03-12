import strawberry
from strawberry.fastapi import GraphQLRouter
from entities.user_entitiy import UserType
from strawberry import ID
from controllers.graphql_controller import GrapqlUserController

#GraphQL
@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, user_id: ID) -> UserType:
        return GrapqlUserController().get_user(user_id)

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)