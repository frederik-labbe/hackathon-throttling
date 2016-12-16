import os

from slackclient import SlackClient


class SlackNotifier:
    def __init__(self, user_name, profile_image):
        self.client = SlackClient(os.environ.get('SLACK_TOKEN'))
        self.user_name = user_name
        self.profile_image = profile_image

    def send_to_channel(self, channel_name, message):
        return self.client.api_call("chat.postMessage", channel=channel_name, text=message, username=self.user_name, icon_emoji=self.profile_image)

    def send_alert_to_channel(self, channel_name, alert_title, message):
        return self.send_to_channel(channel_name=channel_name, message='{}: {}'.format(alert_title, message))