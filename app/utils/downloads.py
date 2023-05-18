from fastapi import HTTPException
from app.models import User, AudioFile


def downloadAudio(audioId: int, userId: int, db) -> str:
    if type(audioId) is not int or type(userId) is not int:
        raise HTTPException(status_code=400, detail='Incorrect input data type')

    file = db.query(AudioFile).filter(AudioFile.ownerID==userId, AudioFile.id==audioId).first()
    return file.fileLocation