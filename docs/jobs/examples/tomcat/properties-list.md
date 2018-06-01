# Collected Tomcat Properties

## jmx.tomcat.connector

```json
{
    "type": "jmx.tomcat.connector",
    "entity": "nurswgvml010",
    "key": {
      "port": "9080"
    },
    "tags": {
      "acceptcount": "128",
      "allowtrace": "false",
      "buffersize": "2048",
      "compression": "off",
      "connectionlinger": "-1",
      "connectiontimeout": "20000",
      "connectionuploadtimeout": "300000",
      "disableuploadtimeout": "true",
      "emptysessionpath": "false",
      "enablelookups": "false",
      "executorname": "Internal",
      "keepalivetimeout": "-1",
      "maxhttpheadersize": "8192",
      "maxkeepaliverequests": "100",
      "maxparametercount": "10000",
      "maxpostsize": "2097152",
      "maxthreads": "200",
      "port": "9080",
      "protocol": "HTTP/1.1",
      "protocolhandlerclassname": "org.apache.coyote.http11.Http11Protocol",
      "proxyport": "0",
      "redirectport": "8443",
      "scheme": "http",
      "secure": "false",
      "tcpnodelay": "true",
      "threadpriority": "5",
      "uriencoding": "utf-8",
      "usebodyencodingforuri": "false",
      "xpoweredby": "false"
    },
    "date": "2016-05-31T09:39:30.255Z"
  }
```

## jmx.tomcat.engine

```json
{
    "type": "jmx.tomcat.engine",
    "entity": "nurswgvml010",
    "key": {},
    "tags": {
      "basedir": "/home/axibase/af/AxibaseFabrica/AxibaseServer/app",
      "defaulthost": "localhost",
      "modelertype": "org.apache.catalina.core.StandardEngine",
      "name": "Standalone"
    },
    "date": "2016-05-31T09:42:45.612Z"
  }
```

## jmx.tomcat.globalrequestprocessor

```json
{
    "type": "jmx.tomcat.globalrequestprocessor",
    "entity": "nurswgvml010",
    "key": {
      "name": "http-9080"
    },
    "tags": {
      "bytesreceived": "59850",
      "bytessent": "6358384",
      "errorcount": "21",
      "maxtime": "12540416",
      "modelertype": "org.apache.coyote.RequestGroupInfo",
      "processingtime": "21779825",
      "requestcount": "1054"
    },
    "date": "2016-05-31T09:43:30.295Z"
  }
```

## jmx.tomcat.protocolhandler

```json
{
    "type": "jmx.tomcat.protocolhandler",
    "entity": "nurswgvml010",
    "key": {
      "port": "9080"
    },
    "tags": {
      "backlog": "128",
      "compressablemimetype": "text/html,text/xml,text/plain",
      "compression": "off",
      "compressionminsize": "2048",
      "disableuploadtimeout": "true",
      "domain": "Standalone",
      "keepalive": "true",
      "keepalivetimeout": "-1",
      "maxhttpheadersize": "8192",
      "maxkeepaliverequests": "100",
      "maxsavepostsize": "4096",
      "maxthreads": "200",
      "modelertype": "org.apache.coyote.http11.Http11Protocol",
      "name": "http-9080",
      "port": "9080",
      "processorcache": "-1",
      "secure": "false",
      "socketbuffer": "9000",
      "solinger": "-1",
      "sotimeout": "20000",
      "sslenabled": "false",
      "tcpnodelay": "true",
      "threadpriority": "5",
      "timeout": "300000",
      "unlocktimeout": "250"
    },
    "date": "2016-05-31T09:44:00.310Z"
  }
```

## jmx.tomcat.server

```json
{
      "type": "jmx.tomcat.server",
      "entity": "nurswgvml010",
      "key": {},
      "tags": {
        "modelertype": "org.apache.catalina.core.StandardServer",
        "port": "9005",
        "serverinfo": "Apache Tomcat/6.0.35",
        "servicenames_0": "Standalone:serviceName=Catalina,type=Service",
        "shutdown": "SHUTDOWN"
      },
      "date": "2016-05-31T09:47:30.244Z"
    }
```

## jmx.tomcat.threadpool

```json
{
    "type": "jmx.tomcat.threadpool",
    "entity": "nurswgvml010",
    "key": {
      "name": "http-9080"
    },
    "tags": {
      "acceptorthreadcount": "1",
      "backlog": "128",
      "currentthreadcount": "11",
      "currentthreadsbusy": "0",
      "daemon": "true",
      "maxthreads": "200",
      "modelertype": "org.apache.tomcat.util.net.JIoEndpoint",
      "name": "http-9080",
      "paused": "false",
      "port": "9080",
      "running": "true",
      "solinger": "-1",
      "sotimeout": "20000",
      "tcpnodelay": "true",
      "threadpriority": "5",
      "unlocktimeout": "250"
    },
    "date": "2016-05-31T09:48:00.231Z"
  }
```