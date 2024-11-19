import requests
def obtener_informacion_ubicacion(geonames_lalo45, México):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_lalo45}"
