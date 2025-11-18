import sys
import dns.resolver
import dns.name
from urllib.parse import urlparse



DNS_RECORDS = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA']

def main():

    if len(sys.argv)!= 2:
        raise ValueError('Incorrect number of arguments was given.')


    json = {}

    url = sys.argv[1]
    domain_name = urlparse(url).netloc

    json['url'] = url
    json['domain_name'] = domain_name
    json['dns'] = {}
    json['ip_data'] = {}
    json['rdap'] = {}
    json['tls'] = {}

    if not json['domain_name']:
        raise ValueError('Incorrect URL value was given.')



    """ DNS DATA """

    resolver = dns.resolver.Resolver()
    for record in DNS_RECORDS:
        
        record_info = {}

        match record:
            case 'A':
                pass
            case 'AAAA':
                pass
            case 'CNAME':
                pass
            case 'MX':
                pass
            case 'NS':
                pass
            case 'TXT':
                pass
            case 'SOA':
                pass

        json['dns'][record] = record_info

if __name__ == "__main__":
    main()
