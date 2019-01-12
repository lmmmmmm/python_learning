import urllib.request as req

response = req.urlopen('https://www.pyhon.org')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(response.read().decode('UTF-8'))
