__author__ = "Alishan Hassan"

import serial
import time

#print("Serial Data Logging from COM4 at 9600 Baud")

ser = serial.Serial('COM4', 9600, timeout=0)

filename = "data" + "_" + time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + "_" + time.strftime("%H") + time.strftime("%M") + time.strftime("%S") + ".txt"
file = open(filename, 'wb')

header = "Elapsed,PiezoValue,BucketFlip,BucketCount".encode('ascii')
print(time.strftime("%c"))
print(header)

file.write(header)
file.write("\n".encode('ascii'))

time.sleep(1) #give a one second delay so we don't get garbled data

x = 0
while 1:
	if x > 15:	
		line = ser.readline()
		print(line)
		file.write(line)
	x += 1
	#time.sleep(.01) #this is only really necessary when printing to the console
	
file.close()