import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter URL: ')
#sample code URL below
url = 'http://py4e-data.dr-chuck.net/known_by_Luella.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
count = 0
print("URL entered already...")

while True:
    pos = int(input("Enter position: "))
    print("Name:", tags[pos-1].text)
    sub_link = tags[pos-1]
    link = sub_link.get('href')
    print("Link:", link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count += 1
    print("Count:", count)
