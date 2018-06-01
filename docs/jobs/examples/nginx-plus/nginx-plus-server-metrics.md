# NGINX Plus Server Metrics

## Server Metrics

* nginx-plus.processes.respawned
* nginx-plus.connections.active
* nginx-plus.connections.idle
* nginx-plus.connections.accepted
* nginx-plus.connections.dropped
* nginx-plus.ssl.handshakes
* nginx-plus.ssl.session_reuses
* nginx-plus.ssl.handshakes_failed
* nginx-plus.requests.current
* nginx-plus.requests.total

## Server Zone Metrics

* nginx-plus.received
* nginx-plus.responses.5xx
* nginx-plus.responses.2xx
* nginx-plus.responses.4xx
* nginx-plus.responses.3xx
* nginx-plus.responses.1xx
* nginx-plus.responses.total
* nginx-plus.processing
* nginx-plus.discarded
* nginx-plus.requests
* nginx-plus.sent

## Upstream Metrics

* nginx-plus.keepalive

## Upstream's Peer Metrics

* nginx-plus.received
* nginx-plus.fails
* nginx-plus.responses.5xx
* nginx-plus.responses.2xx
* nginx-plus.responses.4xx
* nginx-plus.responses.3xx
* nginx-plus.responses.1xx
* nginx-plus.responses.total
* nginx-plus.selected
* nginx-plus.health_checks.last_passed
* nginx-plus.health_checks.fails
* nginx-plus.health_checks.checks
* nginx-plus.health_checks.unhealthy
* nginx-plus.unavail
* nginx-plus.downtime
* nginx-plus.active
* nginx-plus.downstart
* nginx-plus.requests
* nginx-plus.sent

## Cache Metrics

* nginx-plus.responses
* nginx-plus.bytes
* nginx-plus.responses_written
* nginx-plus.bytes_written

## Stream.server_zone Metrics

* nginx-plus.stream.server_zone.connections
* nginx-plus.stream.server_zone.received
* nginx-plus.stream.server_zone.processing
* nginx-plus.stream.server_zone.sent

## Stream.upstream's Peer Metrics

* nginx-plus.received
* nginx-plus.fails
* nginx-plus.selected
* nginx-plus.connections
* nginx-plus.health_checks.last_passed
* nginx-plus.health_checks.fails
* nginx-plus.health_checks.checks
* nginx-plus.health_checks.unhealthy
* nginx-plus.unavail
* nginx-plus.downtime
* nginx-plus.active
* nginx-plus.downstart
* nginx-plus.sent