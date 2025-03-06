import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# This session object saves our config so we don't need to set it every time.
s = requests.session()
# Skip trying to verify TLS certs, due to Burp's CA.
s.verify = False
# Proxy requests through Burp.
s.proxies = {"https": "http://127.0.0.1:8080"}
# Send a GET request to whoami.
r = s.get("https://whoami.quoccacorp.com")
# Will print: b"Hi z6666666! Here's a flag: COMP6443{hi_im_z6666666_hwOk6dGApTnDudlmsKl-}"
print(r.content)
