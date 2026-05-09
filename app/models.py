from datetime import datetime

from sqlalchemy import DateTime, func, Boolean, String, Text, ForeignKey, JSON, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column( unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

class Track(Base):
    __tablename__ = 'tracks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str|None] = mapped_column(Text, nullable = True)
    sort_order: Mapped[int] = mapped_column(nullable = False , default = 0)
    is_published: Mapped[bool] = mapped_column(Boolean , nullable = False , default = False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default =  func.now(), nullable = False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable =False)



class Lesson(Base):
    __tablename__ = 'lessons'
    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'),nullable=False)
    title: Mapped[str] = mapped_column(String(255) , nullable=False)
    content: Mapped[str | None] = mapped_column(Text , nullable = True)
    sort_order: Mapped[int] = mapped_column(nullable = False , default = 0)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())



class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int]= mapped_column(primary_key=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lessons.id'),nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str|None] = mapped_column(Text, nullable = True)
    task_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    difficulty: Mapped[int] = mapped_column(
        nullable = False ,
        default = 1
    )
    metadata_: Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
        nullable = True
    )
    sort_order: Mapped[int] = mapped_column(
        nullable = False,
        default = 0
    )
    is_published: Mapped[bool] = mapped_column(Boolean, nullable = False, default= False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

class Attempt(Base):
    __tablename__ = 'attempts'
    __table_arge__ = (
        CheckConstraint(
            "status IN ('submitted','in review','reviewed','rejected')",
            name="ck_attempts_status"
        )
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    answer_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default = "submitted",
        server_default = "submitted"
    )
    metadata_ : Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
        nullable = True
    )
    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

class Review(Base):
    __tablename__ = "reviews"

    __table_arge__ = (
        UniqueConstraint("attempt_id",name = "uq_reviews_attempt_id"),
        CheckConstraint("score BETWEEN 0 and 100",
                        name = "ck_reviews_score_range"
                        ),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt_id: Mapped[int] = mapped_column(ForeignKey('attempts.id'),nullable=False, unique=True)
    reviewer_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    score: Mapped[float] = mapped_column(nullable=False)
    feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

class Progress(Base):
    __tablename__ = "progress"
    __table_args__ = (
    UniqueConstraint("user_id", "lesson_id", name="uq_progress_user_lesson"),

    CheckConstraint(
        "status IN ('not_started','in_progress','completed')",
        name="ck_progress_status"
    )
    ,
    CheckConstraint("completion_percent BETWEEN 0 and 100",
                    name="ck_progress_completion_percent_range"
                    ),
    CheckConstraint("mastery_score BETWEEN 0 and 100",
                    name="ck_mastery_score_range"
                    )
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lessons.id'),nullable=False)
    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default = "not_started"
    )
    completion_percent: Mapped[int] = mapped_column(nullable=False , default=0)
    mastery_score: Mapped[int] = mapped_column(nullable=False , default=0)
    last_activity_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    metadata_: Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

class Notification(Base):
    __tablename__ = "notifications"
    __table_args__ = (
        CheckConstraint(
            "kind IN ('review_completed','progress_updated','system')",
            name="ck_notifications_kind",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False,
    )
    kind: Mapped[str] = mapped_column(String(50),nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str | None] = mapped_column(Text, nullable=True)
    payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    is_read: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    read_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[int] = mapped_column(primary_key=True)
    actor_user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'),nullable=True)
    action: Mapped[str] = mapped_column(String(100),nullable=False)
    entity_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    entity_id: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    metadata_: Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
class IdempotencyKey(Base):
    __tablename__ = "idempotency_keys"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "key",
            "operation",
            name = "uq_idempotency_user_key_operation"
        ),
        CheckConstraint(
            "status IN ('processing','completed','failed')",
            name = "ck_idempotency_user_key_status"
        )
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    key: Mapped[str] = mapped_column(String(255),nullable=False)
    operation: Mapped[str] = mapped_column(String(100),nullable=False)
    status: Mapped[str] = mapped_column(
        String(30),
        nullable = False,
        default = "processing",
        server_default="processing",

    )
    response_body: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )