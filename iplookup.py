import argparse
from JSON import JSON

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address", help="IP address to lookup. IPv4 or IPv6 can be used.")
args = parser.parse_args()

if args.address is None:  # Check if the arguments is None
    parser.print_help()
    exit(1)

query = JSON(args.address)
query.parse_json()
