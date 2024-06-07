import requests
from django.conf import settings

def get_usd_clp_exchange_rate(start_date=None, end_date=None):
    series_id = "F073.TCO.PRE.Z.D"  # ID de la serie del tipo de cambio
    url = settings.BANCENTRAL_SERIES_URL
    params = {
        "user": settings.BANCENTRAL_API_USER,
        "pass": settings.BANCENTRAL_API_PASSWORD,
        "function": "GetSeries",
        "timeseries": series_id,
    }
    if start_date:
        params["firstdate"] = start_date
    if end_date:
        params["lastdate"] = end_date

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["Codigo"] == 0:  # Verificar que la respuesta fue exitosa
            # Extraer el último valor disponible del tipo de cambio
            exchange_rate = data["Series"]["Obs"][-1]["value"]
            return float(exchange_rate)
        else:
            raise Exception(f"Error en la respuesta del API: {data['Descripcion']}")
    else:
        raise Exception(f"Error al obtener el tipo de cambio: {response.status_code}")
