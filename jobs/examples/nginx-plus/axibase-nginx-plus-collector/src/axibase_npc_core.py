import json, urllib2, socket, argparse
from urlparse import urlparse
from datetime import datetime, timedelta

##############################################################################################################
class Collector():
    def __init__(self, configuration):
        '''
        Build a collector to collect data from NGINX-plus server and store it in ATSD.
        All the required data is provided via config object passed to the constructor.
        See :class:`Configuration` for more details.
        '''
        self.config =  configuration
    def collect(self):
        '''Collect data from all servers specified in config object passed to the constructor'''
        self.config.get_logger().log("Starting collection...")
        for address in self.config.get_addresses():
            try:
                self.config.get_logger().log("Processing " + str(address))
                fetched_data = urllib2.urlopen(str(address) + "/status")
                self.config.get_logger().log("All data loaded.")
                nginx_stats = json.load(fetched_data)
                jsoner = _NginxJsonProcessor(self.config)
                self.config.get_logger().log("Traversing obtained json ... \n")
                entity = address.replace('https://', '').replace('http://', '')
                commands = jsoner.process_nginx_stats(entity, nginx_stats)
                self.config.get_logger().log("Commands built.("+str(len(commands))+")")
                atsd = _ATSDManager(self.config)
                atsd.send_commands(commands)
                self.config.get_logger().log("All done.\n")
            except Exception as e:
                self.config.get_logger().log("Collector error:" + str(e))
                

############################################################################################################
class Configuration:
    ''' Program configuration '''
    def __init__(self, addresses=["http://demo.nginx.com"], metric_prefix="nginx-plus.", atsd_url="tcp://localhost:8081", quiet=False):
        '''
        Args:
            addresses (list)       : Item list of all NGINX-plus servers to collect data from.
            prefix (str)           : Metric prefix for all metrics 
            atsd_url (str)         : ATSD url to store data at
            quiet (bool)           : Flag indicating if program should not generate output  
        '''
        self.substitutions = {"server_zones/*/": "server_zone","stream/server_zones/*/": "status_zone","stream/upstreams/*/":"dyn_config_group","upstreams/*/":"backend","caches/*/":"cache"}
        self.nginx_properties = ["version", "nginx_version", "address", "generation", "load_timestamp", "pid"]
        self.addresses = addresses
        self.prefix = metric_prefix
        self.atsd_url = atsd_url
        self.logger = _Logger(quiet)
        #
        self.nginx_keys = ["address"]
        self.nginx_properties = ["version", "nginx_version", "generation", "load_timestamp", "pid"]
        self.nginx_specials = ["server_zones", "upstreams", "caches", "stream"]
        self.upstream_peer_keys = ["server"]
        self.upstream_peer_properties = ["backup", "weight", "id", "state"]
        self.stream_ups_peer_keys = ["server"]
        self.stream_ups_peer_properties = ["backup", "weight", "id", "state"]
        self.upstream_prop_type = "upstreams"
        self.upstream_peer_pc_type = "upstreams.peers"
        self.nginx_pc_type = "nginx_info"
        self.cache_pc_type = "caches"
        self.stream_ups_peer_pc_type = "stream.upstreams.peers"
        self.server_zone_sc_type= "server_zones"
        self.upstream_sc_type= "upstreams"
        self.upstream_peer_sc_type= "upstreams.peers"
        self.cache_sc_type= "caches"
        self.stream_sz_sc_type= "stream.server_zones"
        self.stream_ups_sc_type= "stream.upstreams"
        self.stream_ups_peer_sc_type= "stream.upstreams.peers"
            
    def get_internal_separator(self):
        return ".";
    def get_substitutions(self):
        return self.substitutions;
    def get_addresses(self):
        return self.addresses;
    def get_logger(self):
        return self.logger
    def get_metric_prefix(self):
        return self.prefix;
    def get_atsd_url(self):
        return self.atsd_url
    def get_nginx_keys(self):
        return self.nginx_keys
    def get_nginx_props(self):
        return self.nginx_properties
    def get_nginx_specials(self):
        return self.nginx_specials
    def get_upstream_peer_keys(self):
        return self.upstream_peer_keys
    def get_upstream_peer_props(self):
        return self.upstream_peer_properties
    def get_stream_ups_peer_props(self):
        return self.stream_ups_peer_properties
    def get_stream_ups_peer_keys(self):
        return self.stream_ups_peer_keys
    def get_upstream_prop_type(self):
        return self.upstream_prop_type
    def get_upstream_peer_prop_type(self):
        return self.upstream_peer_pc_type
    def get_nginx_prop_type(self):
        return self.nginx_pc_type
    def get_stream_ups_peer_prop_type(self):
        return self.stream_ups_peer_pc_type
    def get_cache_prop_type(self):
        return self.cache_pc_type
    def get_server_zone_series_type(self):
        return self.server_zone_sc_type
    def get_upstream_series_type(self):
        return self.upstream_sc_type
    def get_upstream_peer_series_type(self):
        return self.upstream_peer_sc_type
    def get_cache_series_type(self):
        return self.cache_sc_type
    def get_stream_sz_series_type(self):
        return self.stream_sz_sc_type
    def get_stream_ups_series_type(self):
        return self.stream_ups_sc_type
    def get_stream_ups_peer_series_type(self):
        return self.stream_ups_peer_sc_type

############################################################################################################    
class CollectorArgParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-a", "--atsd-url", default="tcp://localhost:8081", help="URL of ATSD (default: %default)")
        self.parser.add_argument('-q', '--quiet', dest="quiet", default=False, action="store_true")
        self.parser.add_argument("-i", "--items", nargs='+', type=str, default=["http://demo.nginx.com"], help="List of items (default: %default)")
        
    def parse_arguments(self):
        return self.parser.parse_args()
############################################################################################################    
class _NginxJsonProcessor:
    def __init__(self, configuration):
        self.config = configuration
    
    def process_nginx_stats(self, entity, json_object):
        '''
        Forms a `commands` list containing commands to target ATSD for the whole server.
        Appends different commands containg information about the whole server:
            * series command with
                metrics:  processes.respawned, connections.active, connections.idle, connections.accepted, connections.dropped, ssl.handshakes, ssl.session_reuses, ssl.handshakes_failed, requests.current, requests.total
            * property command with
                properties:     version, nginx_version, generation, load_timestamp, pid
                keys:           address
        '''
        commands = []
        nginx_property = _CommandProperty(entity, self.config.get_nginx_prop_type(), self.config.get_metric_prefix())
        nginx_series = _CommandSeries(entity, self.config.get_metric_prefix())
        self._process_multiple_properties(entity, json_object, self.config.get_nginx_keys(), self.config.get_nginx_props(), nginx_property)
        self._process_unknown_block_recursively(entity, json_object, [], nginx_series, self.config.get_nginx_keys() + self.config.get_nginx_props() + self.config.get_nginx_specials() + ["timestamp"])
        commands.append(nginx_property)
        commands.append(nginx_series)
        for special in self.config.get_nginx_specials():
            self._process_special_block_by_name(special, entity, json_object[special], commands)
        for command in commands:
            command.set_timestamp(json_object.get("timestamp")) 
        return commands
    
    def _process_special_block_by_name(self, name, entity, block, commands):
        getattr(self, "_process_" + name + "_block")(entity, block, commands)
        
    def _process_server_zones_block(self, entity, server_zones_block, commands):
        '''
        For each SERVER_ZONE appends:
            * series command, containing
                metrics: received, responses.5xx, responses.2xx, responses.4xx, responses.3xx, responses.1xx, responses.total, processing, discarded, requests, sent
                tags:    type(=server_zones), name
        to `commands` list
        '''
        self.config.get_logger().log("---------Processing SERVER ZONES")
        if not server_zones_block:
            self.config.get_logger().log("---------No block detected")
            return
        for server_zone, server_zone_desc in server_zones_block.items():
            self.config.get_logger().log("------Processing SERVER ZONE " + str(server_zone))
            server_zone_series = _CommandSeries(entity, self.config.get_metric_prefix())
            server_zone_series.add_tag("type", self.config.get_server_zone_series_type())
            server_zone_series.add_tag("name", server_zone)
            self._process_unknown_block_recursively(entity=entity, block=server_zone_desc, path_stack=[], built_command=server_zone_series)
            commands.append(server_zone_series)
        self.config.get_logger().log("---------Processing SERVER ZONES finished")
    
    def _process_upstreams_block(self, entity, upstreams_block, commands):
        '''
        For each UPSTREAM appends:
            * series command with
                metrics:     keepalive 
                tags:        type(=upstreams), name
        to `commands` list
        
        For each UPSTREAM.PEER appends:
            * property command with 
                keys:           server, upstream           
                properties:     type, backup, weight, id, state [, last_passed]
            * series command with
                metrics:        requests, sent, received, fails, unavail, health_checks.checks, health_checks.fails, health_checks.unhealthy, health_checks.last_passed, downtime, downstart, selected, responses.1xx, responses.2xx, responses.3xx, responses.4xx, responses.5xx, responses.total
                tags:           type(=upstreams.peers), upstream
        to `commands` list 
        '''
        self.config.get_logger().log("---------Processing UPSTREAMS")
        if not upstreams_block:
            self.config.get_logger().log("---------No block detected")
            return
        for upstream, upstream_description in upstreams_block.items():
            self.config.get_logger().log("------Processing UPSTREAM " + str(upstream))
            upstream_series = _CommandSeries(entity, self.config.get_metric_prefix())
            upstream_series.add_tag("type", self.config.get_upstream_series_type())
            upstream_series.add_tag("name", upstream)
            upstream_series.add_metric("keepalive", upstream_description.get("keepalive"))
            optional_block = upstream_description.get("queue")
            if optional_block is not None:
                upstream_properties = _CommandProperty(entity, self.config.get_upstream_prop_type() ,self.config.get_metric_prefix())
                upstream_properties.add_property("queue.max_size", optional_block.get("max_size"))
                commands.append(upstream_properties)
                upstream_series.add_metric("queue.size", optional_block.get("max_size"))
                upstream_series.add_metric("queue.overflows", optional_block.get("overflows"))
            commands.append(upstream_series)
            for peer in upstream_description["peers"]:
                self.config.get_logger().log("---Processing UPSTREAM.PEER " + str(peer["server"]))
                peer_property = _CommandProperty(entity, self.config.get_upstream_peer_prop_type(), self.config.get_metric_prefix())
                peer_property.add_key("type", self.config.get_upstream_peer_prop_type())
                peer_property.add_key("upstream", upstream)
                peer_property.add_property("last_passed", peer.get('health_checks', {}).get('last_passed'))
                self._process_multiple_properties(entity, peer, self.config.get_upstream_peer_keys(), self.config.get_upstream_peer_props(), peer_property)
                peer_series = _CommandSeries(entity, self.config.get_metric_prefix())
                peer_series.add_tag("type", self.config.get_upstream_peer_series_type() )
                peer_series.add_tag("server", str(peer["server"]))
                peer_series.add_tag("upstream", upstream)
                self._process_unknown_block_recursively(entity=entity, block=peer, path_stack=[], built_command=peer_series, ignored_keys=self.config.get_upstream_peer_keys()+self.config.get_upstream_peer_props() + ["last_passed"])
                commands.append(peer_property)
                commands.append(peer_series)
        self.config.get_logger().log("---------Processing UPSTREAMS finished")
                
    def _process_caches_block(self, entity, caches_block, commands):
        '''
        For each CACHE appends:
            * series commands with
                metrics:         responses, bytes [, responses_written, bytes_written]
                tags:            type, name, cache_status
            * property command with
                keys:          responses, bytes [, responses_written, bytes_written]
                properties:    type, name, cache_status, size, max_size, cold
        to `commands` list
        '''
        self.config.get_logger().log("---------Processing CACHES")
        if not caches_block:
            self.config.get_logger().log("---------No block detected")
            return
        for cache, cache_description in caches_block.items():
            cache_property = _CommandProperty(entity, self.config.get_cache_prop_type(), self.config.get_metric_prefix())
            cache_property.add_key("name", cache)
            cache_property.add_key("type", self.config.get_cache_prop_type())
            self.config.get_logger().log("---Processing CACHE " + str(cache))
            for cache_key, cache_value in cache_description.items():
                if isinstance(cache_value, dict):
                    cache_series = _CommandSeries(entity, self.config.get_metric_prefix())
                    cache_series.add_tag("type", self.config.get_cache_series_type())
                    cache_series.add_tag("name", cache)
                    cache_series.add_tag("cache_status", cache_key)
                    cache_series.add_metric("responses", cache_value.get("responses"))
                    cache_series.add_metric("bytes", cache_value.get("bytes"))
                    cache_series.add_metric("responses_written", cache_value.get("responses_written"))
                    cache_series.add_metric("bytes_written", cache_value.get("bytes_written"))
                    commands.append(cache_series)
                else:
                    cache_property.add_property(cache_key, cache_value)
            commands.append(cache_property)
        self.config.get_logger().log("---------Processing CACHES finished")
    
    def _process_stream_block(self, entity, stream_block, commands):
        '''
        For each STREAM.SERVER_ZONE appends:
            * series command with 
                metrics:         processing, connections, received, sent 
                tags:            type(=stream.server_zones), name
        to `commands` list
        
        For each STREAM.UPSTREAMS.PEER appends:
            * property command with
                keys:           server           
                properties:     type(=stream.upstreams.peers), stream, backup, weight, id, state[, last_passed]
            * series command with
                metrics:      received, fails, selected, connections, health_checks.fails, health_checks.checks, health_checks.unhealthy, unavail, downtime, active, downstart, sent
                tags:         type(=stream.upstream.peer), stream.upstream 
            to `commands` list 
        '''
        if not stream_block:
            self.config.get_logger().log("---------No block detected")
            return
        self.config.get_logger().log("---------Processing STREAM.SERVER_ZONES")
        server_zones_block = stream_block.get("server_zones")
        for server_zone, server_zone_desc in server_zones_block.items():
            self.config.get_logger().log("------Processing SERVER_ZONE " + str(server_zone))
            server_zone_series = _CommandSeries(entity, self.config.get_metric_prefix())
            server_zone_series.add_tag("type", self.config.get_stream_sz_series_type())
            server_zone_series.add_tag("name", server_zone)
            self._process_unknown_block_recursively(entity, server_zone_desc, [], server_zone_series)
            commands.append(server_zone_series)
        self.config.get_logger().log("---------Processing STREAM.UPSTREAMS")
        upstreams_block = stream_block.get("upstreams")
        for upstream, upstream_description in upstreams_block.items():
            self.config.get_logger().log("------Processing STREAM.UPSTREAM " + str(upstream))
            upstream_series = _CommandSeries(entity, self.config.get_metric_prefix())
            upstream_series.add_tag("type", self.config.get_stream_ups_series_type())
            upstream_series.add_tag("name", upstream)
            for peer in upstream_description.get("peers"):
                self.config.get_logger().log("---Processing STREAM.UPSTREAM.PEER " + str(peer.get("server")))
                peer_property = _CommandProperty(entity, self.config.get_stream_ups_peer_prop_type(), self.config.get_metric_prefix())
                peer_property.add_key("upstream", upstream)
                peer_property.add_key("type", self.config.get_stream_ups_peer_prop_type())###extra
                peer_property.add_property("last_passed", peer.get('health_checks', {}).get('last_passed'))
                self._process_multiple_properties(entity, peer, self.config.get_stream_ups_peer_keys(), self.config.get_stream_ups_peer_props(), peer_property)
                peer_series = _CommandSeries(entity, self.config.get_metric_prefix())
                peer_series.add_tag("type", self.config.get_stream_ups_peer_series_type())
                peer_series.add_tag("server",  str(peer.get("server")))
                peer_series.add_tag("upstream", upstream)
                self._process_unknown_block_recursively(entity, peer, [], peer_series, ignored_keys=self.config.get_stream_ups_peer_keys()+self.config.get_stream_ups_peer_props()+["last_passed"])
                commands.append(peer_property)
                commands.append(peer_series)
        self.config.get_logger().log("---------Processing STREAM.SERVER_ZONES finished")
    ###
    def _process_multiple_properties(self, entity, json_object, key_names, properties_names, built_command):
        for key in key_names:
            built_command.add_key(key, json_object.get(key))
        for prop in properties_names:
            built_command.add_property(prop, json_object.get(prop))
            
    def _process_unknown_block_recursively(self, entity, block, path_stack, built_command, ignored_keys=[]):
        for key, value in block.items():
            if not (key in ignored_keys):
                path_stack.append(key)
                if (self._is_complex_part(value)):
                    self._process_unknown_block_recursively(entity, value, path_stack, built_command, ignored_keys)
                else:
                    if self._is_metric(value):
                        built_command.add_metric(self._join_to_path(path_stack), value)
                    else:
                        built_command.add_tag(self._join_to_path(path_stack), value)
                path_stack.pop()
                    
    def _is_complex_part(self, part):
        return isinstance(part, dict) or isinstance(part, list)
        
    def _is_metric(self, value):
        try: 
            float(value)
            return True
        except:
            return False
        
    def _join_to_path(self, stack):
        return self.config.get_internal_separator().join(stack)
########################
class _Command:
    def __init__(self, entity, prefix=""):
        self.entity = entity
        self.prefix = prefix
        self.atsd_format = ""
        self.atsd_format_inconsistent = False
                
    def __str__(self):
        return self.get_atsd_format()
    
    def __repr__(self):
        return self.get_atsd_format()
       
    def get_entity(self):
        return self.entity
    
    def set_entity(self, entity):
        self.entity = entity
    
    def build_atsd_string(self):
        raise NotImplementedError
    
    def toISO(self, timestamp):
        utc_time = datetime(1970, 1, 1) + timedelta(milliseconds=timestamp)
        return utc_time.isoformat()[:-3]+"Z"
    
    def validate(self):
        raise NotImplementedError
    
    def normalize_value(self, value):
        if (str(value) == "True"):
            return "true"
        elif (str(value) == "False"):
            return "false"
        else: 
            return value
    
    def get_atsd_format(self):
        if not self.atsd_format or self.atsd_format_inconsistent:
            self.validate()
            self.atsd_format = self.build_atsd_string()
        self.atsd_format_inconsistent = False
        return self.atsd_format
###    
class _CommandSeries(_Command):
    def __init__(self, entity, prefix=""):
        _Command.__init__(self, entity, prefix)
        self.metrics = dict()
        self.tags = dict()
        self.timestamp = 0
        self.atsd_format_inconsistent = False
        
    def get_tags(self):
        return self.tags

    def get_metrics(self):
        return self.metrics
       
    def add_tag(self, tag_name, tag):
        if tag_name and tag:
            self.tags[tag_name] = self.normalize_value(tag)
            self.atsd_format_inconsistent = True
                        
    def add_metric(self, metric_name, metric):
        if metric_name is not None and metric is not None:
            self.metrics[metric_name] = int(metric) #All metrics are ints
            self.atsd_format_inconsistent = True
                    
    def set_timestamp(self, timestamp):
        if timestamp is not None:
            self.timestamp = timestamp
            self.atsd_format_inconsistent = True
    
    def validate(self):
        if not self.entity:
            raise ValueError('No entity detected!')
        if not self.metrics:
            raise ValueError('No metrics detected!')
         
    def build_atsd_string(self):
        atsd_format = "series "
        atsd_format += "e:" + self.entity + " "
        if self.timestamp:
            atsd_format += "d:" + str(self.toISO(self.timestamp)) + " "
        for tag_name, tag in self.tags.iteritems():
            atsd_format += "t:" + str(tag_name) + "=" + str(tag) + " "
        for metric_name, metric in self.metrics.iteritems():
            atsd_format += "m:" + str(self.prefix) + str(metric_name) + "=" + str(metric) + " "
        return atsd_format.strip()
###
class _CommandProperty(_Command):
    def __init__(self, entity, command_type, prefix=""):
        _Command.__init__(self, entity, prefix)
        self.pc_type = command_type
        self.props = dict()
        self.keys = dict()
        self.atsd_format_inconsistent = False
        self.timestamp = 0
        
    def add_key(self, key_name, key_value):
        if key_name is not None and key_value is not None: 
            self.keys[key_name] = self.normalize_value(key_value)
            self.atsd_format_inconsistent = True
                  
    def add_type(self, command_type): 
        self.type = str(command_type)
        self.atsd_format_inconsistent = True
        
        
    def add_property(self, property_name, property_value):
        if property_name is not None and property_value is not None:
            self.props[property_name] = self.normalize_value(property_value)
            self.atsd_format_inconsistent = True
                    
    def set_timestamp(self, timestamp):
        if timestamp is not None:
            self.timestamp = timestamp
            self.atsd_format_inconsistent = True
            
    def validate(self):
        if not self.entity:
            raise ValueError('No entity detected!')
        if not self.props:
            raise ValueError('No props detected!')
        if not self.pc_type:
            raise ValueError('No type detected!')
        
    def build_atsd_string(self):
        atsd_format = "property "
        atsd_format += "t:" + str(self.pc_type) + " "
        atsd_format += "e:" + self.entity + " "
        if self.timestamp:
            atsd_format += "d:" + str(self.toISO(self.timestamp)) + " "
        for key_name, key_value in self.keys.iteritems():
            atsd_format += "k:" + str(key_name) + "=" + str(key_value) + " "
        for prop_name, prop_value in self.props.iteritems():
            atsd_format += "v:" + str(prop_name) + "=" + str(prop_value) + " "
        return atsd_format.strip()
############################################################################################################
class _Logger:
    def __init__(self, quiet):
        self.quiet = quiet
    
    def log(self, message):
        if not self.quiet:
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), "|", message

#################################################################################
class _ATSDManager():
    def __init__(self, configuration):
        self.config = configuration
        
    def send_commands(self, commands):
        self.config.get_logger().log("Preparing data...")
        command_batch =  "\n".join(sorted(map(lambda x: x.get_atsd_format(), commands)))
        self.config.get_logger().log("Data prepared: \n\n" + str(command_batch) + "\n")
        atsd_url_info = urlparse(self.config.get_atsd_url())
        sock = socket.socket()
        self.config.get_logger().log("Connecting to ATSD...")
        sock.connect((atsd_url_info.hostname, atsd_url_info.port))
        self.config.get_logger().log("Sending...")
        sock.send(command_batch)
        sock.close()
        self.config.get_logger().log("Sent.")
