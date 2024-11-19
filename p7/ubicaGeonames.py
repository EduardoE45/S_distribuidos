import requests

def obtener_informacion_ubicacion(geonames_lalo45, México):
    url = f"http://api.geonames.org/searchJSON?name={México}&maxRows=1&username={geonames_lalo}"

    try:
        response = requests.get(url)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            print(f"Nombre: {ubicacion['name']}")
            print(f"País: {ubicacion['countryName']}")
            print(f"Población: {ubicacion['population']}")
        else:
            print("Ubicación no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    #Coloca tu usuario de geonames
    geonames_username = "lalo45"

    lugar = "México"  # Cambia esto a la ubicación que desees consultar
    obtener_informacion_ubicacion(geonames_lalo45, México)
