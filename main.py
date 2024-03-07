from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

##fill out to add data
@app.get("/")
async def update():
    return {"Hyperloop RPi": "Hello There.",
            "tempurature": random.randint(0,100)
            }


############ CAN ############

#see https://python-can.readthedocs.io/en/stable/ for documentation

#STM32 Nucleo F446RE boards: CAN baud rate is recommended 875 KBits for a prescaler of 16, (or 999KBits for prescaler 14).

uvicorn.run(app,host="hyperloop",port=8000)