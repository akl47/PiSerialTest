import serial
s = serial.Serial('/dev/ttyACM0')
print(s.name)
s.write(b'color:00ff00\n')
s.close()