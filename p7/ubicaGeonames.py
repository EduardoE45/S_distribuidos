import requests

def obtener_informacion_ubicacion(geonames_username, lugar):
    """
    Consulta información de una ubicación utilizando la API de GeoNames.
    
    Parámetros:
        geonames_username (str): Nombre de usuario de GeoNames.
        lugar (str): Nombre del lugar a consultar.
    """
    # Construcción del URL de la solicitud
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"
    
    try:
        # Realiza la solicitud GET
        response = requests.get(url)
        
        # Verifica el código de estado HTTP
        if response.status_code == 200:
            data = response.json()
            
            # Verifica si hay datos en la respuesta
            if "geonames" in data and data["geonames"]:
                ubicacion = data["geonames"][0]
                
                # Imprime la información obtenida
                print(f"Nombre: {ubicacion.get('name', 'Desconocido')}")
                print(f"País: {ubicacion.get('countryName', 'Desconocido')}")
                print(f"Población: {ubicacion.get('population', 'No disponible')}")
                print(f"Latitud: {ubicacion.get('lat', 'No disponible')}")
                print(f"Longitud: {ubicacion.get('lng', 'No disponible')}")
            else:
                print("No se encontraron resultados para la ubicación especificada.")
        else:
            print(f"Error HTTP: {response.status_code}. No se pudo conectar con la API.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    # Coloca tu usuario de GeoNames
    geonames_username = "migfel"  # Reemplaza con tu verdadero usuario
    
    # Nombre del lugar a consultar
    lugar = "México"  # Cambia esto según lo que quieras consultar
    
    # Llama a la función para obtener la información
    obtener_informacion_ubicacion(geonames_username, lugar)
