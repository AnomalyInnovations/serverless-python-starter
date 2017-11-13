import json
import numpy as np

def hello(event, context):
    body = {
        "message": "Python Hello!!",
    }

    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
