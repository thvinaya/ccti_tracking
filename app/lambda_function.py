import json

def lambda_handler(event, context):
    print(context)
    print("Lambda function ARN:", context.invoked_function_arn)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda-enterprise!')
    }
