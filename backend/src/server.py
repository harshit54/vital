from fastapi import FastAPI
from tracker import changePrecision, changeState

app = FastAPI()


@app.get("/precision")
async def precision():
    changePrecision()


@app.get("/state")
async def state():
    changeState()
