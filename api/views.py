import os
import urllib.request

import requests
from bs4 import BeautifulSoup
from django.conf import settings


class Api:
    """各式api"""

    def __init__(self, _type):
        if _type == 'WS':
            self.url = "https://ws-tcg.com"

    def get_ws_today_card(self):
        """取得每日一卡(WS)"""
        html = requests.get(f"{self.url}/ws_today_p/")
        soup = BeautifulSoup(html.text, 'html.parser')
        _list = soup.findAll('img', 'aligncenter')
        url_list = [f"{self.url}{x.get('src')}" for x in _list]
        route = os.path.join(settings.BASE_DIR, 'static/upload/todays_card.png')

        return urllib.request.urlretrieve(url_list[0], route)
