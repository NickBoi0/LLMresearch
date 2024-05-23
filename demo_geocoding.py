import os
from dotenv import load_dotenv
import googlemaps

load_dotenv()
# api_key = os.getenv('maps_api_key')
maps = googlemaps.Client(key='KEY HERE')

address = 'Penn State, PA'

response_geocode = maps.geocode(address)
print(response_geocode)