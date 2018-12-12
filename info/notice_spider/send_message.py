import os, json
from django.core.exceptions import ImproperlyConfigured
import fbchat
from fbchat import Client


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, './secrets.json')  # secrets.json 파일 위치를 명시
with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def send_message(message, receiver_uid):
    FB_ID = get_secret("FB_ID")
    FB_PW = get_secret("FB_PW")
    client = Client(FB_ID, FB_PW, max_tries=2)
    client.send(fbchat.models.Message(message), receiver_uid)
