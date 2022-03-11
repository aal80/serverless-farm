import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_SENSOR1_PIN = 3
DHT_SENSOR2_PIN = 4

def readSensor(name, pin):
    humidity, temp = Adafruit_DHT.read(DHT_SENSOR, pin)
    if humidity is not None and temp is not None:
        print("{0:s} :: Humidity={2:0.1f} Temp={1:0.1f}".format(name, temp, humidity))
        return True
    else:
        print("{0:s} :: Failed to read sensor data".format(name))
        return False
        
totalReadsCount = 0
successfulReadsCount = 0

while True:
    totalReadsCount+=1
    if readSensor('Sensor1',DHT_SENSOR1_PIN):
        successfulReadsCount+=1
    
    totalReadsCount+=1
    if readSensor('Sensor2',DHT_SENSOR2_PIN):
        successfulReadsCount+=1
    
    successRate = successfulReadsCount / totalReadsCount
    print("{0:d} / {1:d} {2:f}".format(successfulReadsCount,totalReadsCount,successRate))
        
    time.sleep(3)

    
    