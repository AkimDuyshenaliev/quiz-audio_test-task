from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import User, AudioFile


def downloadAudio(audioId, userId, db) -> str:
    user = User(id=userId)
    file = AudioFile(fileUUID=audioId)