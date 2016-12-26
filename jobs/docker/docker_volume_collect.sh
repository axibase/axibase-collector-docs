#!/usr/bin/env bash

metric_used=docker.volume.used
metric_used_percent=docker.volume.used_percent
metric_total_used=docker.volume.total_used
metric_total_used_percent=docker.volume.total_used_percent
metric_fs_size=docker.volume.fs.size
docker_volumes_directory=/var/lib/docker/volumes/



#Send network command to atsd by TCP
function send_network_command {
  # echo -e $@ > /dev/tcp/atsd_hostname/8081
  # echo $@ >> ./out.txt
  echo -e $@
}

#Hostname in lower case
function  formatted_hostname {
    echo $(echo $HOSTNAME | awk '{print tolower($0)}');
}

#Send series to atsd host
function send_series {
   local entity=$1
   local metric=$2
   local value=$3
   local datetime=$4
   local hostname=$5
   local command="series e:$entity m:$metric=$value d:${datetime}";
   if [[ ! -z ${hostname} ]]; then
     command=${command}'t:docker-host="'${hostname}'"';
   fi
   send_network_command ${command}
}


#Extract container UID from path to container
function parse_entity () {
   local original_name=$@;
   echo "${original_name/$docker_volumes_directory/}"
}


# Get current date and time in ISO-8601 format
function get_current_iso_time {
   echo $(date -u +"%Y-%m-%dT%H:%M:%SZ")
   exit 1;
}

#Utility method for math operation
function calc() { awk "BEGIN{print $*}"; }


#Retrive files system size where docker containers are placed
function get_docker_file_system_size {
   local file_system_info=$(df -P ${docker_volumes_directory} | tail -1)
   local available=$(echo ${file_system_info} | awk '{print $4}')
   local used=$(echo ${file_system_info} | awk '{print $3}')
   echo $(calc ${available}+${used})
}



#Parse and send information about every container
function send_volume_information {
    #Description of volumes retrieved by du command
    local volumes_info=$(bash -c 'du -s '${docker_volumes_directory}'*')
    #Split information by spaces
    local split_info=(${volumes_info})
    local size=${#split_info[@]}
    local datetime=$(get_current_iso_time)
    local fs_size=$(get_docker_file_system_size)
    local hostname=$(formatted_hostname)
    #Send information about file system size
    send_series ${hostname} ${metric_fs_size} ${fs_size} ${datetime}
    local total_used=0;
    for (( c=0; c<$size; c+=2 ))
    do
        byte_size=${split_info[c]};
        total_used=$(calc ${total_used}+${byte_size});
        entity=$(parse_entity ${split_info[c+1]})

        send_series ${entity} ${metric_used} ${byte_size} ${datetime} ${hostname}

        used_percent=$(calc ${byte_size}/${fs_size}*100);
        send_series ${entity} ${metric_used_percent} ${used_percent} ${datetime} ${hostname}
    done
    #Send information about total containers used memory
    send_series ${hostname} ${metric_total_used} ${total_used} ${datetime}
    send_series ${hostname} ${metric_total_used_percent} $(calc ${total_used}/${fs_size}*100) ${datetime}

}

send_volume_information

