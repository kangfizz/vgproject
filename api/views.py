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
        elif _type == 'VG':
            self.url = "https://cf-vanguard.com"

    @staticmethod
    def saveimage(find_list, _route, front_route=""):
        """儲存Image to 本地"""
        url_list = [f"{front_route}{x.get('src')}" for x in find_list]
        route = os.path.join(settings.BASE_DIR, _route)

        return urllib.request.urlretrieve(url_list[0], route)

    def get_ws_today_card(self):
        """取得每日一卡(WS)"""
        html = requests.get(f"{self.url}/ws_today_p/")
        soup = BeautifulSoup(html.text, 'html.parser')
        _list = soup.findAll('img', 'aligncenter')

        return self.saveimage(_list, 'static/upload/todays_card_ws.png', self.url)

    def get_vg_today_card(self):
        """取得每日一卡(VG)"""
        html = requests.get(f"{self.url}/todays-card/")
        soup = BeautifulSoup(html.text, 'html.parser')
        _list = soup.findAll('img', alt='【カードファイト!! ヴァンガード】今日のカード')

        return self.saveimage(_list, 'static/upload/todays_card_vg.png')
