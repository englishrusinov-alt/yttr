from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Track


class TrackRepository:
    def __init__(self,session:Session)->None:
        self.session = session

    def get_by_id(self,track_id:int)->Track | None:
        stmt = select(Track).where(Track.id == track_id)
        return self.session.scalar(stmt)

    def get_by_title(self,title:str)->Track | None:
        stmt = select(Track).where(Track.title == title)
        return self.session.scalar(stmt)


    def create(self,title:str , description:str)->Track:
        track = Track(title = title,description = description)
        self.session.add(track)
        self.session.flush()
        self.session.refresh(track)
        return track
    def update(self,track:Track, **fields:object)->Track:
        allowed_fields = {"title","description"}

        for field_name , value in fields.items():
            if field_name not in allowed_fields:
                raise ValueError(f"Cannot update field: {field_name}")
            setattr(track,field_name,value)
        self.session.add(track)
        self.session.flush()
        self.session.refresh(track)
        return track