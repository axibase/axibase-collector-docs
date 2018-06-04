# SolarWinds Data Queries

## SolarWinds Base Queries

* Metrics Queries select the most recent statistics:

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, V.Caption AS Name,
T.DateTime, T.DiskSize, T.AvgDiskUsed, T.PercentDiskUsed
FROM VolumeUsage T, Nodes N, Volumes V
WHERE T.NodeID = N.NodeID AND T.VolumeID = V.VolumeID AND V.NodeID = T.NodeID AND VolumeTypeID IN (4, 10)
AND T.DateTime > ? AND V.VolumeSize > 0
ORDER BY T.DateTime
```

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, V.Caption AS Name,
T.DateTime, T.AvgDiskQueueLength, T.AvgDiskTransfer, T.AvgDiskReads, T.AvgDiskWrites
FROM VolumePerformance T, Nodes N, Volumes V
WHERE T.NodeID = N.NodeID AND T.VolumeID = V.VolumeID AND V.NodeID = T.NodeID
AND VolumeTypeID IN (4, 10) AND V.VolumeSize > 0 AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, T.DateTime, T.AvgResponseTime, T.PercentLoss
FROM ResponseTime T, Nodes N
WHERE T.NodeID = N.NodeID AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, I.InterfaceName AS Name,
T.DateTime, T.In_Averagebps, T.In_TotalBytes, T.In_TotalPkts, T.In_AvgUniCastPkts, T.In_AvgMultiCastPkts,
T.Out_Averagebps, T.Out_TotalBytes, T.Out_TotalPkts, T.Out_AvgUniCastPkts, T.Out_AvgMultiCastPkts
FROM InterfaceTraffic T, Nodes N, Interfaces I
WHERE T.NodeID = N.NodeID AND T.InterfaceID = I.InterfaceID AND I.NodeID = T.NodeID AND I.InterfaceType != 24 AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL

SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, I.InterfaceName AS Name,
T.DateTime, T.In_Discards, T.In_Errors, T.Out_Discards, T.Out_Errors
FROM InterfaceErrors T, Nodes N, Interfaces I
WHERE T.NodeID = N.NodeID AND T.InterfaceID = I.InterfaceID AND I.NodeID = T.NodeID AND InterfaceType != 24 AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS SysName, T.*
FROM CPULoad T, Nodes N
WHERE T.NodeID = N.NodeID   AND T.DateTime > ?
ORDER BY T.DateTime
```

* Properties Query selects current properties:

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS ValidSysName, ObjectSubType,
IP_Address, IP_Address_Type,
DynamicIP, UnManaged, Caption, DNS, SysName, Vendor, Description, IOSVersion,
StatusDescription, Status, MachineType, IsServer,
Severity, TotalMemory, LastBoot, SystemUpTime, ResponseTime, PercentLoss,
AvgResponseTime, MinResponseTime, MaxResponseTime,
CPULoad, MemoryUsed, PercentMemoryUsed FROM Nodes N
```

## SolarWinds VMware Queries

* Metrics Queries select the most recent statistics:

```SQL
LECT N.HostName AS Name, C.Name AS Cluster, T.*
FROM VIM_HostStatistics T, VIM_Hosts N, VIM_Clusters C
WHERE T.HostID = N.HostID AND N.ClusterID = C.ClusterID AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT N.Name, T.*
FROM VIM_DataStoreStatistics T, VIM_DataStores N
WHERE T.DataStoreID = N.DataStoreID AND N.Capacity > 0 AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT REPLACE(N.Name, ' ', '_') AS Name, H.HostName AS Host, C.Name AS Cluster, T.*
FROM VIM_VMStatistics T, VIM_VirtualMachines N, VIM_Hosts H, VIM_Clusters C
WHERE T.VirtualMachineID = N.VirtualMachineID AND N.HostID = H.HostID
AND H.ClusterID = C.ClusterID AND N.ManagedStatus = 1 AND T.DateTime > ?
ORDER BY T.DateTime
```

```SQL
SELECT N.Name, T.*
FROM VIM_ClusterStatistics T, VIM_Clusters N
WHERE T.ClusterID = N.ClusterID
AND N.TotalMemory > 0 AND T.DateTime > ?
ORDER BY T.DateTime
```

* Properties Query selects current properties:

```SQL
SELECT LOWER(REPLACE(N.Name, ' ', '_')) AS Name, N.DataStoreIdentifier, N.Type, N.URL, N.Accessible,
N.ManagedStatus, N.Capacity, N.FreeSpace,
N.ProvisionedSpace, N.IOPSTotal, N.IOPSRead, N.IOPSWrite, N.LatencyTotal, N.LatencyRead, N.LatencyWrite,
N.DepletionDate, N.Platform, N.ClusterCount, N.Local
FROM VIM_DataStores N* Metrics Queries select most recent statistics
```

```SQL
SELECT LOWER(REPLACE(N.Name, ' ', '_')) AS VmName, N.Name, LOWER(H.HostName) AS Host,
LOWER(REPLACE(C.Name, ' ', '_')) AS Cluster,
N.UUID,N.ManagedObjectID,N.VMConfigFile,N.MemoryConfigured,N.MemoryShares,N.CPUShares,N.GuestState,
N.IPAddress, N.LogDirectory, N.GuestVmWareToolsVersion, N.GuestVmWareToolsStatus,
N.GuestName, N.GuestFamily, N.GuestDnsName, N.NicCount, N.VDisksCount, N.ProcessorCount, N.PowerState, N.BootTime,
N.ConfigStatus, N.OverallStatus, N.ManagedStatus, N.NetworkUsageRate, N.NetworkTransmitRate, N.NetworkReceiveRate,
N.CpuLoad, N.CpuUsageMHz, N.MemUsage, N.MemUsageMB, N.TriggeredAlarmDescription, N.IsLicensed, N.RelativePath,
N.DatastoreIdentifier, N.IdentityModifyCount, N.CpuReady, N.SwappedMemoryUtilization, N.BalloonMemload,
N.IOPSTotal, N.IOPSRead, N.IOPSWrite, N.LatencyTotal, N.LatencyRead,
N.LatencyWrite, N.SnapshotStorageSize, N.ConsumedMemLoad,
N.ConsumedPercentMemLoad, N.LastActivityDate, N.TotalStorageSize,
N.TotalStorageSizeUsed, N.VolumeSummaryCapacity, N.VolumeSummaryFreeSpace,
N.VolumeSummaryCapacityDepletionDate, N.DynamicMemoryEnabled,
N.CpuCostop, N.SnapshotSummaryCount, N.DateCreated, N.OldestSnapshotDate,
N.HeartBeat, N.SnapshotDateModified, N.MemoryAllocationLimit, N.VirtualDiskDateModified
FROM VIM_VirtualMachines N, VIM_Hosts H, VIM_Clusters C WHERE N.HostID = H.HostID AND H.ClusterID = C.ClusterID

```

```SQL
SELECT LOWER(N.HostName) AS ESXHostName, HostName,
LOWER(REPLACE(C.Name, ' ', '_')) AS Cluster, N.ManagedObjectID, N.VMwareProductName, N.VMwareProductVersion,
N.PollingMethod,N.Model,N.Vendor,N.ProcessorType,N.CpuCoreCount,N.CpuPkgCount,N.CpuMhz,N.NicCount,
N.HbaCount,N.HbaFcCount,N.HbaScsiCount,N.HbaIscsiCount,N.MemorySize,N.BuildNumber,N.BiosSerial,
N.IPAddress,N.ConnectionState,N.ConfigStatus,N.OverallStatus,N.ManagedStatus,
N.ManagedStatusMessage,N.NetworkUtilization,N.NetworkUsageRate,N.NetworkTransmitRate,
N.NetworkReceiveRate,N.NetworkCapacityKbps,
N.CpuLoad,N.CpuUsageMHz,N.MemUsage,N.MemUsageMB,N.VmCount,N.VmRunningCount,
N.TriggeredAlarmDescription,N.BootTime,N.DateCreated,N.TotalLatency
FROM VIM_Hosts N, VIM_Clusters C WHERE N.ClusterID = C.ClusterID
```

```SQL
SELECT LOWER(REPLACE(Name, ' ', '_')) AS ClusterName, Name, ManagedObjectID,
TotalMemory, TotalCpu, CpuCoreCount, CpuThreadCount, EffectiveCpu, EffectiveMemory,
DrsBehaviour, DrsStatus, DrsVmotionRate, HaAdmissionControlStatus, HaStatus,
HaFailoverLevel, ConfigStatus, OverallStatus, ManagedStatus,
CPULoad, CPUUsageMHz, MemoryUsage, MemoryUsageMB, TriggeredAlarmDescription,
VmCapacityCount, VmCapacityConstraint, DiskUtilizationDepletionDate,
DatastoreUsedSpace, CpuUtilizationDepletionDate, MemoryUtilizationDepletionDate FROM VIM_Clusters
```

## SolarWinds AMP Queries

* Metrics Queries select the most recent statistics:

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS Name,
REPLACE(C.Name, ' ', '_') AS Component, DateTime, R.ResponseTime, R.ComponentAvailability
FROM APM_Component C, APM_Application A, Nodes N, APM_ResponseTime R
WHERE R.ComponentID = C.ID AND C.ApplicationID = A.ID AND A.NodeID = N.NodeID
AND ISNULL(C.IsDisabled, 0) != 1 AND DateTime > ?
ORDER BY DateTime
```

* Properties Query selects current properties:

```SQL
SELECT REPLACE(ISNULL(NULLIF(N.SysName, ''), N.Caption), ' ', '_') AS Name,
REPLACE(C.ComponentName, ' ', '_') AS Component, C.ComponentStatus, C.ComponentResponseTime
FROM APM_AlertsData C, APM_Application A, Nodes N
WHERE C.ApplicationID = A.ID AND A.NodeID = N.NodeID
```
