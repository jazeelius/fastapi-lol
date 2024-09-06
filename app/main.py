from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends, APIRouter
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from fastapi.middleware.cors import CORSMiddleware

# from app.routers import vote
from .database import engine, get_db
from . import schemas, utils, models
from .routers import post, user, auth, vote
from . import config
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
#                                 password='jazeel1978', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Error connecting to database:", error)
#         time.sleep(2)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "fuck bitch"}


    









