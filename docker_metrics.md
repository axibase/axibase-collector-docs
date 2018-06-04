# Docker Metrics

## Collected by [DOCKER Job](./jobs/docker.md)

### Host Metrics

Name | Category | Description
---- | -------- | --------
docker.totalcontainers | System | Total number of containers.
docker.activecontainers | System | Total number of active containers.
docker.stoppedcontainers | System | Total number of stopped containers.
docker.pausedcontainers | System | Total number of paused containers.
docker.totalImages | System | Total number of images.
docker.cpu.sum.avg.usage.host.percent | CPU | Σ `docker.cpu.avg.usage.host.percent` for running containers.
docker.cpu.sum.avg.usage.kernel.percent | CPU | Σ `docker.cpu.avg.usage.kernel.percent` for running containers.
docker.cpu.sum.avg.usage.total.percent | CPU | Σ `docker.cpu.avg.usage.total.percent` for running containers.
docker.cpu.sum.avg.usage.user.percent | CPU | Σ `docker.cpu.avg.usage.user.percent` for running containers.
docker.cpu.sum.host.avg.usage.total.percent | CPU | Σ `docker.cpu.host.avg.usage.total.percent` for running containers.
docker.cpu.sum.throttlingdata.periods | CPU | Σ `docker.cpu.throttlingdata.periods` for running containers.
docker.cpu.sum.throttlingdata.throttledperiods | CPU | Σ `docker.cpu.throttlingdata.throttledperiods` for running containers.
docker.cpu.sum.throttlingdata.throttledtime | CPU | Σ `docker.cpu.throttlingdata.throttledtime` for running containers.
docker.cpu.sum.usage.kernel | CPU | Σ `docker.cpu.usage.kernel` for running containers.
docker.cpu.sum.usage.kernel.percent | CPU | Σ `docker.cpu.usage.kernel.percent` for running containers.
docker.cpu.sum.usage.system | CPU | Σ `docker.cpu.usage.system` for running containers.
docker.cpu.sum.usage.total | CPU | Σ `docker.cpu.usage.total` for running containers.
docker.cpu.sum.usage.total.percent | CPU | Σ `docker.cpu.usage.total.percent` for running containers.
docker.cpu.sum.usage.user | CPU | Σ `docker.cpu.usage.user` for running containers.
docker.cpu.sum.usage.user.percent | CPU | Σ `docker.cpu.usage.user.percent` for running containers.
docker.sum.memory.rss | Memory | Σ `docker.memory.rss` for running containers.
docker.sum.memory.usage | Memory | Σ `docker.memory.usage` for running containers.
docker.sum.diskio.ioservicebytes.read | I/O | Σ `docker.diskio.ioservicebytes.read` for running containers.
docker.sum.diskio.ioservicebytes.write | I/O | Σ `docker.diskio.ioservicebytes.write` for running containers.
docker.fs.running.size.rootfs | File System | The size of the files which have been created or changed for running containers. Σ `docker.fs.size.rootfs` for running containers.
docker.fs.running.size.rw | File System | The total size of all the files for all running containers, in bytes. Σ `docker.fs.size.rw` for running containers.
docker.fs.total.size.rootfs | File System | The size of the files which have been created or changed for all containers. Σ `docker.fs.size.rootfs` for all containers.
docker.fs.total.size.rw | File System | The total size of all the files for all containers, in bytes. Σ `docker.fs.size.rw` for all containers.
docker.data.space_available | File System | Data space available for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.data.space_used | File System | Data space used for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.data.space_used_percent | File System | Percentage of data space used for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.data.space_total | File System | Data space total for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.metadata.space_available | File System | Metadata space available for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.metadata.space_used | File System| Metadata space used for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.metadata.space_used_percent | File System | Percentage of metadata space used for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.
docker.metadata.space_total | File System | Metadata space total for the [Device Mapper](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/) storage driver.

### Container Metrics

Name | Category | Description
---- | -------- | --------
docker.cpu.usage.system | CPU | Total CPU consumed by container in kernel mode in nanoseconds.
docker.cpu.usage.user | CPU | Total CPU consumed by tasks of the cgroup in user mode in nanoseconds.
docker.cpu.usage.user.percent | CPU | Percentage of CPU consumed by tasks in user mode.
docker.cpu.usage.total | CPU | Total CPU consumed by tasks of the cgroup in nanoseconds.
docker.cpu.usage.total.percent | CPU | Percentage of CPU consumed by tasks.
docker.cpu.usage.kernel | CPU | Total CPU consumed by tasks of the cgroup in kernel mode in nanoseconds.
docker.cpu.usage.kernel.percent | CPU | Percentage of CPU consumed by tasks in kernel mode.
docker.cpu.usage.percpu | CPU | Total CPU time consumed per core.
docker.cpu.throttlingdata.periods | CPU | The number of periods with throttling active.
docker.cpu.throttlingdata.throttledperiods | CPU | The number of periods when the container hit its throttling limit.
docker.cpu.throttlingdata.throttledtime | CPU | Total time that a container's CPU usage was throttled.
docker.cpu.avg.usage.total.percent | CPU | The average value of `docker.cpu.usage.total.percent`.
docker.cpu.avg.usage.allocated.percent | CPU | The avarage value `docker.cpu.usage.total.percent` for allocated CPU core.
docker.cpu.avg.usage.host.percent | CPU | The avarage value of `docker.cpu.usage.total.percent` for CPU core.
docker.cpu.avg.usage.kernel.percent | CPU | The average value for `docker.cpu.usage.kernel.percent`.
docker.cpu.avg.usage.user.percent | CPU | The average value for `docker.cpu.usage.user.percent`.
docker.memory.activeanon | Memory | The number of bytes of active memory backed by anonymous pages, excluding sub-cgroups.
docker.memory.activefile | Memory | The number of bytes of active memory backed by files, excluding sub-cgroups.
docker.memory.cache | Memory | The number of bytes used for the cache, excluding sub-cgroups.
docker.memory.failcnt | Memory | The number of times the container hit its memory limit.
docker.memory.hierarchical.memorylimit | Memory |  The memory limit for the hierarchy that contains the memory cgroup, in bytes.
docker.memory.hierarchical.memswlimit | Memory | The memory plus swap limit for the hierarchy that contains the memory cgroup, in bytes.
docker.memory.inactiveanon | Memory | The number of bytes of inactive memory in anonymous pages, excluding sub-cgroups.
docker.memory.inactivefile | Memory | The number of bytes of inactive memory in file pages, excluding sub-cgroups.
docker.memory.limit | Memory | The memory limit for the container in bytes.
docker.memory.mappedfile | Memory | The number of bytes of mapped files, excluding sub-groups.
docker.memory.maxusage | Memory | The max amount of memory used by container in bytes.
docker.memory.percent | Memory | Percentage of memory used.
docker.memory.pgfault | Memory | The total number of page faults, excluding sub-cgroups.
docker.memory.pgmajfault | Memory | The number of major page faults, excluding sub-cgroups.
docker.memory.pgpgin | Memory | The number of charging events, excluding sub-cgroups.
docker.memory.pgpgout | Memory | The number of uncharging events, excluding sub-groups.
docker.memory.rss | Memory | The number of bytes of anonymous and swap cache memory (includes transparent hugepages), excluding sub-cgroups.
docker.memory.rsshuge | Memory | The number of bytes of anonymous transparent hugepages, excluding sub-cgroups.
docker.memory.unevictable | Memory | The number of bytes of memory that cannot be reclaimed (mlocked etc), excluding sub-cgroups.
docker.memory.usage | Memory | The current number of bytes used for memory including cache.
docker.memory.swap | Memory | The amount of swap currently used by the processes, excluding sub-groups.
docker.memory.writeback | Memory | The number of bytes being written back to disk, excluding sub-cgroups.
docker.memory.total.activeanon | Memory | The number of bytes of active memory backed by anonymous pages, including sub-cgroups.
docker.memory.total.activefile | Memory | The number of bytes of active memory backed by files, including sub-cgroups.
docker.memory.total.cache | Memory | The number of bytes used for the cache, including sub-cgroups.
docker.memory.total.inactiveanon | Memory | The number of bytes of inactive memory in anonymous pages, including sub-cgroups.
docker.memory.total.inactivefile | Memory |The number of bytes of inactive memory in file pages, including sub-cgroups.
docker.memory.total.mappedfile | Memory | The number of bytes of mapped files, including sub-groups.
docker.memory.total.pgfault | Memory | The total number of page faults, including sub-cgroups.
docker.memory.total.pgmajfault | Memory | The number of major page faults, including sub-cgroups.
docker.memory.total.pgpgin | Memory | The number of charging events, including sub-cgroups.
docker.memory.total.pgpgout | Memory | The number of uncharging events, including sub-groups.
docker.memory.total.rss | Memory | The number of bytes of anonymous and swap cache memory (includes transparent hugepages), including sub-cgroups.
docker.memory.total.rsshuge | Memory | The number of bytes of anonymous transparent hugepages, including sub-cgroups.
docker.memory.total.swap | Memory | The amount of swap currently used by the processes, including sub-groups.
docker.memory.total.unevictable | Memory | The number of bytes of memory that cannot be reclaimed (mlocked etc), including sub-cgroups.
docker.memory.total.writeback | Memory | The number of bytes being written back to disk, including sub-cgroups.
docker.network.rx | Network | The number of bytes received by all network interfaces.
docker.network.rx_sec | Network | The number of bytes received by all network interfaces per second.
docker.network.rxbytes | Network | Total received bytes on the network interface.
docker.network.rxdropped | Network | Total receive packets dropped on the network interface.
docker.network.rxerrors | Network | Total receive errors on the network interface.
docker.network.rxpackets | Network | Total received packets on the network interface.
docker.network.tx | Network | The number of bytes transmitted by all network interfaces.
docker.network.tx_sec | Network | The number of bytes transmitted by all network interfaces per second.
docker.network.txbytes | Network | Total transmitted bytes on the network interface.
docker.network.txdropped | Network | Total transmitted packets dropped on the network interface.
docker.network.txerrors | Network | Total transmission errors on the network interface.
docker.network.txpackets | Network | Total packets transmitted on the network interface.
docker.diskio.iomerged.* | I/O | The number of BIOS requests merged into requests for I/O operations by a cgroup. Entries have two fields: number and operation. Number is the number of requests, and operation represents the type of operation (read, write, sync, or async).
docker.diskio.ioqueue.* | I/O |  The number of requests queued for I/O operations by a cgroup. Entries have two fields: number and operation. Number is the number of requests, and operation represents the type of operation (read, write, sync, or async). If the cgroup isn’t doing any I/O, this will be zero.
docker.diskio.ioservicebytes.* | I/O | The number of bytes transferred to or from specific devices by a cgroup as seen by the CFQ scheduler. Entries have four fields: major, minor, operation, and bytes. Major and minor are device types and node numbers specified in Linux Allocated Devices, operation represents the type of operation (read, write, sync, or async) and bytes is the number of transferred bytes.
docker.diskio.ioservicebytes.async | I/O |
docker.diskio.ioservicebytes.blockread | I/O |
docker.diskio.ioservicebytes.blockread_sec | I/O |
docker.diskio.ioservicebytes.blockwrite | I/O |
docker.diskio.ioservicebytes.blockwrite_sec | I/O |
docker.diskio.ioservicebytes.read | I/O |
docker.diskio.ioservicebytes.sync | I/O |
docker.diskio.ioservicebytes.total | I/O |
docker.diskio.ioservicebytes.write | I/O |
docker.diskio.ioservicetime.* | I/O | The total time between request dispatch and request completion for I/O operations on specific devices by a cgroup as seen by the CFQ scheduler. Entries have four fields: major, minor, operation, and time. Major and minor are device types and node numbers specified in Linux Allocated Devices, operation represents the type of operation (read, write, sync, or async) and time is the length of time in nanoseconds (ns). The time is reported in nanoseconds rather than a larger unit so that this report is meaningful even for solid-state devices.
docker.diskio.ioserviced.* | I/O | The number of I/O operations performed on specific devices by a cgroup as seen by the CFQ scheduler. Entries have four fields: major, minor, operation, and number. Major and minor are device types and node numbers specified in Linux Allocated Devices, operation represents the type of operation (read, write, sync, or async) and number represents the number of operations.
docker.diskio.ioserviced.async | I/O |
docker.diskio.ioserviced.read | I/O |
docker.diskio.ioserviced.sync | I/O |
docker.diskio.ioserviced.total | I/O |
docker.diskio.ioserviced.write | I/O |
docker.diskio.iotime.* | I/O | The total time between request dispatch and request completion for I/O operations on specific devices by a cgroup as seen by the CFQ scheduler. Entries have four fields: major, minor, operation, and time. Major and minor are device types and node numbers specified in Linux Allocated Devices, operation represents the type of operation (read, write, sync, or async) and time is the length of time in nanoseconds (ns). The time is reported in nanoseconds rather than a larger unit so that this report is meaningful even for solid-state devices.
docker.diskio.iowaittime.* | I/O | The total time I/O operations on specific devices by a cgroup spent waiting for service in the scheduler queues. When you interpret this report, note: * the time reported can be greater than the total time elapsed, because the time reported is the cumulative total of all I/O operations for the cgroup rather than the time that the cgroup itself spent waiting for I/O operations. To find the time that the group as a whole has spent waiting, use the blkio.group_wait_time parameter.* if the device has a queue_depth > 1, the time reported only includes the time until the request is dispatched to the device, not any time spent waiting for service while the device reorders requests.Entries have four fields: major, minor, operation, and time. Major and minor are device types and node numbers specified in Linux Allocated Devices, operation represents the type of operation (read, write, sync, or async) and time is the length of time in nanoseconds (ns). The time is reported in nanoseconds rather than a larger unit so that this report is meaningful even for solid-state devices.
docker.diskio.sectors.* | I/O | The number of 512-bytes sectors read and written by the processes member of the cgroup, device by device. Reads and writes are merged in a single counter.
docker.fs.size.rw | File System | The total size of all the files in the container, in bytes. If you were to export the filesystem of the container as a tarball, it would be about that size.
docker.fs.size.rootfs | File System | The size of the files which have been created or changed, if you compare the container to its base image. Just after creation, this should be zero; as you modify (or create) files, this will increase.
docker.process.all | Process | The number of all processes for running container.
docker.process.filtered | Process | The number of all processed which have been filtered by [field 'Excluded Processes'](./jobs/docker.md#job-settings) for running conteiner.
docker.pids.current | Process | The number of pids in the cgroup (Linux specific stats, not populated on Windows.)
docker.pids.limit | Process | The hard limit on the number of pids in the cgroup. A "Limit" of 0 means that there is no limit. (Linux specific stats, not populated on Windows.)
docker.storage.read.count.normalized | I/O | The disk stats on Windows.
docker.storage.read.size | I/O | The disk stats on Windows.
docker.storage.write.count.normalized | I/O | The disk stats on Windows.
docker.storage.write.size | I/O | The disk stats on Windows.

### Collected by [TCP Job](./jobs/tcp.md)

### TCP Job Container Metrics

Name | Category | Description
---- | -------- | --------
docker.tcp-connect-status | Network | Connection status for the container port.
docker.tcp-connect-time | Network | Number of milliseconds spent on opening the connection to the container port.

### Collected by [SCRIPT](./jobs/docker/volume-size.md)

### Volume Metrics

Name | Category | Description
---- | -------- | --------
docker.volume.fs.size | File System | Total size (used + available, in bytes) of the file system where the /var/lib/docker directory is located. Collected for the entire docker host.
docker.volume.total_used | File System | Total space (in bytes) used by the /var/lib/docker directory. Collected for the entire docker host.
docker.volume.total_used_percent | File System | Percentage of space used by the /var/lib/docker directory in the file system where the /var/lib/docker directory is located. Calculated as docker.volume.total_used/docker.volume.fs.size * 100. Collected for the entire docker host.
docker.volume.used | File System | Space used by all files in the given volume (in bytes).
docker.volume.used_percent | File System | Space used by files in the given volume as percentage of the total size of the file system where the /var/lib/docker directory is located. Calculated as docker.volume.used/docker.volume.fs.size * 100.
