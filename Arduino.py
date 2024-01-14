import pyfirmata
import time

comport='COM4'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:11:o')
mforward=board.get_pin('d:2:o')
mreverse=board.get_pin('d:3:o')

def led(total):
    if total==0:
        led_1.write(1)
        time.sleep(1)
        led_1.write(0)
        

def motorforward():
    mforward.write(1)
    time.sleep(1)
    mforward.write(0)
        
def motorreverse():
    mreverse.write(1)
    time.sleep(1)
    mreverse.write(0)   
