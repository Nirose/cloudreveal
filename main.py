import socket
from argparse import ArgumentParser
import http.client

# Add arguments for options
parser = ArgumentParser()
parser.add_argument("-d", "--domain",
                    help="the domain to check, Usage: .py -d google.com", default='couponscorpion.com', required=True)
parser.add_argument("-l", "--log",
                    help="show the log;is disabled by default, Usage: .py -l", default=False, action='store_true')
args = parser.parse_args()

# Subdomains for checking direct connection to the server bypassing the cloudflare
subs = ['www', 'server', 'cpanel', 'webmail',
        'mail', 'cdn', 'web', 'ftp', 'direct', 'ezmail', 'webdisk', 'amp']

# Store the found IPs
ips = []
# Logs to check every subdomain checked for IP and information
logs = dict()

# Get ASN data from hackertarget API


def getASN(ip):
    conn = http.client.HTTPSConnection("api.hackertarget.com")
    conn.request("GET", "/aslookup/?q="+ip)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


for sub in subs:
    # print (socket.gethostname())
    ip = False
    subd = str(sub+'.'+args.domain)
    try:
        ip = socket.gethostbyname(subd)
        # print(ip)
        log = {subd: ip}
        logs.update(log)
        if ip not in ips:
            ips.append(str(ip))
            try:
                addr = str(socket.gethostbyaddr(ip)[0])
            except socket.error as e:
                addr = 'N/A'
            dtext = getASN(ip)
            req = dtext.split('","')
            asn = '"'+req[3]
            print(ip, subd, addr, asn)
    except socket.error as e:
        # print('Invalid Subdomain: ', e)
        if ip:
            log = {subd: ip}
            logs.update(log)
        else:
            log = {subd: 'N/A'}
            logs.update(log)
if args.log:
    print('Log: ', logs)
    print(ips)
