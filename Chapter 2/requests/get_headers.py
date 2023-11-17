import requests 

response = requests.get('https://www.github.com')

try:
    for key, value in response.headers.items():
        print("%s, %s" % (key, value))
        print("\n")
        print("\n")
        
except Exception as error:
    print('%s' % (error))