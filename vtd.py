import http.client
import json
from argparse import ArgumentParser


class virustotal:
    def __init__(self):
        # initialize arguments
        parser = ArgumentParser()
        parser.add_argument("-d", "--domain",
                            help="the domain to check, Usage: .py -d google.com", default='couponscorpion.com', required=True)
        self.args = parser.parse_args()

    def subs(self):
        domain = self.args.domain
        conn = http.client.HTTPSConnection("www.virustotal.com")
        conn.request("GET", "/ui/domains/"+domain +
                     "/subdomains?limit=40")  # max limit is 40

        res = conn.getresponse()
        data = res.read()

        jd = json.loads(data.decode("utf-8"))
        subd = jd['data']
        # print(devices)
        for d in subd:
            print(d['id'])


if __name__ == "__main__":
    check = virustotal()
    check.subs()
