import requests
import socket
from argparse import ArgumentParser
# dom = 'couponscorpion.com'
parser = ArgumentParser()
parser.add_argument("-d", "--domain",
                    help="the domain to check, Usage: .py -d google.com", default='couponscorpion.com', required=True)
parser.add_argument("-l", "--log",
                    help="show the log;is disabled by default, Usage: .py -l", default=False)
args = parser.parse_args()
sub = ['www', 'server', 'cpanel', 'webmail', 'mail', 'cdn', 'web']
ips = []
logs = dict()
for req in sub:
    # print (socket.gethostname())
    host = str(req+'.'+args.domain)
    try:
        ip = socket.gethostbyname(host)
        # print(ip)
        log = {host: ip}
        logs.update(log)
        ips.extend(str(ip))
        if ip not in ips:
            try:
                addr = str(socket.gethostbyaddr(ip)[0])
            except socket.error as e:
                addr = 'N/A'
            re = requests.get('https://api.hackertarget.com/aslookup/?q='+ip)
            req = str(re.content).split('","')
            asn = req[3]
            print(ip, host, addr, asn)
    except socket.error as e:
        # print('Invalid Subdomain: ', e)
        if args.log:
            log = {host: ip}
            logs.update(log)
            print('Log: ', logs)
