from fastapi import UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import User, Audio

from pydub import AudioSegment

import os
import shutil
import uuid


def createUser(username: str, db: Session):
    newUser = User(username=username)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    createdUser: object = db.query(User).filter(User.username==username).order_by(desc(User.id)).first() 
    return {'id': createdUser.id, 'token': createdUser.token}


def addAudio(userId: int, file: UploadFile, db: Session):
    print(userId)
    user = db.query(User).filter(User.id==userId).first() 
    imageUUID = uuid.uuid4()
    userFolder = f'user-{user.id}-{user.username}'
    convertedFileName = f'{imageUUID}.mp3'
    os.mkdir(f'static/{userFolder}')

    # сохранить wav
    with open(f"static/{userFolder}/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # конвертировать wav в mp3
    sound = AudioSegment.from_wav(f'static/{userFolder}/{file.filename}')
    sound.export(f'static/{userFolder}/{convertedFileName}', format="mp3")

    try:
        os.remove(f'static/{userFolder}/{file.filename}')
    except OSError:
        pass

    # newAudio = Audio(ownerUserId=)
