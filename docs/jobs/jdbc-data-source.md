# JDBC Data Source

To add a database as a data source in Axibase Collector, navigate to **Data Sources > Databases** and select "New Data Source".

| FIELD        | DESCRIPTION |
|:-------------|:-------------|
| <a name="db-name"></a>Name | Name of data source. |
| Database Type  | Type of database. <br> Possible values: Oracle, MSSQL, MSSQL_Native, DB2, SOLID, MYSQL, POSTGRESQL, SYBASE, DERBY, SAP, PI_SERVER, VERTICA, CUSTOM      |
| <a name="db-server"></a>Server | IP or hostname of the target server. |
| <a name="db-port"></a>Port | Port on which the database is listening. |
| <a name="db-database"></a>Database | Name of the database residing on the database server. |
| Instance | Name of the instance. |
| Username | Username which will be connecting to the database. We recommend that a read-only account is created to access the database. |
| Password | User password. |
| Driver Properties | Extended JDBC diver properties. Specific to each database |
| Test Query | Test query to keep the connection alive. |
| Max Active | Maximum number of active connections. |
| Max Idle | Maximum number of idle connections. |
| Min Idle | Minimum number of idle connections. |
| Initial Size | Initial size of the connection pool. |
| Max Wait (seconds) | Maximum number of seconds for a job to wait until it requires a connection from the pool. |
| Max Age (minutes) | Maximum duration of the connection, after which the connection will be closed and reopened. |
| Login Timeout (seconds) | Wait duration when opening a connection. |
| Idle Timeout (seconds) | Duration after which an unused connection is closed. |
| Socket Timeout (seconds) | Duration after which the connection is dropped if there is no response from the server. |

![](./images/datasource-database.png)
