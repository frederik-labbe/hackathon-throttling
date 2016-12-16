import time
import logging
import sys

from ThrottlingNotify.fetch_daemon import FetchDaemon
from ThrottlingNotify.analyse_daemon import AnalyseDaemon
from ThrottlingNotify.config import DAEMONS_RUN_FREQUENCY_S
from ThrottlingNotify.config import THROTTLING_EVENTS_BUCKET_NAME
from ThrottlingNotify.config import THROTTLING_EVENTS_FOLDER_NAME

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(name)-50s %(levelname)-8s %(message)s')

fetch_daemon = FetchDaemon(bucket_name=THROTTLING_EVENTS_BUCKET_NAME, folder_name=THROTTLING_EVENTS_FOLDER_NAME)
analyse_daemon = AnalyseDaemon()

while True:
    new_events = fetch_daemon.run()
    analyse_daemon.run(new_events)
    time.sleep(DAEMONS_RUN_FREQUENCY_S)
