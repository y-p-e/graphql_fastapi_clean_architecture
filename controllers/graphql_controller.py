import base64
from entities.user_entitiy import UserFilter, UserBaseModel
from usecases.get_user import UserUseCase
from strawberry import ID
from presetners.user_presenter import UserPresenter


class GrapqlUserController:
	def get_user(self, user_id: ID):
		user_id_base64_str = base64.b64decode(user_id).decode()
		user_id_str = user_id_base64_str[5:]
		user_id_int = int(user_id_str)
		user_filter = UserFilter(user_id=user_id_int)
		user_base_model: UserBaseModel = UserUseCase().get_user(user_filter)
		return UserPresenter().create_schema(user_base_model)
