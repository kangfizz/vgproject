import os
from datetime import datetime, timedelta
os.environ.update({"DJANGO_SETTINGS_MODULE": "vgsite.settings"})

import django
django.setup()

import requests

from api.views import Api


NOW = datetime.now() + timedelta(hours=8)
print(NOW)
print("===== vg todays card catch =====")
if datetime.strftime(NOW, "%H:%M") == "09:31":
    Api("VG").get_vg_today_card()
print("===== ws todays card catch =====")
if datetime.strftime(NOW, "%H:%M") == "09:32":
    Api("WS").get_ws_today_card()
