from fastapi import FastAPI
from src.tracker import changePrecision, changeState, startTracker, stopTracker
from src.control import openKeyboard
app = FastAPI()


@app.get("/precision")
async def precision():
    try:
        changePrecision()
        return {'response': 'Successful'}
    except:
        return {'response': 'Error'}


@app.get("/state")
async def state():
    try:
        changeState()
        return {'response': 'Successful'}
    except:
        return {'response': 'Error'}


@app.get("/keyboard")
async def keyboard():
    try:
        openKeyboard()
        return {'response': 'Successful'}
    except:
        return {'response': 'Error'}


@app.get("/start")
async def start():
    try:
        startTracker()
        return {'response': 'Successful'}
    except:
        return {'response': 'Error'}


@app.get("/quit")
async def quit():
    try:
        stopTracker()
        return {'response': 'Successful'}
    except:
        return {'response': 'Error'}
