# support0.py - H09A, wk 2

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s = requests.Session()
s.proxies = {"https": "127.0.0.1:8080"}
s.verify = False

flags = {}

for i in range(248):
    # e.g. https://support-v0.quoccacorp.com/raw/6/
    response = s.get(f"https://support-v0.quoccacorp.com/raw/{i}/")
    print(response.text)

    # todo: add regex for easier flag search (see haas1.py)
    if "COMP6443{" in response.text:
        flags[i] = response.text

print(flags)

# print(response.content)
# print(response.headers)
# print()
