from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Lesson


class LessonRepository:
    def __init__(self,session:Session)->None:
        self.session = session

    def get_by_id(self,lesson_id:int)->Lesson | None:
        stmt = select(Lesson).where(Lesson.id == lesson_id)
        return self.session.scalar(stmt)

    def get_by_title(self,title:str)->Lesson | None:
        stmt = select(Lesson).where(Lesson.title == title)
        return self.session.scalar(stmt)


    def create(self,track_id:int ,title:str , content:str)->Lesson:
        lesson = Lesson(track_id = track_id , title = title, content= content)
        self.session.add(lesson)
        self.session.flush()
        self.session.refresh(lesson)
        return lesson
    def update(self,lesson:Lesson, **fields:object)->Lesson:
        allowed_fields = {"title","content"}

        for field_name , value in fields.items():
            if field_name not in allowed_fields:
                raise ValueError(f"Cannot update field: {field_name}")
            setattr(lesson,field_name,value)
        self.session.add(lesson)
        self.session.flush()
        self.session.refresh(lesson)
        return lesson