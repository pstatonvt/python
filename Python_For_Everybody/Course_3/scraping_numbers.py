from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

array = []
counter = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_72206.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
<<<<<<< HEAD
print(soup)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
=======

# Retrieve all of the anchor numberss
span = soup('span')

#isolating the numbers in the column, appending them to a list, and summing them
for x in span:
    counter += 1
    x.contents[0] = int(x.contents[0])
    array.append(x.contents[0])

print("Count", counter)
print("Sum", sum(array))
>>>>>>> db292f38c555d17d485cc4e18808fe82922e5b40
