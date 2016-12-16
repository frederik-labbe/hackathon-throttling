import logging
from Utils.utils import get_epoch_now

from Data.throttling_event import ThrottlingEvent
from Data.throttling_abuse import ThrottlingAbuse


class AnalyseDaemon:
    def __init__(self):
        self.logger = logging.getLogger(str(AnalyseDaemon))

    def run(self):
        organization_id = 'test1'
        limit_name = 'quota'

        self.logger.info('Start analysing')
        if not ThrottlingAbuse().last_abuse_since(minutes=1000, organization_id=organization_id, limit_name=limit_name) \
           and ThrottlingEvent().get_event_count_since(minutes=1000, organization_id=organization_id, limit_name=limit_name) > 3:
            self.logger.info('Busted!')
            ThrottlingAbuse(organization_id, limit_name).update(get_epoch_now())
        self.logger.info('Finished analysing')
