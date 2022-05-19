import time
from threading import Thread
from hal import hal_lcd as LCD
# gets list of unchangeable data (year,month,day,hour,min,sec,)


def clock_init():
    t1 = Thread(target=clock_thread)
    t1.start()


def clock_thread():
    lcd = LCD.lcd()
    while(True):
        # gets list of unchangeable data (year,month,day,hour,min,sec,)
        local_time = time.localtime()

        # search strftime online to see all possible prints
        row1 = time.strftime("%I:%M:%S%p", local_time)
        # %H=hour, %M=minute, %S=seconds, %Y=year in numbers, %a=month in abbreviated str, %b=day in abbreviated str
        row2 = time.strftime("%a:%b:%Y", local_time)

        lcd.lcd_display_string(str(row1), 1)
        lcd.lcd_display_string(str(row2), 2)
        time.sleep(1)

        #second requirement of removing ":"
        row1 = time.strftime("%I %M %S%p", local_time)
        row2 = time.strftime("%a %b %Y", local_time)
        lcd.lcd_display_string(str(row1), 1)
        lcd.lcd_display_string(str(row2), 2)
        time.sleep(1)
