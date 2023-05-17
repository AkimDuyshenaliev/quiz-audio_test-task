from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db import get_db
from app.utils.downloads import downloadAudio

downloadsRouter = APIRouter(
    tags=['record'],
    prefix='/record'
)


@downloadsRouter.get('', status_code=200)
def downloadAudioRouter(id: int, user: int, db: Session = Depends(get_db)):
    """ Скачать аудиофайл по id пользователя и uuid аудиофайла """
    return FileResponse(downloadAudio(audioId=id, userId=user, db=db))