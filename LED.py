import time
from machine import Pin
LED1 = Pin(2,Pin.OUT)
LED2 = Pin(0,Pin.OUT)    
while True:
	LED1.value(1)
 	time.sleep(1)
 	LED1.value(0)
 	time.sleep(1)
 	LED2.value(1)
 	time.sleep(1)
 	LED2.value(0)
 	time.sleep(1)