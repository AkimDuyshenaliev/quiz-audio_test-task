from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models import User, AudioFile
from urllib.parse import urlparse

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


def addAudio(userId: int, token: str, file: UploadFile, url: str, db: Session):
    if not (user := db.query(User).filter(User.id==userId).first()):
        raise HTTPException(status_code=404, detail='User not found')
    if token != str(user.token):
        raise HTTPException(status_code=403, detail='Wrong access token')

    imageUUID = uuid.uuid4()
    userFolder = f'user-{user.id}-{user.username}'
    convertedFileName = f'{imageUUID}.mp3'
    try:
        os.mkdir(f'static/{userFolder}')
    except FileExistsError:
        pass

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

    fileLocation='static/%s/%s.mp3' % (userFolder, imageUUID)
    newAudio = AudioFile(
        fileUUID=imageUUID, 
        ownerID=user.id, 
        fileLocation=fileLocation)
    db.add(newAudio)
    db.commit()
    # db.refresh(newAudio)

    parsedURL = urlparse(url)
    downloadLink = f'{parsedURL.scheme}://{parsedURL.netloc}/'
    print(downloadLink)

    return {
        'userID': userId, 
        'fileUUID': imageUUID, 
        # 'downloadLink': downloadLink,
        'fileLocation': 'static/%s/%s.mp3' % (userFolder, imageUUID)}
