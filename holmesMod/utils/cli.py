import argparse
from termcolor import colored

def display_banner():
    global description
    ascii_art = r'''
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      || ITSEC || | == |
      ||  ASIA || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
    `"""""""""""""`  '-'
'''
    ascii_art = ascii_art.replace('ITSEC', colored('ITSEC', 'red', attrs=['bold']))
    ascii_art = ascii_art.replace('ASIA', colored('ASIA', 'red', attrs=['bold']))
    print(colored(ascii_art, 'cyan', attrs=['bold']))

    description = "[#] HolmesGeo - A Simple Tool for IP Geolocation Check [#]"
    description = description.replace('HolmesGeo', colored('HolmesGeo', 'red', attrs=['bold']))
    description = description.replace('A Simple Tool for IP Geolocation Check', colored('A Simple Tool for IP Geolocation Check', 'green', attrs=['bold']))


def display_guides():

    guides = """
================================================================================
| Please provide a file with IP addresses to check:                            |
|  - Use --apache to extract IPs from Apache log file.                         |
|  - Use --csv to extract IPs from a CSV file.                                 |
|  - Input from stdin is automatically detected when using pipe (|).           |
|  - Use --check to perform IP check from a text file with one IP per line.    |
|                                                                              |
| Additional Options:                                                          |
|  - Use --no-rdns to disable reverse DNS lookups (speeds up processing).      |
|  - Use --virtot to perform additional certificate and registrar lookup.      |
|  - Use --no-output to skip file generation (console output only).            |
|                                                                              |
| Usage Example:                                                               |
| python3 -m holmesMod.main --apache apache.log                                |
| python3 -m holmesMod.main --csv file.csv                                     |
| python3 -m holmesMod.main --csv file.csv --column source_ip                  |
| python3 -m holmesMod.main --check list_ip.txt                                |
| python3 -m holmesMod.main --check list_ip.txt --virtot                       |
| python3 -m holmesMod.main --check list_ip.txt --no-rdns                      |
| python3 -m holmesMod.main --check list_ip.txt --no-output                    |
| python3 -m holmesMod.main --apache apache.log --virtot                       |
| python3 -m holmesMod.main --csv file.csv --virtot                            |
| python3 -m holmesMod.main --csv file.csv --column source_ip --virtot         |
| cat ip.txt | python3 -m holmesMod.main --virtot                              |
| cat ip.txt | python3 -m holmesMod.main --no-rdns                             |
| cat ip.txt | python3 -m holmesMod.main --no-output                           |
|                                                                              |
| ./chk.sh --check samples/iplist.txt                                          |
| ./chk.sh --check samples/iplist.txt --no-rdns                                |
| ./chk.sh --check samples/iplist.txt --no-output                              |
| ./chk.sh --csv samples/sample.csv --column ip_address                        |
| ./chk.sh --apache samples/sample_log.txt                                     |
| cat samples/iplist.txt | ./chk.sh --virtot                                   |
| cat samples/iplist.txt | ./chk.sh --no-output                                |
| echo "8.8.8.8" | ./chk.sh                                                    |
| echo -e "8.8.8.8\\n37.252.185.229" | ./chk.sh --no-output                    |
|                                                                              |
================================================================================
"""
    print(colored(guides, 'cyan'))


def parse_arguments():
    
    parser = argparse.ArgumentParser(description=description)
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument("--apache", metavar="FILE", 
                        help="Extract IPs from an Apache log file")
    input_group.add_argument("--csv", metavar="FILE", 
                        help="Extract IPs from a CSV file")
    input_group.add_argument("--check", metavar="FILE", 
                        help="Perform IP check from a text file with one IP per line")
    
    parser.add_argument("--column", default=None, 
                        help="Column name containing IP addresses in CSV mode")
    parser.add_argument("--virtot", action="store_true",
                        help="Perform additional certificate and registrar lookup")
    parser.add_argument("--no-rdns", action="store_true",
                        help="Disable reverse DNS lookups (speeds up processing)")
    parser.add_argument("--no-output", action="store_true",
                        help="Skip file generation and output results to console only")
    
    display_guides()
    args = parser.parse_args()
    if args.apache:
        args.mode = "apache"
        args.file = args.apache
    elif args.csv:
        args.mode = "csv"
        args.file = args.csv
    elif args.check:
        args.mode = "check"
        args.file = args.check
    else:
        args.mode = None
        args.file = None
    
    return args
