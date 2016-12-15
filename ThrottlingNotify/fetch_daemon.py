import time

from bucket_utils import S3Bucket


class FetchDaemon:
    def __init__(self, bucket_name, delay_ms):
        self.bucket_name = bucket_name
        self.delay_ms = delay_ms

    def start(self):
        throttling_bucket = S3Bucket(self.bucket_name)
        while True:
            throttling_bucket.consume()
            time.sleep(self.delay_ms)


def _analyse_bucket(bucket):
    bucket
    print 'Analysed bucket: Notify level is Something, notify someone'