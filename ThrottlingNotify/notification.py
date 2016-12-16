import logging

from Utils.slack_notifier import SlackNotifier
from Utils.email_notifier import EmailNotifier
import config


class Notification:
    def __init__(self, alert_level, organization_id, limit_name):
        self.logger = logging.getLogger(str(Notification))

        notify_level = config.NOTIFY_LEVELS.get(alert_level, dict())
        self.alert_title = notify_level.get('alert_title')
        self.alert_message = notify_level.get('alert_message_fmt').format(organization_id, limit_name)

    def notify_all(self):
        try:
            self.logger.info('Sending to slack...')
            self.to_slack()
        except:
            self.logger.warn('Unable to notify Slack')

        try:
            self.logger.info('Sending email...')
            self.to_email()
        except:
            self.logger.warn('Unable to notify Email')

    def to_slack(self):
        slack_notify = SlackNotifier(config.SLACK_NOTIFIER_BOT_NAME, config.SLACK_NOTIFIER_PROFILE_PICTURE)
        slack_notify.send_alert_to_channel(config.SLACK_NOTIFIER_CHANNEL, self.alert_title, self.alert_message)

    def to_email(self):
        email_notify = EmailNotifier(config.EMAIL_CONFIG_FILE)
        email_notify.send_email(config.EMAIL_OPS, self.alert_title, self.alert_message)

    def to_console(self):
        print '{}: {}'.format(self.alert_title, self.alert_message)
