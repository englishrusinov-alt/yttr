from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User


class UserRepository:
    def __init__(self,session:Session)->None:
        self.session = session

    def get_by_id(self,user_id:int)->User | None:
        stmt = select(User).where(User.id == user_id)
        return self.session.scalar(stmt)
    def get_by_email(self,email:str)->User | None:
        stmt = select(User).where(User.email==email)
        return self.session.scalar(stmt)

    def create(self,email:str , is_active: bool=True)->User:
        user = User(email = email,is_active = is_active)
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user
    def update(self,user:User, **fields:object)->User:
        allowed_fields = {"email","is_active"}

        for field_name , value in fields.items():
            if field_name not in allowed_fields:
                raise ValueError(f"Cannot update field: {field_name}")
            setattr(user,field_name,value)
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user