from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.types import Float
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import relationship

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_URL="postgresql://osxhgvdnwkrrsx:03aa7fc38ea3842c590df8e451a160fc593eb770287a3440ff005797b79b1125@ec2-34-230-110-100.compute-1.amazonaws.com:5432/d9393lnt8ndre9"
print(DATABASE_URL)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

ledgers = sqlalchemy.Table(
    'ledger',
    metadata,
    sqlalchemy.Column("order_no", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("datatime", sqlalchemy.DateTime),
    sqlalchemy.Column("primary_category", sqlalchemy.String),
    sqlalchemy.Column("secondary_category", sqlalchemy.String),
    sqlalchemy.Column("contents", sqlalchemy.String),
    sqlalchemy.Column("answer", sqlalchemy.String),
    sqlalchemy.Column("latitude", Float,),
    sqlalchemy.Column("longitude", Float),
    # mesh = relationship("mesh")
)

# meshs = sqlalchemy.Table(
#     'mesh',
#     metadata,
#     sqlalchemy.Column("latitude", sqlalchemy.String,),
#     sqlalchemy.Column("longitude", sqlalchemy.String),
#     sqlalchemy.Column('orde_no', sqlalchemy.String), \
#                   ForeignKey('ledger.order_no')
#     ledger = relationship("ledger")
# )


engine = sqlalchemy.create_engine(
    # DATABASE_URL, connect_args={"check_same_thread": False}
    DATABASE_URL
)
metadata.create_all(engine)


class LedgerIn(BaseModel):
    order_no: str
    datatime: datetime
    primary_category: str
    secondry_category: str
    contents: str
    answer: str
    latitude: Float
    longitude: Float


class Ledger(BaseModel):
    order_no: str
    datatime: datetime
    primary_category: str
    secondry_category: str
    contents: str
    answer: str
    latitude: Float
    longitude: Float


# class MeshIn(BaseModel):
#     order_no: str
#     latitude: str
#     longitude: str


# class Mesh(BaseModel):
#     order_no: str
#     latitude: str
#     longitude: str



app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/")
async def root():
    return {"message": "Hello World"}



# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get("/ledger/{id}/", response_model=Ledger)
async def read_ledgers(id: str):
    # query = ledgers.select()
    query = "SELECT * FROM ledger WHERE order_no=(%s)"
    with engine.connect() as connection:
        result = connection.execute(query,id)
        for r in result:
            return JSONResponse(content={
                    "order_no": r[0],
                    "datatime": str(r[1]),
                    "primary_category": r[2],
                    "secondry_category": r[3],
                    "contents": r[4],
                    "latitude": r[5],
                    "longitud": r[6]
                    })

# @app.post("/ledger/", response_model=Ledger)
# async def create_ledger(ledger: LedgerIn):
#     query = ledgers.insert().values(text=ledger.text, completed=ledger.completed)
#     last_record_id = await database.execute(query)
#     return {**ledger.dict(), "orde_no": last_record_id}