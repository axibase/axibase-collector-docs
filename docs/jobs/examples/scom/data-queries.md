# Microsoft SCOM Data Queries

* Metrics query:

```SQL
SELECT LEFT(tme.NAME+'.', CHARINDEX('.',tme.NAME+'.')-1) AS EntityName,
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(mp.MpName, '.2003', ''), '.2007', ''), '.2008', ''), '.2012', ''), '.Windows.Server', '.Server'), 'Server.AD', 'AD'), 'Microsoft.', ''), '.Monitoring', ''), '.Internal', '') + '.' +
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(pc.ObjectName, ' 2008', ''), '$', '.'), '/', '_'), ' : ', '_'), ' ', '_') + '.' +
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(pc.CounterName, 'I/O', 'IO'), ')', ''), '(', ''), ', ', '_'), '. ', '_'), ' ', '_'), '/', '_') AS MetricName,
  ps.PerfmonInstanceName AS Instance, pdv.SampleValue, pdv.TimeSampled, pdv.TimeAdded
  FROM dbo.PerformanceDataAllView pdv WITH (NOLOCK, NOWAIT)
  INNER JOIN dbo.PerformanceSource ps WITH (NOLOCK, NOWAIT) ON pdv.performancesourceinternalid = ps.performancesourceinternalid
  INNER JOIN dbo.PerformanceCounter pc WITH (NOLOCK, NOWAIT) ON pc.performancecounterid = ps.performancecounterid
  INNER JOIN Rules r WITH (NOLOCK, NOWAIT) ON ps.RuleId = r.RuleId
  INNER JOIN ManagementPack mp WITH (NOLOCK, NOWAIT) ON mp.ManagementPackId = r.ManagementPackId
  INNER JOIN dbo.BaseManagedEntity bme WITH (NOLOCK, NOWAIT) ON ps.BaseManagedEntityId = bme.BaseManagedEntityId
  INNER JOIN dbo.BaseManagedEntity tme WITH (NOLOCK, NOWAIT) ON tme.BaseManagedEntityId = bme.TopLevelHostEntityId
WHERE pdv.TimeAdded > ? ORDER BY pdv.TimeSampled
```

* Properties queries:

```SQL
SELECT LEFT(tme.NAME+'.', CHARINDEX('.',tme.NAME+'.')-1) AS Name,
tme.Name AS FullName,
DisplayName_55270A70_AC47_C853_C617_236B0CFF9B4C AS DisplayName,
Collation_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS Collation,
DatabaseAutogrow_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS DatabaseAutogrow,
DatabaseName_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS DatabaseName,
DatabaseSize_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS DatabaseSize,
DatabaseSizeNumeric_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS DatabaseSizeNumeric,
LogAutogrow_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS LogAutogrow,
LogSize_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS LogSize,
LogSizeNumeric_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS LogSizeNumeric,
Owner_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS Owner,
RecoveryModel_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS RecoveryModel,
Updateability_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS Updateability,
UserAccess_10C1C7F7_BA0F_5F9B_C74A_79A891170934 AS UserAccess,
InstanceName_97408C11_D1C8_5BCE_EF78_74F0473964F3 AS InstanceName
FROM MTV_Database mvi WITH (NOLOCK, NOWAIT)
INNER JOIN BaseManagedEntity bme WITH (NOLOCK, NOWAIT) ON bme.BaseManagedEntityId = mvi.BaseManagedEntityId
INNER JOIN BaseManagedEntity tme WITH (NOLOCK, NOWAIT) ON tme.BaseManagedEntityId = bme.TopLevelHostEntityId
```

```SQL
SELECT LEFT(tme.NAME+'.', CHARINDEX('.',tme.NAME+'.')-1) AS Name,
tme.Name AS FullName,
ActiveDirectoryObjectSid,
ActiveDirectorySite,
DNSName,
DomainDnsName,
ForestDnsName,
IPAddress,
IsVirtualMachine,
LogicalProcessors,
NetbiosComputerName,
NetbiosDomainName,
NetworkName,
OrganizationalUnit,
PrincipalName
FROM MTV_Computer mvi WITH (NOLOCK, NOWAIT)
INNER JOIN BaseManagedEntity bme WITH (NOLOCK, NOWAIT) ON bme.BaseManagedEntityId = mvi.BaseManagedEntityId
INNER JOIN BaseManagedEntity tme WITH (NOLOCK, NOWAIT) ON tme.BaseManagedEntityId = bme.TopLevelHostEntityId
```

```SQL
SELECT LEFT(tme.NAME+'.', CHARINDEX('.',tme.NAME+'.')-1) AS Name,
tme.Name AS FullName,
DisplayName_55270A70_AC47_C853_C617_236B0CFF9B4C AS DisplayName,
OSVersion_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS OSVersion,
SerialNumber_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS SerialNumber,
PhysicalMemory_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS PhysicalMemory,
OSVersionDisplayName_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS OSVersionDisplayName,
LogicalProcessors_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS LogicalProcessors,
SystemDrive_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS SystemDrive,
InstallDate_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS InstallDate,
WindowsDirectory_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS WindowsDirectory,
ServicePackVersion_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS ServicePackVersion,
CSDVersion_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS CSDVersion,
ProductType_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS ProductType,
BuildNumber_66DD9B43_3DC1_3831_95D4_1B03B0A6EA13 AS BuildNumber,
InstallType_CE8B3D0D_530C_D1DD_B9B7_1FE321B33A6D AS InstallType,
PowerPlan_CE8B3D0D_530C_D1DD_B9B7_1FE321B33A6D AS PowerPlan,
InstallType_D96F58D4_4D6E_E538_4736_5639707EF674 AS InstallType,
PowerPlan_2C2DE865_0CD3_A6B8_51A5_3DABF7B48D4E AS PowerPlan
FROM MTV_OperatingSystem mvi WITH (NOLOCK, NOWAIT)
INNER JOIN BaseManagedEntity bme WITH (NOLOCK, NOWAIT) ON bme.BaseManagedEntityId = mvi.BaseManagedEntityId
INNER JOIN BaseManagedEntity tme WITH (NOLOCK, NOWAIT) ON tme.BaseManagedEntityId = bme.TopLevelHostEntityId
```
