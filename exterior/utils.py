import requests
from credittrack.settings import api_currency

def obtener_tipo_cambio(tipo1, tipo2, valor):
    base_url = f"https://api.currencyapi.com/v3/latest?apikey={api_currency}&base_currency={tipo2}"
    response = requests.get(base_url)
    data = response.json()
    clp_amount = 1000
    usd_value = data["data"]["USD"]["value"]
    eur_value = data["data"]["EUR"]["value"]
    jpy_value = data["data"]["JPY"]["value"]

    usd_amount = clp_amount * usd_value
    eur_amount = clp_amount * eur_value
    jpy_amount = clp_amount * jpy_value
    return usd_amount, eur_amount, jpy_amount