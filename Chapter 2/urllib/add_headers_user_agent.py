from urllib.request import Request 

USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0'
URL = 'https://www.debian.org/'

def add_headers_user_agent():
    
    headers = {'Accept-Language' : 'nl', 'User-agent': USER_AGENT}
    request = Request(URL, headers=headers)
    
    # request.add_headers('Accept-Language', 'nl')
    # request.add_headers('User-agent': USER_AGENT)
    
    print('Request Headers: ')
    for key, value in request.header_items():
        print("%s : %s" %(key, value))
        
        
if __name__ == '__main__':
    add_headers_user_agent()