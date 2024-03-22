import os
from dotenv import load_dotenv

load_dotenv()


class Env:
    def __init__(self):
        self.remote_webdriver_url = os.getenv('REMOTE_WEBDRIVER_URL')
        self.cp_url = os.getenv('CP_URL')
        self.sb_url = os.getenv('SB_URL')
        self.pwz_url = os.getenv('PWZ_URL')
        self.emp_dash_url = os.getenv('EMP_DASH_URL')
        self.mailpit = os.getenv('MAILPIT')
        self.partner_url = os.getenv('PARTNER_CABINET_URL')
        self.mim_url = os.getenv('MIM_URL')
