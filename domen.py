import argparse
import sublist3r
import sys

idk = f"""
             \033[92m██╗░░░██╗░█████╗░██████╗░░██████╗░██╗
             ╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝░██║
             ░╚████╔╝░███████║██████╔╝██║░░██╗░██║
             ░░╚██╔╝░░██╔══██║██╔══██╗██║░░╚██╗██║
             ░░░██║░░░██║░░██║██║░░██║╚██████╔╝██║
             ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝
             \033[31m                                         TT:yargi.py\033[0m
"""
print(idk)

def main1():
    parser = argparse.ArgumentParser(
        description='Subdomain Enumeration Tool',
        epilog='Examples:\n'
               '  python domen.py -d example.com\n'
               '  python domen.py -d example.com -p 80,443 -s\n'
               '  python domen.py -d example.com -b -e google,bing'
    )
    parser.add_argument('-d', '--domain', help='Target domain', required=True)
    parser.add_argument('-p', '--ports', help='Comma-separated list of ports to scan (default: None)', default=None)
    parser.add_argument('-s', '--silent', help='Enable silent mode (no output)', action='store_true')
    parser.add_argument('-v', '--verbose', help='Enable verbose mode (detailed output)', action='store_true')
    parser.add_argument('-b', '--bruteforce', help='Enable brute force enumeration', action='store_true')
    parser.add_argument('-e', '--engines', help='Comma-separated list of engines to use (default: None)', default=None)
    parser.add_argument('-t', '--threads', help='Number of threads (default: 10)', type=int, default=10)
    parser.add_argument('-f', '--savefile', help='File to save results (default: subdomains.txt)', default='subdomains.txt')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()

def main2():
    args = main1()

    domain = args.domain
    ports = args.ports
    silent = args.silent
    verbose = args.verbose
    enable_bruteforce = args.bruteforce
    engines = args.engines
    threads = args.threads
    savefile = args.savefile

    if engines:
        engines = engines.split(',')

    if ports:
        ports = [int(port) for port in ports.split(',')]

    subdomains = sublist3r.main(domain, ports=ports, silent=silent, verbose=verbose,
                                 enable_bruteforce=enable_bruteforce, engines=engines,
                                 threads=threads, savefile=savefile)

    print(f"Subdomains found for {domain}:")
    for subdomain in subdomains:
        print(subdomain)

if __name__ == '__main__':
    main2()
