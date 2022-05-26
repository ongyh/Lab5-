# System imports
from time import sleep

# Local imports
from hal import hal_keypad as keypad
from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_adc as adc
from hal import hal_servo as servo

import adc_servo_controller as adc_c
import led_control
import clock

def main():
    #Initiallize LED driver
    #led.init()                                             #for LED code
    #led_control.led_control_init()
    #adc.init()                                             #for adc code
    #servo.init()
    #adc_c.adc_servo_init()

    clock.clock_init()

    #led_control.check_keypad(LCD)                           #for led code
    #adc_c.check_adc_servo()                                #for adc code

    #Initiallize Keypad driver
    #led_control.led_control_init()                          #for led code
    #keypad.init()                                           #for led code

    # Instantiate and initialize the LCD driver
    lcd = LCD.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    #Clear LCD and display message
    lcd.lcd_clear()
    lcd.lcd_display_string("DevOps for AIoT", 1)  # write on line 1
    lcd.lcd_display_string("Lab 5", 2)  # write on line 2
    sleep(3.0)



# Main entry point
if __name__ == "__main__":
    main()

