#!/usr/bin/env python3
import argparse
import os
import sys
import time
import dns.resolver
from dns.exception import DNSException

def resolve_domain(domain, record_types=None):
    if record_types is None:
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    results = {}
    resolver = dns.resolver.Resolver()
    
    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype, raise_on_no_answer=False)
            results[rtype] = [str(r) for r in answers]
        except dns.resolver.NXDOMAIN:
            results['ERROR'] = f"{domain} n'existe pas (NXDOMAIN)"
            return results
        except dns.resolver.NoAnswer:
            results[rtype] = []
        except DNSException as e:
            results[rtype] = [f"Erreur: {str(e)}"]
    
    return results

def main():
    domains_str = os.getenv("DOMAINS")
    if not domains_str:
        print("Erreur : variable d'environnement DOMAINS manquante")
        sys.exit(1)

    domains = [d.strip() for d in domains_str.split(",") if d.strip()]
    loop = int(os.getenv("LOOP_INTERVAL", "0"))

    print(f"Domaines à vérifier : {', '.join(domains)}")
    print(f"Intervalle : {loop}s (0 = one-shot)\n")

    while True:
        print(f"--- {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
        for domain in domains:
            print(f"\n>>> {domain}")
            results = resolve_domain(domain)
            if 'ERROR' in results:
                print(f"    {results['ERROR']}")
            else:
                for rtype, records in results.items():
                    if records:
                        print(f"    {rtype}:")
                        for rec in records:
                            print(f"        {rec}")
        print()

        if loop <= 0:
            break
        time.sleep(loop)

if __name__ == "__main__":
    main()
