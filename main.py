from ThrottlingNotify.fetch_daemon import FetchDaemon
from ThrottlingNotify.config import FETCH_FREQUENCY_MS
from ThrottlingNotify.config import THROTTLING_BUCKET_NAME

daemon = FetchDaemon(THROTTLING_BUCKET_NAME, FETCH_FREQUENCY_MS)
daemon.start()
