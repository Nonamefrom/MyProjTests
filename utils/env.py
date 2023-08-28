import os
from dotenv import load_dotenv

load_dotenv()

class Env(): # pylint: disable=too-few-public-methods
    def __init__(self):
        self.remote_webdriver_url = os.getenv('REMOTE_WEBDRIVER_URL')
        self.cp_url = os.getenv('CP_URL')
