from fastapi import FastAPI, Depends, UploadFile, Form, Request
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sql_models import Perguntas1Create,Perguntas2Create, PerguntasFinaisCreate
from crud_helper import save_perguntas1, save_perguntas2, save_perguntas_finais
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import boto3
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/perguntas1")
def perguntas1(perguntas1: Perguntas1Create, db:Session = Depends(get_db)):
    save_perguntas1(db, perguntas1)
    return "saved"

@app.post("/perguntas2")
def perguntas2(perguntas2: Perguntas2Create, db:Session = Depends(get_db)):
    save_perguntas2(db, perguntas2)
    return "saved"

@app.post("/perguntasfinais")
def perguntas2(perguntasfinais: PerguntasFinaisCreate, db:Session = Depends(get_db)):
    save_perguntas_finais(db, perguntasfinais)
    return "saved"

@app.post("/upload-video")
async def upload(content: Request):
    async with content.form() as form:
      filename = form["blobs"].filename
      contents = await form["blobs"].read()
      with open(filename, "wb") as binary_video_file:
          binary_video_file.write(contents)
      session = boto3.Session(aws_access_key_id=os.environ["aws_access_key_id"], aws_secret_access_key=os.environ["aws_secret_access_key"])
      s3 = session.client('s3')
      s3.put_object(Body=contents, Bucket="lemonstudio-video-oregon", Key=filename)