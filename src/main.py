import sensors
import time
import aws

print('Welcome to Serverless Farm')

totalReadsCount = 0
successfulReadsCount = 0

def process_sensor(sensor_id):
    sensor_data = sensors.read(sensor_id)
    if sensor_data is not None:
        print('{} T={}C / Rh={}%'.format(sensor_data.sensor_name, sensor_data.temperature,sensor_data.humidity))
        aws.submitReading(sensor_data)
    else:
        print('reading failed')

while True:
    process_sensor(sensors.ID.SENSOR1)
    process_sensor(sensors.ID.SENSOR2)
    time.sleep(60)
