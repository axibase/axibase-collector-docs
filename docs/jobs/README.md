# Jobs

**Type** | **Description**
----- | -----
[AWS](aws.md) | Collects AWS statistics using CloudWatch API.
[Docker](docker.md) | Collects container statistics using Docker Engine API.
[JDBC](jdbc.md) | Executes SQL queries against relational databases.<br>Stores result sets as series and properties.
[File](file.md) | Downloads CSV/TSV files from `http://` and `file://` sources and uploads them into ATSD for parsing.<br>Supports wildcards, placeholders, and reliable delivery with pre- and post-upload file actions.
[JMX](jmx.md) | Collects MBean attribute values from Java applications.
[HTTP](http.md) | Executes HTTP requests or Web Driver scripts. <br>Stores transaction status and response code.
[ICMP](icmp.md) | Pings hostnames/IP addresses and stores response status.
[JSON](json.md) | Downloads JSON documents and extracts series and properties using JSONPath.
[OVPM](ovpm.md) | Offloads statistics from HP OpenView Performance Manager.
[PI](pi.md) | Extracts PI points archive data via JDBC driver.
[SNMP](snmp.md) | Queries SNMP devices using built-in and custom MIB files.
[Socrata](socrata.md) | Downloads JSON documents published in Socrata schema and converts them into series, property, and message commands.
[TCP](tcp.md) | Connects to hostnames/IP addresses and stores connection status.
