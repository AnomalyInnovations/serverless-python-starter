import json
import numpy as np

def hello(event, context):
  array = np.arange(15).reshape(3, 5)
  array_str = ','.join(str(x) for x in array)
  body = {
    "message": "Python numpy example: " + array_str,
  }

  return {
      "statusCode": 200,
      "body": json.dumps(body)
  }
