from fastapi import FastAPI
import random
import os
import can

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

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

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native

while True:
    msg = can0.recv(5.0)
    print (msg)
    if msg is None:
        print('Timeout occurred, no message.')

os.system('sudo ifconfig can0 down')