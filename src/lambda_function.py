import json
import boto3
import os 

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])  # Use the environment variable for the table name

def lambda_handler(event, context):
    response = table.update_item(
        Key={"id": "counter"},
        UpdateExpression="ADD #count :increment",
        ExpressionAttributeNames={
            "#count": "count"
        },
        ExpressionAttributeValues={
            ":increment": 1
        },
        ReturnValues="UPDATED_NEW"
    )

    count = int(response["Attributes"]["count"])

    return {
        "statusCode": 200,
        "body": json.dumps({"count": count})
    }