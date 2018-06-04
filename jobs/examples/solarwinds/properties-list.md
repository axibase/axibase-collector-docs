# Collected Microsoft SCOM Properties

## sw.node

```json
{
  "type": "sw.node",
  "entity": "nurswgvml011",
  "key": {},
  "tags": {
    "avgresponsetime": "0",
    "caption": "NURSWGVML011",
    "cpuload": "0",
    "description": "Linux NURSWGVML011 3.5.0-23-generic #35~precise1-Ubuntu SMP Fri Jan 25 17:13:26 UTC 2013 x86_64",
    "dynamicip": "0",
    "ip_address": "10.102.0.10",
    "ip_address_type": "IPv4",
    "isserver": "1",
    "lastboot": "2015-06-04 08:15:00.0",
    "machinetype": "net-snmp - Linux",
    "maxresponsetime": "0",
    "memoryused": "2.62119424E8",
    "minresponsetime": "0",
    "objectsubtype": "SNMP",
    "percentloss": "0.0",
    "percentmemoryused": "50",
    "responsetime": "0",
    "severity": "0",
    "status": "1",
    "statusdescription": "Node status is Up.",
    "sysname": "NURSWGVML011",
    "systemuptime": "1386165.5",
    "totalmemory": "5.15076096E8",
    "unmanaged": "0",
    "vendor": "net-snmp"
  },
  "timestamp": 1441377901659
}
```

## sw.vmw.cluster

```json
{
  "type": "sw.vmw.cluster",
  "entity": "nurcls01",
  "key": {},
  "tags": {
    "configstatus": "green",
    "cpucorecount": "0",
    "cpuload": "0.0",
    "cputhreadcount": "0",
    "cpuusagemhz": "0",
    "drsbehaviour": "fullyAutomated",
    "drsstatus": "0",
    "drsvmotionrate": "3",
    "effectivecpu": "0",
    "effectivememory": "0",
    "haadmissioncontrolstatus": "1",
    "hafailoverlevel": "1",
    "hastatus": "0",
    "managedobjectid": "domain-c66",
    "managedstatus": "1",
    "memoryusage": "0.0",
    "memoryusagemb": "0",
    "name": "NURCLS01",
    "overallstatus": "green",
    "totalcpu": "0",
    "totalmemory": "0"
  },
  "timestamp": 1441377902164
}
```

## sw.vmw.cluster.vms

```json
{
  "type": "sw.vmw.cluster.vms",
  "entity": "nurcls02",
  "key": {
    "vmname": "axibase_time-series_database_(atsd)"
  },
  "tags": {
    "host": "nuresx003",
    "memoryconfigured": "1073741824",
    "name": "Axibase Time Series Database (ATSD)",
    "powerstate": "poweredOff",
    "processorcount": "1"
  },
  "timestamp": 1434348901820
}
```

## sw.vmw.host.vms

```json
{
  "type": "sw.vmw.host.vms",
  "entity": "nuresx002",
  "key": {
    "vmname": "nurswgvml003"
  },
  "tags": {
    "cluster": "nurcls02",
    "memoryconfigured": "536870912",
    "name": "NURSWGVML003",
    "powerstate": "poweredOn",
    "processorcount": "1"
  },
  "timestamp": 1441377901851
}
```

## sm.vmware.cluster.vms

```json
{
  "type": "sm.vmware.cluster.vms",
  "entity": "nurcls02",
  "key": {
    "vm": "nurswgvml006"
  },
  "tags": {
    "description": "10.102.0.5 Hadoop/HBASE",
    "host": "nuresx002",
    "mem_size_mb": "2048",
    "num_vcpu": "1",
    "power_state": "On",
    "vm": "NURSWGVML006"
  },
  "timestamp": 1451899080193
}
```

## sw.vmw.vm

```json
{
  "type": "sw.vmw.vm",
  "entity": "nurswgvml011",
  "key": {},
  "tags": {
    "boottime": "2015-06-04 08:08:28.087",
    "cluster": "nurcls02",
    "configstatus": "green",
    "consumedmemload": "0.0",
    "consumedpercentmemload": "0.0",
    "cpuload": "0.97",
    "cpushares": "0",
    "cpuusagemhz": "25",
    "datastoreidentifier": "5270f91f-90add1ce-c319-00242129ebce",
    "guestdnsname": "NURSWGVML011",
    "guestfamily": "linuxGuest",
    "guestname": "Ubuntu Linux (64-bit)",
    "gueststate": "running",
    "guestvmwaretoolsstatus": "toolsOk",
    "guestvmwaretoolsversion": "9221",
    "host": "nuresx002",
    "identitymodifycount": "0",
    "iopsread": "0.0",
    "iopstotal": "0.0",
    "iopswrite": "0.0",
    "ipaddress": "10.102.0.10",
    "islicensed": "1",
    "latencyread": "0.0",
    "latencytotal": "0.0",
    "latencywrite": "0.0",
    "logdirectory": "[datastore1] NURSWGVML011/",
    "managedobjectid": "vm-414",
    "managedstatus": "1",
    "memoryconfigured": "536870912",
    "memoryshares": "534",
    "memusage": "21.192",
    "memusagemb": "109",
    "name": "NURSWGVML011",
    "networkreceiverate": "3.6",
    "networktransmitrate": "1.4666667",
    "networkusagerate": "5.266667",
    "niccount": "1",
    "overallstatus": "green",
    "powerstate": "poweredOn",
    "processorcount": "1",
    "relativepath": "NURSWGVML011",
    "uuid": "564D5286-A10C-873E-5F47-9D7D55B0E4EC",
    "vdiskscount": "1",
    "vmconfigfile": "[datastore1] NURSWGVML011/NURSWGVML011.vmx"
  },
  "timestamp": 1441377902648
}
```

## sw.apm.component

```json
{
  "type": "sw.apm.component",
  "entity": "www.google.com",
  "key": {},
  "tags": {
    "component": "Web_Link_Monitor",
    "componentresponsetime": "0",
    "componentstatus": "Not licensed"
  },
  "timestamp": 1441377900841
}
```