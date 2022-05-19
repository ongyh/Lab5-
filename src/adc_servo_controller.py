from time import sleep
from threading import Thread
from hal import hal_adc as adc
from hal import hal_servo as servo


def adc_servo_init():
    global adc_value
    t1 = Thread(target=adc_servo_thread)
    t1.start()


def adc_servo_thread():
    global adc_value
    while True:
        adc_value = adc.get_adc_value(1)  #channel 1 = potentialmeter & [probably returns 0 - 1023 vlaue]


def check_adc_servo():
    global adc_value
    if adc_value <= 1023:
        percentage = (100 - ((int(adc_value) / 1023) * 100))
        servo.set_servo_position((percentage/100)*180)
