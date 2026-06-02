import requests


def consumir_servicios():
    url = "http://localhost:8080/migaja/v1/gasto"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos
