'''
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.'
'''
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
print("Location entered...")
#address = input("Enter a location: ")
address = 'Institut Superieur de technologies'
print("Retrieving", serviceurl + address)
url = serviceurl + urllib.parse.urlencode(
    {'address': address})

url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
js = json.loads(data)

print("Retrieved " + str(len(data)) + " characters...")

print("Place_ID:", js["results"][0]["place_id"])
