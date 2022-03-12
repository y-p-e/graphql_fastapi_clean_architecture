from entities.user_entitiy import UserFilter
from usecases.get_user import UserUseCase


class RestUserController:
  def get_user(self, user_id: int):
    user_filter = UserFilter(user_id=user_id)
    return UserUseCase().get_user(user_filter)