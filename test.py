import serial
s = serial.Serial('/dev/ttyUSB0')
print(s.name)
s.write(b'color:ff0000')
s.close()