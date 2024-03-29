import time
import os
import psutil
import ctypes


ctypes.windll.user32.MessageBoxW(0,u"Close this window now",u"Programm started",16)
timer = 0
battery = psutil.sensors_battery()
shown = False
def timeradd(t):
    global timer
    timer += t
    time.sleep(t)

def main():
    global shown
    global timer
    global battery
    battery = psutil.sensors_battery()
    while battery.power_plugged == False:
        if battery.percent < 60 and shown == False:
            timerPrint = timer/60
            ctypes.windll.user32.MessageBoxW(0, u"Change battery now \n After "+str(timerPrint)+ "minutes of working 60 Percent has been reached.", u"Important Message",16)
            shown = True
            break
        
        timeradd(60)
        battery = psutil.sensors_battery()

if __name__ == '__main__':
    while shown == False:
        main()
        while battery.power_plugged == True:
            time.sleep(60)
        else:
            shown = False