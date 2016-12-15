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
        content = self.get_oject(key_name='', file_name='clementineparrot.gif')
        print 'Consuming {}'.format(self.bucket_name)

    def get_oject(self, key_name, file_name):
        s3_key = Key(self.bucket)
        s3_key.key = key_name
        return s3_key.get_contents_to_file(file_name)

    def delete_object(self, file_name):
        pass
