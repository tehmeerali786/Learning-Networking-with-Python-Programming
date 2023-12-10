import requests 
response = requests.post('http://httpbin.org/post', json={"key":"value"})
print(response.status_code)
print(response.json())