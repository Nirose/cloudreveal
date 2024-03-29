# Reveal IP behind CDN servers by checking well-known subdomains
Check and Prevent against origin IP being revealed through subdomain enumeration.

## Usage
* Store the subdomains in `list.txt`
* Run the command (without any suddomains, not even `www`)

    `python3 main.py -d domain.com`

## Resultsmain
The results depend on your understanding of what you are looking for

`104.31.91.30 www.domain.com N/A "CLOUDFLARENET - Cloudflare, Inc., US"`

`1**.2**.9*.5* webmail.domain.com somehostname.com "Some Hosting Company"`

### Classification
|IP|subdomain|hostname|Server ASN|
|--|:-------:|:------:|----------:|
|104.31.91.30|www.domain.com|N/A|"CLOUDFLARENET - Cloudflare, Inc., US"|
|1**.2**.9*.5*|webmail.domain.com|somehostname.com|"HOSTNET - Some Hosting Solutions, US"|

## WIP
* Detect subdomains with virustotal API for subdomain information
