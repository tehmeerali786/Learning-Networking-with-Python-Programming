import requests 

cookies = []

url = 'http://httpbin.org/cookies'

cookies = dict(admin='True')
cookies_req = requests.get(url, cookies=cookies)
print(cookies_req.text)

