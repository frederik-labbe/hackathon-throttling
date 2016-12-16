import time
import logging
import sys

from ThrottlingNotify.fetch_daemon import FetchDaemon
from ThrottlingNotify.analyse_daemon import AnalyseDaemon
from ThrottlingNotify.config import DAEMONS_RUN_FREQUENCY_S
from ThrottlingNotify.config import THROTTLING_EVENTS_BUCKET_NAME
from ThrottlingNotify.config import THROTTLING_EVENTS_FOLDER_NAME

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(name)-50s %(levelname)-8s %(message)s')

fetch_daemon = FetchDaemon(THROTTLING_EVENTS_BUCKET_NAME, THROTTLING_EVENTS_FOLDER_NAME)
analyse_daemon = AnalyseDaemon()

while True:
    new_events = fetch_daemon.run()
    if new_events:
        analyse_daemon.run()
    time.sleep(DAEMONS_RUN_FREQUENCY_S)
