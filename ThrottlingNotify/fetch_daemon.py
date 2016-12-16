import logging

from Utils.bucket import S3Bucket


class FetchDaemon:
    def __init__(self, bucket_name, folder_name):
        self.bucket_name = bucket_name
        self.folder_name = folder_name
        self.logger = logging.getLogger(str(FetchDaemon))

    def run(self):
        self.logger.info('Start fetching')
        throttling_bucket = S3Bucket(self.bucket_name)
        new_events = throttling_bucket.consume(prefix='organizations')
        self.logger.info('Finished fetching')
        return new_events
