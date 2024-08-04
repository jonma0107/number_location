# from dotenv import load_dotenv
# import os

# import phonenumbers
# import folium
# from phonenumbers import geocoder

# from MyNumber import number

# # Cargar las variables de entorno desde el archivo .env
# load_dotenv()

# Key = os.getenv('opencagedataAPIKEY')

# samNumber = phonenumbers.parse(number)

# yourLocation = geocoder.description_for_number(samNumber, "en")

# print(f"Your phone number is located in: {yourLocation}")

# ## get service provider

# from phonenumbers import carrier

# # service_provider2 = carrier.name_for_number(samNumber, "en")
# # print(service_provider2)

# service_provider = phonenumbers.parse(number)
# print(carrier.name_for_number(service_provider, "en"))

# # get area code

# from opencage.geocoder import OpenCageGeocode

# geocoder = OpenCageGeocode(Key)

# query = str(yourLocation)

# results = geocoder.geocode(query)
# ## print(results)

# lat = results[0]['geometry']['lat']

# lng = results[0]['geometry']['lng']

# print(f"Latitude: {lat}, Longitude: {lng}")


# # Map Location

# myMap = folium.Map(location=[lat, lng], zoom_start=9)

# folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# # save map in html file

# myMap.save("myLocation.html")

# ***********************************************************************

# GOOGLE MAPS

from dotenv import load_dotenv
import os

import phonenumbers
import folium
import googlemaps
from phonenumbers import geocoder, carrier
from MyNumber import numbersList

# Asegúrate de que 'number' contiene el número de teléfono a analizar
number = numbersList

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

Key = os.getenv('googlecloudAPIKEY')

# Inicializar el cliente de Google Maps
gmaps = googlemaps.Client(key=Key)

# Iterar sobre la lista de números de teléfono
for number in numbersList:
    try:
        # Parsear el número de teléfono
        samNumber = phonenumbers.parse(number)
        yourLocation = geocoder.description_for_number(samNumber, "en")

        print(f"Your phone number {number} is located in: {yourLocation}")

        # Obtener el proveedor de servicios
        service_provider = carrier.name_for_number(samNumber, "en")
        print(f"Service provider for {number}: {service_provider}")

        # Geocodificar la ubicación
        geocode_result = gmaps.geocode(yourLocation)

        if geocode_result and len(geocode_result) > 0:
            location = geocode_result[0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            print(f"Latitude: {lat}, Longitude: {lng}")

            # Mapear la ubicación
            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

            # Guardar el mapa en un archivo HTML
            map_filename = f"myLocation_{number}.html"
            myMap.save(map_filename)
            print(f"Map saved to {map_filename}")
        else:
            print(f"No se pudo encontrar la ubicación para el número {number}.")
    except Exception as e:
        print(f"An error occurred while processing the number {number}: {e}")
    

    
