import json
import requests
import boto3 
import os

from datetime import datetime

BUCKET_NAME = os.getenv("BUCKET_NAME")

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client("s3")

    start_date = datetime.now().date()
    end_date = start_date 

    response = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key=DEMO_KEY")
    if response.status_code == 200:
        data = response.json()

        with open("/tmp/data.json", "w") as _file:
            _file.write(json.dumps(data["near_earth_objects"]))
            client.put_object(Body=json.dumps(data["near_earth_objects"]), Bucket = BUCKET_NAME, Key = "near_earth_objects")
    return {
        'statusCode': 200,
        'body': 'done'
    }

