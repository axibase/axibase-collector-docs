# Enabling JMX in Java Applications

## Examples

### Apache ActiveMQ Server

#### Reference Information

* Configuring JMX in ActiveMQ: [activemq.apache.org/jmx.html](http://activemq.apache.org/jmx.html)

#### Configure JMX properties

* Change to ActiveMQ installation directory:

```sh
cd /opt/apache-activemq-5.13.1
```

* Modify JMX settings in the ActiveMQ JVM launch options. <br>Search for the `ACTIVEMQ_SUNJMX_START` setting and change it as specified below.

##### ActiveMQ 5.11.x and later

```sh
vi ./bin/env
```

```properties
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote.port=1090"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote.rmi.port=1090"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote.ssl=false"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Djava.rmi.server.hostname=activemq_hostname"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote.password.file=${ACTIVEMQ_CONF}/jmx.password"
ACTIVEMQ_SUNJMX_START="$ACTIVEMQ_SUNJMX_START -Dcom.sun.management.jmxremote.access.file=${ACTIVEMQ_CONF}/jmx.access"
```

##### ActiveMQ 5.10.x and earlier

```sh
vi ./bin/activemq
```

```properties
ACTIVEMQ_SUNJMX_START="-Dcom.sun.management.jmxremote \
   -Dcom.sun.management.jmxremote.port=1090 \
   -Dcom.sun.management.jmxremote.rmi.port=1090 \
   -Dcom.sun.management.jmxremote.ssl=false \
   -Djava.rmi.server.hostname=activemq_hostname \
   -Dcom.sun.management.jmxremote.password.file=${ACTIVEMQ_BASE}/conf/jmx.password \
   -Dcom.sun.management.jmxremote.access.file=${ACTIVEMQ_BASE}/conf/jmx.access"
```

> Replace `activemq_hostname` with the full hostname or IP address of the ActiveMQ server.
> This should be the same hostname that Axibase Collector will be using when connecting to the ActiveMQ server.

The result should be as shown in the image below:

![SUN_JMX_START_IMAGE](./images/very_new_screen.png)

#### Setup JMX User Credentials

Change to `./conf` directory.

Add/edit the `jmx.access` and `jmx.password` files as follows.

Make sure the owner of these files is the same as ActiveMQ user.

`jmx.access`:

```txt
# The "monitorRole" role has readonly access.
monitorRole readonly
```

`jmx.password`:

```txt
# The "monitorRole" role has password "abc123".
monitorRole abc123
```

#### Secure Password File

Secure access to the  `jmx.password` file by restricting permissions:

```sh
chmod -v 0600 ./conf/jmx.password
```

#### Restart ActiveMQ Server

```sh
./bin/activemq stop
./bin/activemq start
```
