# view an RFC doc commandline with python3 'python3 rfc.py 4096'
import urllib3
import sys

if len(sys.argv) != 2:
    print("Enter a valid rfc")
    sys.exit()

rfc_number = int(sys.argv[1])
template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
http = urllib3.PoolManager()
# need to set this within the office networks
#http = urllib3.proxy_from_url('http://www-proxy.us.oracle.com:80/')
response = http.request('GET', url)  # HTTP response object
if response.status == 200:
    print(response.data.decode('utf-8'))
else:
    print("RFC number", rfc_number, "not found")

