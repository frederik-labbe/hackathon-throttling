from datetime import datetime


def get_epoch_now():
    return int(datetime.now().strftime('%s'))