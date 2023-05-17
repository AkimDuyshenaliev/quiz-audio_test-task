from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db import Base


metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    username = Column(String)