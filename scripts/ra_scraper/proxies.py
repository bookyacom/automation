#!usr/bin/pyhton3

import pandas as pd
import requests
import time
import sys

# The script gets random open proxies and save them into a file

# The downloaded proxies are later used by the scraper to mask its own ip
# in order not get blocked by the server

proxy_file = "proxy_list.csv"

data = list()
for x in range(10):
    time.sleep(5)
    r = requests.get("https://api.getproxylist.com/proxy").json()
    try:
        data.append("http://%s:%s" % (r["ip"], r["port"]))
    except KeyError:
        # 24 calls per day allowed, when exceeded return error msg
        print(r["error"])
        sys.exit(1)

df = pd.DataFrame(data, columns=['ip'])
df['tm_downloaded'] = time.time()
df['tm_last_used'] = 0
df['times_failed'] = 0

with open(proxy_file, "a+") as f:
    df.to_csv(f, header=False, index=False, sep=";")
