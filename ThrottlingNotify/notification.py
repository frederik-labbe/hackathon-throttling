from Utils.slack import SlackNotifier
import config


class Notification:
    def __init__(self, alert_level, organization_id, limit_name):
        notify_level = config.NOTIFY_LEVELS.get(alert_level, dict())
        self.alert_title = notify_level.get('alert_title')
        self.alert_message = notify_level.get('alert_message_fmt').format(organization_id, limit_name)

    def to_slack(self):
        slack_notify = SlackNotifier(config.SLACK_NOTIFIER_BOT_NAME, config.SLACK_NOTIFIER_PROFILE_PICTURE)
        slack_notify.send_alert_to_channel(config.SLACK_NOTIFIER_CHANNEL, self.alert_title, self.alert_message)

    def to_console(self):
        print '{}: {}'.format(self.alert_title, self.alert_message)
