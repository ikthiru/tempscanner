import serial
import csv
import datetime
import RPi.GPIO as GPIO
import time

hid = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)
temp = serial.Serial('/dev/ttyUSB1', 115200, timeout=0)
x = datetime.datetime.now()
tiktok = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(tiktok, GPIO.OUT)

hid.flush()
temp.flush() 

temp_map = {'4512991' : 34,
'4578528' : 34.1,
'4644065' : 34.2,
'4709602' : 34.3,
'4775139' : 34.4,
'4840676' : 34.5,
'4906213' : 34.6,
'4971750' : 34.7,
'5037287' : 34.8,
'5102824' : 34.9,
'5168361' : 35,
'5233898' : 35.1,
'5299435' : 35.2,
'5364972' : 35.3,
'5430509' : 35.4,
'5496046' : 35.5,
'5561583' : 35.6,
'5627120' : 35.7,
'5692657' : 35.8,
'5758194' : 35.9,
'5823731' : 36,
'5889268' : 36.1,
'5954805' : 36.2,
'6020342' : 36.3,
'6085879' : 36.4,
'6151416' : 36.5,
'6216953' : 36.6,
'6282490' : 36.7,
'6348027' : 36.8,
'6413564' : 36.9,
'6479101' : 37,
'6544638' : 37.1,
'6610175' : 37.2,
'6675712' : 37.3,
'6741249' : 37.4,
'6806786' : 37.5,
'6872323' : 37.6,
'6937860' : 37.7,
'7003397' : 37.8,
'7068934' : 37.9,
'7134471' : 38,
'7200008' : 38.1,
'7265545' : 38.2,
'7331082' : 38.3,
'7396619' : 38.4,
'7462156' : 38.4,
'7527693' : 38.5,
'7593230' : 38.6,
'7658767' : 38.7,
'7724304' : 38.8,
'7789841' : 38.9,
'7855378' : 39,
'7920915' : 39.1,
'7986452' : 39.2,
'8051989' : 39.3,
'8117526' : 39.4,
'8183063' : 39.5,
'8248600' : 39.6,
'8314137' : 39.7,
'8379674' : 39.8,
'8445211' : 39.9,
'8510748' : 40,
'8576285' : 40.1,
'8641822' : 40.2,
'8707359' : 40.3,
'8772896' : 40.4,
'8838433' : 40.5,
'8903970' : 40.6,
'8969507' : 40.7,
'9035044' : 40.8,
'9100581' : 41}

while True:
    if temp.in_waiting > 0: #True:
        tempread = temp.readline(17)
        tempread1 = int.from_bytes(tempread, 'big', signed=True)
        convert = repr(tempread1)[-7:] 
        hidraw = hid.readline(10).decode('utf-8').rstrip()
        if len(hidraw) > 0:
            print(hidraw)
            if temp_map[convert] <= 37.3:
                GPIO.output(23, GPIO.LOW)
                time.sleep(1)
                GPIO.output(23, GPIO.HIGH)
                print("buzzer triggered")
            else:
                pass
            with open('log.csv', 'a', newline='') as csvfile:
                fieldnames = ['date' , 'temp', 'card']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'date':datetime.datetime.now() ,'card':hidraw,'temp':temp_map[convert]})