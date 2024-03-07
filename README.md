## HyperloopRPi

Code to run on the raspberry pi main controller in the UoM Hyperloop society's pod.

The RPi will interact with STM32 microcontrollers via a CAN Bus.
Docs for using the RPi CAN hat [here](https://www.waveshare.com/wiki/RS485_CAN_HAT), or see [python-can](https://python-can.readthedocs.io/en/stable/).

Communication with the [base station](https://github.com/Benkol003/HyperloopUI) is faciliated through a JSON server.

## Dependencies
Install pip requirements with `pip install -r requirements.txt`.