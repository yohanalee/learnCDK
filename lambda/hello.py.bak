import json
import os
from urllib import request
import boto3
from boto3.dynamodb.conditions import Key

# initialise ddb client and ddb_table
ddb = boto3.resource("dynamodb")
ddb_table = ddb.Table(os.environ["DDB_TABLE_NAME"])


def handler(event, context):
    HTTP_REQUEST = event["httpMethod"]

    if HTTP_REQUEST == "POST":
        request_body = json.loads(event["body"])
        for item in request_body:
            ddb_table.put_item(Item=item)
        return _200(request_body)

    if HTTP_REQUEST == "GET":
        result = ddb_table.scan()
        return _200(result["Items"])

    if HTTP_REQUEST == "PUT":
        request_body = json.loads(event["body"])
        response = ddb_table.get_item(Key={"id": request_body["id"]})
        item_to_update = response["Item"]
        item_to_update["name"] = request_body["name"]
        ddb_table.put_item(Item=item_to_update)
        return _200(item_to_update)

    if HTTP_REQUEST == "DELETE":
        request_body = json.loads(event["body"])
        response = ddb_table.delete_item(Key={"id": request_body["id"]})
        return _200(response)


def _200(response_body):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },
        "body": json.dumps(response_body),
    }
