Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from gpiozero import LED
l
>>> led = LED(17)
>>> from gpiozero import LED
>>> led = LED(17)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    led = LED(17)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 135, in __call__
    self = super(GPIOMeta, cls).__call__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 131, in __init__
    super(DigitalOutputDevice, self).__init__(pin, active_high, initial_value)
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 41, in __init__
    super(OutputDevice, self).__init__(pin)
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 69, in __init__
    super(SourceMixin, self).__init__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 386, in __init__
    'pin %r is already in use by another gpiozero object' % pin
gpiozero.exc.GPIOPinInUse: pin GPIO17 is already in use by another gpiozero object
>>> led.on()
>>> led.off()
>>> 
