THROTTLING_EVENTS_BUCKET_NAME = 'hackathon-throttling-events'
THROTTLING_EVENTS_FOLDER_NAME = 'organizations'
DAEMONS_RUN_FREQUENCY_S = 1

TIME_TO_CHECK_MINUTES = 5

NOTIFY_LEVELS = {
    0: {
        'alert_title': 'Warning',
        'alert_message_fmt': 'Organization {} is a dick for busting limit {}',
        'event_count_to_trigger': 3
    },
    1: {
        'alert_title': 'Abuse level 1',
        'alert_message_fmt': 'Organization {} is a super dick for busting limit {}',
        'event_count_to_trigger': 4
    },
    2: {
        'alert_title': 'Abuse level 2',
        'alert_message_fmt': 'Organization {} is not worth it for busting limit {}',
        'event_count_to_trigger': 5
    }
}

SLACK_NOTIFIER_BOT_NAME = 'Cloud Throttling'
SLACK_NOTIFIER_PROFILE_PICTURE = ':lightning:'
SLACK_NOTIFIER_CHANNEL = 'throttling-alerts'

EMAIL_CONFIG_FILE = 'config.cfg'
EMAIL_OPS = 'emilefugulin@hotmail.com'
