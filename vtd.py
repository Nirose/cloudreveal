import http.client
import json
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-d", "--domain",
                    help="the domain to check, Usage: .py -d google.com", default='couponscorpion.com', required=True)
args = parser.parse_args()
conn = http.client.HTTPSConnection("www.virustotal.com")

conn.request("GET", "/ui/domains/"+args.domain+"/subdomains?limit=40")

res = conn.getresponse()
data = res.read()

jd = json.loads(data.decode("utf-8"))
subd = jd['data']
# print(devices)
for d in subd:
    print(d['id'])
