from fastapi import APIRouter, Depends, UploadFile, Request
from sqlalchemy.orm import Session
from app.db import get_db
from app.utils.users import createUser, addAudio

userRouter = APIRouter(
    tags=['user'],
    prefix='/user'
)


@userRouter.post('/create', status_code=200)
def createUserRouter(username: str, db: Session = Depends(get_db)):
    """ Создать пользователя с указанным именем """
    return createUser(username=username, db=db)


@userRouter.post('/add-audio', status_code=200)
def addAudioRuter(userId:int, token: str, file: UploadFile, request: Request, db: Session = Depends(get_db)):
    """ Загрузить аудиофайл по id пользователя """
    return addAudio(userId=userId, token=token, file=file, url=request.url._url, db=db)