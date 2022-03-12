from enum import IntEnum
from . import dht11

class ID(IntEnum):
    SENSOR1 = 3
    SENSOR2 = 4

class SensorReadingResult:
    def __init__(self, sensor_name, temperature, humidity):
        self.sensor_name = sensor_name
        self.temperature = temperature
        self.humidity = humidity

def read(sensor):
    result = dht11.readSensor(sensor)
    if result is not None:
        return SensorReadingResult(sensor.name, result[0], result[1])
    return None

