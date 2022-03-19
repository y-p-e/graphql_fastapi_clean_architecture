from entities.user_entitiy import UserFilter, UserBaseModel
from database import SessionLocal 
from models import User

class UserUseCase:
  def get_user(self, user_filter: UserFilter):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_filter.user_id).one()
    user_base_model = UserBaseModel.from_orm(user)
    return user_base_model

