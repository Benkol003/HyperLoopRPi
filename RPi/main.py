from fastapi import FastAPI

import random

app = FastAPI()

##fill out to add data
@app.get("/")
async def update():
    return {"Hyperloop RPi": "Hello There.",
            "Tempurature": random.randint(0,100)
            }
