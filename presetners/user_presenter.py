import base64
from entities.user_entitiy import UserBaseModel, UserType


class UserPresenter:
	def create_schema(user_base_model: UserBaseModel):
		user_id_str = str(user_base_model.id)
		user_id_base64 = base64.b64encode(user_id_str.encode()).decode()
		user_type = UserType.from_pydantic(user_base_model)
		user_type.id = user_id_base64
		return user_type
