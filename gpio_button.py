from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(2)
led = LED(17)
light = False 


def lightSwitch(flag):
    "Switches off and on LED on 17th pin and prints out message in console"
    if (flag == False):
        print('Turning on lights!')
        led.on()
        flag = True
    else:
        print('Turning off lights!')
        led.off()
        flag = False
    return flag



while True:
    button.wait_for_press()
    #light = lightSwitch(light)
    led.toggle()
    button.wait_for_release()


