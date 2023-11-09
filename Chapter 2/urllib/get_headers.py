import urllib.request

url = input('https://www.kravious.com/')

http_response = urllib.request.urlopen(url)

if http_response.code == 200:
    print(http_response.headers())
    for key, value in http_response.getheaders():
        print(key, value)