# Collected Microsoft SCOM Properties

* `scom.computer`

```json
{
  "type": "scom.computer",
  "entity": "test",
  "key": {},
  "tags": {
    "activedirectorysite": "Default-First-Site-Name",
    "dnsname": "test.example.org",
    "domaindnsname": "example.org",
    "forestdnsname": "example.org",
    "fullname": "test.example.org",
    "ipaddress": "192.0.2.1, 2001:db8::1, 192.0.2.2, 2001:db8::2",
    "isvirtualmachine": "1",
    "logicalprocessors": "4",
    "netbioscomputername": "test",
    "netbiosdomainname": "example",
    "networkname": "test.example.org",
    "organizationalunit": "CN=Computers,DC=example,DC=org",
    "principalname": "test.example.org"
  },
  "timestamp": 1446653700541
}
```

* `scom.database`

```json
{
  "type": "scom.database",
  "entity": "test",
  "key": {
    "databasename": "cpsdyn"
  },
  "tags": {
    "collation": "Latin1_General_BIN",
    "databaseautogrow": "True",
    "displayname": "cpsdyn",
    "fullname": "test.example.org",
    "instancename": "RTC",
    "logautogrow": "True",
    "owner": "sa",
    "recoverymodel": "SIMPLE",
    "updateability": "READ_WRITE",
    "useraccess": "MULTI_USER"
  },
  "timestamp": 1446653700676
}
```

* `scom.operating_systems`

```json
{
  "type": "scom.operating_system",
  "entity": "test",
  "key": {},
  "tags": {
    "buildnumber": "9200",
    "displayname": "Microsoft Windows Server 2012 Datacenter Evaluation",
    "fullname": "test.example.org",
    "installdate": "11/12/2012 13:53:33",
    "installtype": "Full",
    "logicalprocessors": "4",
    "osversion": "6.2.9200",
    "osversiondisplayname": "Microsoft Windows Server 2012 Datacenter Evaluation",
    "physicalmemory": "4193844",
    "powerplan": "Balanced",
    "producttype": "ServerNT",
    "serialnumber": "00184-40000-00001-AA148",
    "servicepackversion": "0.0",
    "systemdrive": "C:",
    "windowsdirectory": "C:\\Windows"
  },
  "timestamp": 1446653700748
}
```