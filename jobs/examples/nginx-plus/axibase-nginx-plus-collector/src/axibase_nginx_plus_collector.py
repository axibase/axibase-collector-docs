#===============================================================================
# Axibase NGINX plus Collector main script.
# Run: 
#        python axibase_nginx_plus_collector.py -h 
# for more information.
#===============================================================================
from axibase_npc_core import Collector, Configuration, CollectorArgParser
args = CollectorArgParser().parse_arguments()
user_config = Configuration(addresses=args.items, atsd_url=args.atsd_url, quiet=args.quiet)
Collector(user_config).collect()
