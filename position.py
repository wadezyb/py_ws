#!/usr/bin/python
import time
import serial

num = 10
delay = 2.5
port = '/dev/ttyUSB0'
ser=serial.Serial()
ser.port = port
ser.baudrate = 115200
ser.writeTimeout = 0
ser.open()
if ser.isOpen():
  print('Open Port: '+ser.port+' Successfully!\n')
  ser.write('t\r\n')
  time.sleep(0.5)
  print('Unit Mode: Profile Position Mode\n')
  ser.write('UM 1\r\n')
  time.sleep(2)
  print('Motor On\n')
  ser.write('MO 1\r\n')
  time.sleep(2)
  c = 0
  while c<num:
    c=c+1
    print(c)
    ser.write('cmdP 100000\r\n')
    time.sleep(delay)
    ser.write('cmdP 0\r\n')
    time.sleep(delay)

  ser.close()
else:
  print('Failed to open Serial Port')

