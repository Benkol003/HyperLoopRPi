import signal
import os
import can

run = True

def handler_stop_signals(signum, frame):
    global run
    run = False

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
while run:
    msg = can0.recv(5.0)
    if msg is not None:
        print(msg)


os.system('sudo ifconfig can0 down')