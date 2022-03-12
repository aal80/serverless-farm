import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
def readSensor(pin):
    humidity, temp = Adafruit_DHT.read(DHT_SENSOR, pin)
    if humidity is not None and temp is not None:
        #print("{0:s} :: Humidity={2:0.1f} Temp={1:0.1f}".format(name, temp, humidity))
        return (temp, humidity)
    else:
        #print("{0:s} :: Failed to read sensor data".format(name))
        return None

    