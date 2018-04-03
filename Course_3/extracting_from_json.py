'''
Read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
'''

import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_72209.json'
print("Location entered...")
print("Retrieving", url)
url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
info = json.loads(data)
print("Retrieved " + str(len(data)) + " characters")
nums = []
#print(len(info["comments"]))

for i in range(0, len(info["comments"])):
    #print("Name:", info["comments"][i]["name"])
    #print("Count:", info["comments"][i]["count"])
    nums.append(info["comments"][i]["count"])

print("Sum:", sum(nums))
