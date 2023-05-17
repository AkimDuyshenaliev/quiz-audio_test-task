from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.utils.question import askQuestion

questionRouter = APIRouter(
    tags=['question'],
    prefix='/ask-question'
)


@questionRouter.post('', status_code=200)
def askQuestionRouter(questions_num: int, db: Session = Depends(get_db)):
    """ Выбрать количество вопросов """
    return askQuestion(questions_num=questions_num, db=db)