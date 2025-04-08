import os
from os import getenv
import requests
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY')
async def currency_exchange(_from, _to):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{_from}/{_to}"
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()
        return data["conversion_rate"]

    return None