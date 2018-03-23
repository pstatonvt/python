import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_72208.xml'
print("Retrieving", url)
html = urllib.request.urlopen(url).read()
print("Retrieved", len(html), "characters")

tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
count_lst = []
count = 0

for item in lst:
    #print("Name:", item.find('name').text)
    #print("Count:", item.find('count').text)
    num = item.find('count').text
    num = int(num)
    count_lst.append(num)
    count += 1

print("Count:", count)
print("Sum:", sum(count_lst))


#for number in count_lst:
#    number = int(number)

#print("Sum:", sum(count_lst))
