# Collected Microsoft SCOM Properties

* `scom.computer`

```json
{
  "type": "scom.computer",
  "entity": "2013-lync-fe",
  "key": {},
  "tags": {
    "activedirectorysite": "Default-First-Site-Name",
    "dnsname": "2013-LYNC-FE.Contoso.com",
    "domaindnsname": "Contoso.com",
    "forestdnsname": "Contoso.com",
    "fullname": "2013-LYNC-FE.Contoso.com",
    "ipaddress": "192.0.2.1, 2001:db8::1, 192.0.2.2, 2001:db8::2",
    "isvirtualmachine": "1",
    "logicalprocessors": "4",
    "netbioscomputername": "2013-LYNC-FE",
    "netbiosdomainname": "Contoso",
    "networkname": "2013-LYNC-FE.Contoso.com",
    "organizationalunit": "CN=Computers,DC=Contoso,DC=com",
    "principalname": "2013-LYNC-FE.Contoso.com"
  },
  "timestamp": 1446653700541
}
```

* `scom.database`

```json
{
  "type": "scom.database",
  "entity": "2013-lync-fe",
  "key": {
    "databasename": "cpsdyn"
  },
  "tags": {
    "collation": "Latin1_General_BIN",
    "databaseautogrow": "True",
    "displayname": "cpsdyn",
    "fullname": "2013-LYNC-FE.Contoso.com",
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
  "entity": "2013-lync-fe",
  "key": {},
  "tags": {
    "buildnumber": "9200",
    "displayname": "Microsoft Windows Server 2012 Datacenter Evaluation",
    "fullname": "2013-LYNC-FE.Contoso.com",
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