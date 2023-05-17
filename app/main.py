from fastapi import FastAPI
from app.crud.questionRouters import questionRouter
from app.crud.userRouters import userRouter
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router=questionRouter)
app.include_router(router=userRouter)
