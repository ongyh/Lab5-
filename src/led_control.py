from hal import hal_led as led
from threading import Thread
from time import sleep
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD


def led_control_init():
    global delay

    t1 = Thread(target=led_thread)
    t1.start()
    # Set initial LED blinking every 1 second after Thread starts
    delay = 1


def led_thread():
    global delay
    delay = 0

    while(True):
        if delay != 0:
            led.set_output(20,1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)


def check_keypad(lcd):
    global delay
    lcd = LCD.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)  # write on line 1
    lcd.lcd_display_string("0: OFF 1: BLINK", 2)  # write on line 2

    while(True):
        #Add code here to read from keypad and control LED
        keypad.init()
        keypadinp = keypad.get_key()
        if keypadinp == 1:
            print("Value entered : " + str(keypadinp))
            lcd.lcd_clear()
            delay = 1
            lcd.lcd_display_string("LED Control", 1)
            lcd.lcd_display_string("Blink LED", 2)
        elif keypadinp == 0:
            print("Value entered" + str(keypadinp))
            lcd.lcd_clear()
            delay = 0
            lcd.lcd_display_string("LED Control", 1)
            lcd.lcd_display_string("OFF LED", 2)
        else:
            print("Value entered" + str(keypadinp))
            lcd.lcd_clear()
            lcd.lcd_display_string("Wrong input", 1)
            lcd.lcd_display_string("type again lah", 2)







