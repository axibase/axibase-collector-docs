# Collected VMware Properties

## vmware.cluster

```json

{
    "type": "vmware.cluster",
    "entity": "nurcls01",
    "key": {},
    "tags": {
      "allocated_cpu": "0",
      "allocated_mem": "0",
      "allocated_vm_cpu": "0",
      "allocated_vm_mem": "0",
      "available_pool_cpu": "17143",
      "available_pool_mem": "22304260096",
      "available_vm_cpu": "17143",
      "available_vm_mem": "22304260096",
      "current_cpu": "0",
      "current_mem": "0",
      "overall_status": "green"
    },
    "timestamp": 1451138406320
}
```

## vmware.cluster.hosts

```json
{
    "type": "vmware.cluster.hosts",
    "entity": "nurcls02",
    "key": {
      "host": "nuresx002"
    },
    "tags": {
      "cpu_core_count": "4",
      "cpu_count": "1",
      "cpu_hz": "2659999643",
      "cpu_thread_count": "8",
      "host": "nuresx002",
      "mem_size": "51530223616",
      "total_cpu_mhz": "10639"
    },
    "timestamp": 1463409915809
}
```

## vmware.cluster.vms

```json
{
    "type": "vmware.cluster.vms",
    "entity": "nurcls02",
    "key": {
      "vm": "nurswgvml009 (1)"
    },
    "tags": {
      "description": "10.102.0.8 Oracle EM",
      "host": "nuresx003",
      "mem_size_mb": "6144",
      "num_vcpu": "2",
      "power_state": "On",
      "vm": "NURSWGVML009 (1)"
    },
    "timestamp": 1434348902340
}
```

## vmware.host

```json
{
    "type": "vmware.host",
    "entity": "nuresx002",
    "key": {},
    "tags": {
      "boot_time": "2015-06-04 07:55:11.773",
      "cpu_core_count": "4",
      "cpu_count": "1",
      "cpu_hz": "2659999643",
      "cpu_model": "Intel(R) Core(TM) i7 CPU         920  @ 2.67GHz",
      "cpu_power_mgmt_policy": "Balanced",
      "cpu_power_mgmt_support": "Enhanced Intel SpeedStep(R)",
      "cpu_thread_count": "8",
      "dns_name": "nuresx002",
      "enabled": "1",
      "hba_count": "4",
      "host_key": "52d42485-687c-da1d-1f03-31aaed31e399",
      "host_model": "MS-7522",
      "host_vendor": "MSI",
      "ip_address": "188.40.115.149",
      "local_ip_address": "10.102.0.7",
      "mem_size": "51530223616",
      "mmode": "NO",
      "name": "nuresx002",
      "nic_count": "2",
      "password_last_upd_dt": "2016-04-29 15:41:35.52",
      "port": "443",
      "power_state": "Off",
      "product_api_type": "HostAgent",
      "product_api_version": "5.1",
      "product_build": "1065491",
      "product_fullname": "VMware ESXi 5.1.0 build-1065491",
      "product_name": "VMware ESXi",
      "product_os_type": "vmnix-x86",
      "product_vendor": "VMware, Inc.",
      "product_version": "5.1.0",
      "username": "vpxuser",
      "uuid_bios": "00000000-0000-0000-0000-00242129ebce",
      "vmotion_enabled": "0"
    },
    "timestamp": 1463411019043
}
```

## vmware.host.vms

```json
{
      "type": "vmware.host.vms",
      "entity": "nuresx002",
      "key": {
        "vm": "nurswgvml003"
      },
      "tags": {
        "cluster": "NURCLS02",
        "description": "10.102.0.2 Shared NFS/CIFS disk, ntp server",
        "mem_size_mb": "512",
        "num_vcpu": "1",
        "power_state": "On",
        "vm": "NURSWGVML003"
      },
      "timestamp": 1451288718347
}
```

## vmware.vm

```json
{
    "type": "vmware.vm",
    "entity": "atsd1",
    "key": {},
    "tags": {
      "guest_state": "unknown",
      "is_template": "0",
      "memory_overhead": "0",
      "name": "ATSD1",
      "power_state": "Off"
    },
    "timestamp": 1446733800850
}
```