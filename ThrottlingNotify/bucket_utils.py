import os

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

    def consume(self):
        # TODO: get all files
        content = self.get_oject(key_name='organizations', file_name='1481831315169.json')
        # TODO: get files in bucket and parse data
        throttling_data_objects = list()
        return throttling_data_objects

    def get_oject(self, folder_name, file_name):
        s3_key = Key(self.bucket)
        s3_key.key = '{}/{}'.format(folder_name, file_name)
        return s3_key.get_contents_as_string()

    def delete_object(self, file_name):
        pass
