import argparse
from JSON import JSON

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", help="the format of the output (XML, JSON, CSV, Newline, PHP)")
parser.add_argument("-a", "--address", help="IP address to lookup. IPv4 or IPv6 can be used.")
args = parser.parse_args()

if args.format is not None and args.address is None:
    print("Provide an address as well")
    exit(9)
elif args.address is not None and args.format is None:
    print("Please provide a format as well")
    exit(9)
elif args.format.upper() == "JSON":
    query = JSON(args.address)
    query.parse_json()
