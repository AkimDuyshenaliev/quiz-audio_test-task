from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import User, AudioFile


def downloadAudio(audioId: int, userId: int, db) -> str:
    if audioId or userId is not int:
        raise HTTPException(status_code=400, detail='Incorrect input data type')

    file = db.query(AudioFile).filter(AudioFile.ownerID==userId, AudioFile.id==audioId).first()
    return file.fileLocation