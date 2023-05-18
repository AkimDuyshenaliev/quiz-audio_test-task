from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db import Base


metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    username = Column(String)

    _audioFiles = relationship("AudioFile")


class AudioFile(Base):
    __tablename__ = "audioFile"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    fileUUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ownerID = Column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    fileLocation = Column(String)


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    question_id = Column(Integer, unique=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at= Column(DateTime)