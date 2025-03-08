import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# This is what HaaS will send kb. We'll send it to HaaS in the HTTP POST body
# It's just the form's default value (either copy/paste or decode it from the request body via Burp)
kb_req = """GET / HTTP/1.1
Host: kb.quoccacorp.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://haas.quoccacorp.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: http://haas.quoccacorp.com
Connection: keep-alive

"""

# Send a POST request to HaaS, whose requestBox parameter contains the get request to send to kb
# (requestBox can be seen in the HTML form (inspect element) and/or the POST body param in Burp)
response = requests.post(
    "https://haas-v1.quoccacorp.com/",
    proxies={"https": "http://127.0.0.1:8080"},  # Proxy requests through Burp.
    verify=False,  # Skip trying to verify TLS certs, due to Burp's CA.
    data={
        "requestBox": kb_req
    },  # POST data / request body - the request for HaaS to send to kb
)

# Print the response body - no headers from HaaS, just the text that'd get displayed in your browser
# This is the value of the response kb sent to HaaS, which HaaS then forwarded to us
print(response.text)
