import http.cookiejar
import urllib

URL = 'https://github.com/'

def extract_cookie_info():
    # set up the cookiejar
    cookie_j = http.cookiejar.CookieJar()
    
    # create url opener 
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_j))
    
    # now access without any login info 
    resp = opener.open(URL)
    for cookie in cookie_j:
        print("Cookie: %s --> %s" %(cookie.name, cookie.value))
        
    print("Headers: %s" %resp.headers)
    
if __name__ == "__main__":
    extract_cookie_info()
        