import time

from Utils.bucket import S3Bucket


class FetchDaemon:
    def __init__(self, bucket_name, delay_ms):
        self.bucket_name = bucket_name
        self.delay_ms = delay_ms

    def start(self):
        throttling_bucket = S3Bucket(self.bucket_name)
        while True:
            throttling_data_objects = throttling_bucket.consume(prefix='organizations')
            for throttling_data in throttling_data_objects:
                _analyse_throttling(throttling_data)
            time.sleep(self.delay_ms)


def _analyse_throttling(throttling_data):
    # TODO: analyse data and choose if and what notification
    throttling_data
    print 'Analysed bucket: Notify level is Something, notify someone'