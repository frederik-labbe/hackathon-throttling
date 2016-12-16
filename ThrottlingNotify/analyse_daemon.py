import logging
from Utils.utils import get_epoch_now

from Data.throttling_event import ThrottlingEvent
from Data.throttling_abuse import ThrottlingAbuse
from notification import Notification
import config


class AnalyseDaemon:
    def __init__(self):
        self.logger = logging.getLogger(str(AnalyseDaemon))

    def run(self, new_events):
        self.logger.info('Start analysing')
        for organization_id, limit_name in new_events.iteritems():
            last_abuse_far_enough = not ThrottlingAbuse().last_abuse_since(minutes=config.TIME_TO_CHECK_MINUTES, organization_id=organization_id, limit_name=limit_name)
            if last_abuse_far_enough:
                self.logger.info('Last abuse is far enough for org {} limit {}'.format(organization_id, limit_name))
                event_count_since = ThrottlingEvent().get_event_count_since(minutes=config.TIME_TO_CHECK_MINUTES, organization_id=organization_id, limit_name=limit_name)
                self.logger.info('Has {} similar events'.format(event_count_since))

                # get level with highest event_count busted
                level_triggered = None
                for level in config.NOTIFY_LEVELS:
                    if event_count_since >= config.NOTIFY_LEVELS.get(level).get('event_count_to_trigger', 999):
                        level_triggered = level
                    else:
                        break

                if level_triggered:
                    alert = config.NOTIFY_LEVELS.get(level_triggered)
                    self.logger.info('{} detected for org {}, limit {}. Notifications sent.'.format(alert.get('alert_title'), organization_id, limit_name))
                    notification = Notification(level_triggered, organization_id, limit_name)
                    notification.notify_all()

                    ThrottlingAbuse(organization_id, limit_name).update(get_epoch_now())
        self.logger.info('Finished analysing')
