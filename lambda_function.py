import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("BusTickets")

def _resp(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, ensure_ascii=False)
    }

def lambda_handler(event, context):
    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return _resp(200, {"ok": True})

    try:
        body = json.loads(event.get("body") or "{}")

        required = ["tripType","fromCity","fromStation","toCity","toStation","travelDate","passengers","seatNumber","email","ticketType"]
        missing = [k for k in required if not body.get(k)]
        if missing:
            return _resp(400, {"error": f"Missing fields: {', '.join(missing)}"})

        ticket_id = str(uuid.uuid4())
        item = {
            "ticketId": ticket_id,
            "tripType": body["tripType"],
            "fromCity": body["fromCity"],
            "fromStation": body["fromStation"],
            "toCity": body["toCity"],
            "toStation": body["toStation"],
            "travelDate": body["travelDate"],
            "passengers": int(body.get("passengers", 1)),
            "seatNumber": body["seatNumber"],
            "email": body["email"],
            "ticketType": body["ticketType"],
            "createdAt": datetime.utcnow().isoformat(timespec="seconds") + "Z"
        }
        table.put_item(Item=item)

        return _resp(200, {"message": "Booking successful", "ticketId": ticket_id})
    except Exception as e:
        return _resp(500, {"error": str(e)})
