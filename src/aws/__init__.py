import boto3
import sensors
import time
import json

TABLE_NAME = 'serverless-farm'

lambdaClient = boto3.client('lambda')

ddb = boto3.resource('dynamodb')
table = ddb.Table(TABLE_NAME)

def submitReading(sensor_data):
    event = dict()
    event['sensorName']=sensor_data.sensor_name
    event['temperature'] = int(sensor_data.temperature)
    event['humidity'] = int(sensor_data.humidity)

    resp = lambdaClient.invoke_async(
        FunctionName='arn:aws:lambda:us-east-1:281024298475:function:serverless-farm-data-receiver',
        InvokeArgs=json.dumps(event)
    )
    #print(resp)

    # table.put_item(
    #     Item={
    #         'SensorId':sensor_data.sensor_name,
    #         'Temperature': int(sensor_data.temperature),
    #         'Humidity': int(sensor_data.humidity),
    #         'Timestamp': int(time.time())
    #     }
    # )


