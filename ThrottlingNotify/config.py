THROTTLING_EVENTS_BUCKET_NAME = 'hackathon-throttling-events'
THROTTLING_EVENTS_FOLDER_NAME = 'organizations'
DAEMONS_RUN_FREQUENCY_S = 5

NOTIFY_LEVELS = {
    1: {
        'alert_title': 'Alert level 1',
        'alert_message_fmt': 'Organization {} is a dick'
    },
    2: {
        'alert_title': 'Alert level 2',
        'alert_message_fmt': 'Organization {} is a super dick'
    },
    3: {
        'alert_title': 'Alert level 3',
        'alert_message_fmt': 'Organization {} is not worth it'
    }
}