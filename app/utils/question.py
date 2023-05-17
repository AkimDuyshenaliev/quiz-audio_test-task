from fastapi import HTTPException
from sqlalchemy.orm import Session
import requests
from app.models import Question


def askQuestion(questions_num: int, db: Session):
    if questions_num is not int:
        raise HTTPException(status_code=400, detail='Incorrect input data type')

    qNum: int = questions_num if questions_num <= 100 else 100 
    link: str = f'https://jservice.io/api/random?count={qNum}'
    questionData: list = requests.get(link).json()
    if not questionData:
        return {}

    count: int = 0
    while count != qNum:
        if db.query(Question).filter(Question.question_id == questionData[count]['id']).first():
            link = f'https://jservice.io/api/random?count=1'
            questionData[count] = requests.get(link).json()[0]
            continue
        db_question = Question(
            question_id=questionData[count]['id'],
            question_text=questionData[count]['question'],
            answer_text=questionData[count]['answer'],
            created_at=questionData[count]['created_at'])
        db.add(db_question)
        db.commit()
        count += 1
    db.refresh(db_question)
    return db_question