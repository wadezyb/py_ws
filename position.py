#!/usr/bin/python
import time
import serial

num = 100
delay = 10
ser=serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 115200
ser.writeTimeout = 0
ser.open()
ser.write('t\r\n')
time.sleep(0.5)
ser.write('UM 1\r\n')
time.sleep(2)
ser.write('MO 1\r\n')
time.sleep(2)
c = 0
while c<num:
  c=c+1
  ser.write('cmdP 100000\r\n')
  time.sleep(delay)
  ser.write('cmdP 0\r\n')
  time.sleep(delay)
ser.close()
