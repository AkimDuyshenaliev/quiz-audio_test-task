from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import User, AudioFile


def downloadAudio(audioId, userId, db) -> str:
    file = db.query(AudioFile).filter(AudioFile.ownerID==userId, AudioFile.id==audioId).first()
    return file.fileLocation