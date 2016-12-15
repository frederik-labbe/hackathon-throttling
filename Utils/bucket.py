import os

import json

from throttling_event import ThrottlingEvent

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key


class S3Bucket:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.connection = S3Connection(calling_format=boto.s3.connection.OrdinaryCallingFormat(),
                                       aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                       aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
        self.bucket = self.connection.get_bucket(self.bucket_name)

    def consume(self, prefix):
        throttling_data_objects = list()
        for key in self.bucket.list(prefix=prefix):
            content = self.get_oject(key=key)
            event = ThrottlingEvent(organization_id=content['organizationId'],
                                    timestamp=content['timestamp']['epochSecond'],
                                    limit_name=content['limitDefinition']['name'],
                                    limit_capacity=content['limitDefinition']['capacity'],
                                    limit_duration=content['limitDefinition']['expiration']['seconds'],
                                    percentage_used=content['percentageCapacityUsed'],
                                    is_reported=False)
            throttling_data_objects.append(content)
        return throttling_data_objects

    def get_oject(self, key):
        s3_key = Key(self.bucket, key)
        content = s3_key.get_contents_as_string()
        return json.loads(content)

    def delete_object(self, file_name):
        pass
