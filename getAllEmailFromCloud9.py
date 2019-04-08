import boto3
import hashlib
import json


# Tags which identify the security groups you want to update
SECURITY_GROUP_TAG_FOR_SSH = { 'Application': 'Cloud9'}
TAG_FOR_EMAIL = { 'Contact': ''}
regions = ['eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-central-1', 'eu-north-1']

def lambda_handler(event, context):
    name='Application'
    value='Cloud9'
    result = main(name,value)
    return result

def main(name,value):
    for region in regions:
        ressource_client = boto3.client('ec2', region_name=region)
        filters = [{'Name': 'tag-key', 'Values': [name]},{ 'Name': "tag-value", 'Values': [value]}]
        response = ressource_client.describe_instances(Filters=filters)
        if response["Reservations"] == []:
            return json.dumps(response)
        else:
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    print(json.dumps(instance['Tags']['Contact']))
