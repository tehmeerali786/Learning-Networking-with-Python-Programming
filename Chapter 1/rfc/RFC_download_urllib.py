import sys, urllib.request 
from urllib.request import Request, urlopen

try:
    rfc_number = int(sys.argv[1])
    
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)
    
template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
req = Request(url = template.format(rfc_number),
              headers={'User-Agent': 'Mozilla/5.0'} )
rfc_raw = urlopen(req).read()
rfc = rfc_raw.decode()
print(rfc)