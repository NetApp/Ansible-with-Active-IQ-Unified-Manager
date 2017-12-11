#============================================================
#
#
# Copyright (c) 2017 NetApp, Inc. All rights reserved.
# Specifications subject to change without notice.
#
# This sample code is provided AS IS, with no support or
# warranties of any kind, including but not limited to
# warranties of merchantability or fitness of any kind,
# expressed or implied.
#
# Min Python Version = python 2.7
#
#============================================================


#!/usr/bin/python

from ansible.module_utils.basic import *

import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")


def get():
    url_path        = "/api/1.0/slo/"

    flag=0

    url_path+="data-protection-nodes"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if resource_type != None:
        if flag is 0:
            url_path+="?resource_type="+resource_type
            flag=1
        else:
            url_path+="&resource_type="+resource_type
    if primary_resource_key != None:
        if flag is 0:
            url_path+="?primary_resource_key="+primary_resource_key
            flag=1
        else:
            url_path+="&primary_resource_key="+primary_resource_key
    if primary_resource_type != None:
        if flag is 0:
            url_path+="?primary_resource_type="+primary_resource_type
            flag=1
        else:
            url_path+="&primary_resource_type="+primary_resource_type
    if protection_service_level_key != None:
        if flag is 0:
            url_path+="?protection_service_level_key="+protection_service_level_key
            flag=1
        else:
            url_path+="&protection_service_level_key="+protection_service_level_key
    if restore_source_node_name != None:
        if flag is 0:
            url_path+="?restore_source_node_name="+restore_source_node_name
            flag=1
        else:
            url_path+="&restore_source_node_name="+restore_source_node_name
    if restore_source_files != None:
        if flag is 0:
            url_path+="?restore_source_files="+restore_source_files
            flag=1
        else:
            url_path+="&restore_source_files="+restore_source_files
    if restore_file_count != None:
        if flag is 0:
            url_path+="?restore_file_count="+restore_file_count
            flag=1
        else:
            url_path+="&restore_file_count="+restore_file_count
    if node_name != None:
        if flag is 0:
            url_path+="?node_name="+node_name
            flag=1
        else:
            url_path+="&node_name="+node_name
    if source_node_name != None:
        if flag is 0:
            url_path+="?source_node_name="+source_node_name
            flag=1
        else:
            url_path+="&source_node_name="+source_node_name
    if lag_time != None:
        if flag is 0:
            url_path+="?lag_time="+lag_time
            flag=1
        else:
            url_path+="&lag_time="+lag_time
    if protection_relationship_status != None:
        if flag is 0:
            url_path+="?protection_relationship_status="+protection_relationship_status
            flag=1
        else:
            url_path+="&protection_relationship_status="+protection_relationship_status
    if protection_relationship_state != None:
        if flag is 0:
            url_path+="?protection_relationship_state="+protection_relationship_state
            flag=1
        else:
            url_path+="&protection_relationship_state="+protection_relationship_state
    if total_bytes_transferred != None:
        if flag is 0:
            url_path+="?total_bytes_transferred="+total_bytes_transferred
            flag=1
        else:
            url_path+="&total_bytes_transferred="+total_bytes_transferred
    if current_transfer_type != None:
        if flag is 0:
            url_path+="?current_transfer_type="+current_transfer_type
            flag=1
        else:
            url_path+="&current_transfer_type="+current_transfer_type
    if current_snapshot_progress != None:
        if flag is 0:
            url_path+="?current_snapshot_progress="+current_snapshot_progress
            flag=1
        else:
            url_path+="&current_snapshot_progress="+current_snapshot_progress
    if current_transfer_error != None:
        if flag is 0:
            url_path+="?current_transfer_error="+current_transfer_error
            flag=1
        else:
            url_path+="&current_transfer_error="+current_transfer_error
    if current_transfer_snapshot_key != None:
        if flag is 0:
            url_path+="?current_transfer_snapshot_key="+current_transfer_snapshot_key
            flag=1
        else:
            url_path+="&current_transfer_snapshot_key="+current_transfer_snapshot_key
    if last_snapshot_key != None:
        if flag is 0:
            url_path+="?last_snapshot_key="+last_snapshot_key
            flag=1
        else:
            url_path+="&last_snapshot_key="+last_snapshot_key
    if last_snapshot_timestamp != None:
        if flag is 0:
            url_path+="?last_snapshot_timestamp="+last_snapshot_timestamp
            flag=1
        else:
            url_path+="&last_snapshot_timestamp="+last_snapshot_timestamp
    if last_transfer_error != None:
        if flag is 0:
            url_path+="?last_transfer_error="+last_transfer_error
            flag=1
        else:
            url_path+="&last_transfer_error="+last_transfer_error
    if last_transfer_type != None:
        if flag is 0:
            url_path+="?last_transfer_type="+last_transfer_type
            flag=1
        else:
            url_path+="&last_transfer_type="+last_transfer_type
    if last_transfer_duration != None:
        if flag is 0:
            url_path+="?last_transfer_duration="+last_transfer_duration
            flag=1
        else:
            url_path+="&last_transfer_duration="+last_transfer_duration
    if last_transfer_end_timestamp != None:
        if flag is 0:
            url_path+="?last_transfer_end_timestamp="+last_transfer_end_timestamp
            flag=1
        else:
            url_path+="&last_transfer_end_timestamp="+last_transfer_end_timestamp
    if last_transfer_size != None:
        if flag is 0:
            url_path+="?last_transfer_size="+last_transfer_size
            flag=1
        else:
            url_path+="&last_transfer_size="+last_transfer_size
    if storage_platform_protection_relationship_key != None:
        if flag is 0:
            url_path+="?storage_platform_protection_relationship_key="+storage_platform_protection_relationship_key
            flag=1
        else:
            url_path+="&storage_platform_protection_relationship_key="+storage_platform_protection_relationship_key
    if storage_platform_protection_relationship_type != None:
        if flag is 0:
            url_path+="?storage_platform_protection_relationship_type="+storage_platform_protection_relationship_type
            flag=1
        else:
            url_path+="&storage_platform_protection_relationship_type="+storage_platform_protection_relationship_type
    if storage_platform_type != None:
        if flag is 0:
            url_path+="?storage_platform_type="+storage_platform_type
            flag=1
        else:
            url_path+="&storage_platform_type="+storage_platform_type
    if file_share_key != None:
        if flag is 0:
            url_path+="?file_share_key="+file_share_key
            flag=1
        else:
            url_path+="&file_share_key="+file_share_key
    if is_healthy != None:
        if flag is 0:
            url_path+="?is_healthy="+is_healthy
            flag=1
        else:
            url_path+="&is_healthy="+is_healthy
    if unhealthy_reason != None:
        if flag is 0:
            url_path+="?unhealthy_reason="+unhealthy_reason
            flag=1
        else:
            url_path+="&unhealthy_reason="+unhealthy_reason
    if sortBy != None:
        if flag is 0:
            url_path+="?sortBy="+sortBy
            flag=1
        else:
            url_path+="&sortBy="+sortBy
    if maxRecords != None:
        if flag is 0:
            url_path+="?maxRecords="+maxRecords
            flag=1
        else:
            url_path+="&maxRecords="+maxRecords
    if nextTag != None:
        if flag is 0:
            url_path+="?nextTag="+nextTag
            flag=1
        else:
            url_path+="&nextTag="+nextTag
    response=http_request_for_get(url_path)
    json_response=response.json()
    return json_response

def post():
    url_path        = "/api/1.0/slo/"
    url_path+="data-protection-nodes"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (resource_type != None) & (resource_type != key):
        payload['resource_type']=resource_type
    if (primary_resource_key != None) & (primary_resource_key != key):
        payload['primary_resource_key']=primary_resource_key
    if (primary_resource_type != None) & (primary_resource_type != key):
        payload['primary_resource_type']=primary_resource_type
    if (protection_service_level_key != None) & (protection_service_level_key != key):
        payload['protection_service_level_key']=protection_service_level_key
    if (restore_source_node_name != None) & (restore_source_node_name != key):
        payload['restore_source_node_name']=restore_source_node_name
    if (restore_source_files != None) & (restore_source_files != key):
        payload['restore_source_files']=restore_source_files
    if (restore_file_count != None) & (restore_file_count != key):
        payload['restore_file_count']=restore_file_count
    if (node_name != None) & (node_name != key):
        payload['node_name']=node_name
    if (source_node_name != None) & (source_node_name != key):
        payload['source_node_name']=source_node_name
    if (lag_time != None) & (lag_time != key):
        payload['lag_time']=lag_time
    if (protection_relationship_status != None) & (protection_relationship_status != key):
        payload['protection_relationship_status']=protection_relationship_status
    if (protection_relationship_state != None) & (protection_relationship_state != key):
        payload['protection_relationship_state']=protection_relationship_state
    if (total_bytes_transferred != None) & (total_bytes_transferred != key):
        payload['total_bytes_transferred']=total_bytes_transferred
    if (current_transfer_type != None) & (current_transfer_type != key):
        payload['current_transfer_type']=current_transfer_type
    if (current_snapshot_progress != None) & (current_snapshot_progress != key):
        payload['current_snapshot_progress']=current_snapshot_progress
    if (current_transfer_error != None) & (current_transfer_error != key):
        payload['current_transfer_error']=current_transfer_error
    if (current_transfer_snapshot_key != None) & (current_transfer_snapshot_key != key):
        payload['current_transfer_snapshot_key']=current_transfer_snapshot_key
    if (last_snapshot_key != None) & (last_snapshot_key != key):
        payload['last_snapshot_key']=last_snapshot_key
    if (last_snapshot_timestamp != None) & (last_snapshot_timestamp != key):
        payload['last_snapshot_timestamp']=last_snapshot_timestamp
    if (last_transfer_error != None) & (last_transfer_error != key):
        payload['last_transfer_error']=last_transfer_error
    if (last_transfer_type != None) & (last_transfer_type != key):
        payload['last_transfer_type']=last_transfer_type
    if (last_transfer_duration != None) & (last_transfer_duration != key):
        payload['last_transfer_duration']=last_transfer_duration
    if (last_transfer_end_timestamp != None) & (last_transfer_end_timestamp != key):
        payload['last_transfer_end_timestamp']=last_transfer_end_timestamp
    if (last_transfer_size != None) & (last_transfer_size != key):
        payload['last_transfer_size']=last_transfer_size
    if (storage_platform_protection_relationship_key != None) & (storage_platform_protection_relationship_key != key):
        payload['storage_platform_protection_relationship_key']=storage_platform_protection_relationship_key
    if (storage_platform_protection_relationship_type != None) & (storage_platform_protection_relationship_type != key):
        payload['storage_platform_protection_relationship_type']=storage_platform_protection_relationship_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (file_share_key != None) & (file_share_key != key):
        payload['file_share_key']=file_share_key
    if (is_healthy != None) & (is_healthy != key):
        payload['is_healthy']=is_healthy
    if (unhealthy_reason != None) & (unhealthy_reason != key):
        payload['unhealthy_reason']=unhealthy_reason
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.json()
    return json_response

def put():
    url_path        = "/api/1.0/slo/"
    url_path+="data-protection-nodes/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (resource_type != None) & (resource_type != key):
        payload['resource_type']=resource_type
    if (primary_resource_key != None) & (primary_resource_key != key):
        payload['primary_resource_key']=primary_resource_key
    if (primary_resource_type != None) & (primary_resource_type != key):
        payload['primary_resource_type']=primary_resource_type
    if (protection_service_level_key != None) & (protection_service_level_key != key):
        payload['protection_service_level_key']=protection_service_level_key
    if (restore_source_node_name != None) & (restore_source_node_name != key):
        payload['restore_source_node_name']=restore_source_node_name
    if (restore_source_files != None) & (restore_source_files != key):
        payload['restore_source_files']=restore_source_files
    if (restore_file_count != None) & (restore_file_count != key):
        payload['restore_file_count']=restore_file_count
    if (node_name != None) & (node_name != key):
        payload['node_name']=node_name
    if (source_node_name != None) & (source_node_name != key):
        payload['source_node_name']=source_node_name
    if (lag_time != None) & (lag_time != key):
        payload['lag_time']=lag_time
    if (protection_relationship_status != None) & (protection_relationship_status != key):
        payload['protection_relationship_status']=protection_relationship_status
    if (protection_relationship_state != None) & (protection_relationship_state != key):
        payload['protection_relationship_state']=protection_relationship_state
    if (total_bytes_transferred != None) & (total_bytes_transferred != key):
        payload['total_bytes_transferred']=total_bytes_transferred
    if (current_transfer_type != None) & (current_transfer_type != key):
        payload['current_transfer_type']=current_transfer_type
    if (current_snapshot_progress != None) & (current_snapshot_progress != key):
        payload['current_snapshot_progress']=current_snapshot_progress
    if (current_transfer_error != None) & (current_transfer_error != key):
        payload['current_transfer_error']=current_transfer_error
    if (current_transfer_snapshot_key != None) & (current_transfer_snapshot_key != key):
        payload['current_transfer_snapshot_key']=current_transfer_snapshot_key
    if (last_snapshot_key != None) & (last_snapshot_key != key):
        payload['last_snapshot_key']=last_snapshot_key
    if (last_snapshot_timestamp != None) & (last_snapshot_timestamp != key):
        payload['last_snapshot_timestamp']=last_snapshot_timestamp
    if (last_transfer_error != None) & (last_transfer_error != key):
        payload['last_transfer_error']=last_transfer_error
    if (last_transfer_type != None) & (last_transfer_type != key):
        payload['last_transfer_type']=last_transfer_type
    if (last_transfer_duration != None) & (last_transfer_duration != key):
        payload['last_transfer_duration']=last_transfer_duration
    if (last_transfer_end_timestamp != None) & (last_transfer_end_timestamp != key):
        payload['last_transfer_end_timestamp']=last_transfer_end_timestamp
    if (last_transfer_size != None) & (last_transfer_size != key):
        payload['last_transfer_size']=last_transfer_size
    if (storage_platform_protection_relationship_key != None) & (storage_platform_protection_relationship_key != key):
        payload['storage_platform_protection_relationship_key']=storage_platform_protection_relationship_key
    if (storage_platform_protection_relationship_type != None) & (storage_platform_protection_relationship_type != key):
        payload['storage_platform_protection_relationship_type']=storage_platform_protection_relationship_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (file_share_key != None) & (file_share_key != key):
        payload['file_share_key']=file_share_key
    if (is_healthy != None) & (is_healthy != key):
        payload['is_healthy']=is_healthy
    if (unhealthy_reason != None) & (unhealthy_reason != key):
        payload['unhealthy_reason']=unhealthy_reason
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.json()
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path        = "/api/1.0/slo/"
    url_path+="data-protection-nodes/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.json()
        return json_response
    else:
        return "Provide the object key for deletion"

def http_request_for_get(url_path,**payload):
	response = requests.get("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_put(url_path,**payload):
	response = requests.put("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_delete(url_path,**payload):
	response = requests.delete("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": ['get', 'put', 'post', 'delete'],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "resource_type" : {"required": False, "type": "str"},
                "primary_resource_key" : {"required": False, "type": "str"},
                "primary_resource_type" : {"required": False, "type": "str"},
                "protection_service_level_key" : {"required": False, "type": "str"},
                "restore_source_node_name" : {"required": False, "type": "str"},
                "restore_source_files" : {"required": False, "type": "str"},
                "restore_file_count" : {"required": False, "type": "str"},
                "node_name" : {"required": False, "type": "str"},
                "source_node_name" : {"required": False, "type": "str"},
                "lag_time" : {"required": False, "type": "str"},
                "protection_relationship_status" : {"required": False, "type": "str"},
                "protection_relationship_state" : {"required": False, "type": "str"},
                "total_bytes_transferred" : {"required": False, "type": "str"},
                "current_transfer_type" : {"required": False, "type": "str"},
                "current_snapshot_progress" : {"required": False, "type": "str"},
                "current_transfer_error" : {"required": False, "type": "str"},
                "current_transfer_snapshot_key" : {"required": False, "type": "str"},
                "last_snapshot_key" : {"required": False, "type": "str"},
                "last_snapshot_timestamp" : {"required": False, "type": "str"},
                "last_transfer_error" : {"required": False, "type": "str"},
                "last_transfer_type" : {"required": False, "type": "str"},
                "last_transfer_duration" : {"required": False, "type": "str"},
                "last_transfer_end_timestamp" : {"required": False, "type": "str"},
                "last_transfer_size" : {"required": False, "type": "str"},
                "storage_platform_protection_relationship_key" : {"required": False, "type": "str"},
                "storage_platform_protection_relationship_type" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "file_share_key" : {"required": False, "type": "str"},
                "is_healthy" : {"required": False, "type": "str"},
                "unhealthy_reason" : {"required": False, "type": "str"},
                "sortBy" : {"required": False, "type": "str"},
                "maxRecords" : {"required": False, "type": "str"},
                "nextTag" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global key
        key = module.params["key"]
        global resource_type
        resource_type = module.params["resource_type"]
        global primary_resource_key
        primary_resource_key = module.params["primary_resource_key"]
        global primary_resource_type
        primary_resource_type = module.params["primary_resource_type"]
        global protection_service_level_key
        protection_service_level_key = module.params["protection_service_level_key"]
        global restore_source_node_name
        restore_source_node_name = module.params["restore_source_node_name"]
        global restore_source_files
        restore_source_files = module.params["restore_source_files"]
        global restore_file_count
        restore_file_count = module.params["restore_file_count"]
        global node_name
        node_name = module.params["node_name"]
        global source_node_name
        source_node_name = module.params["source_node_name"]
        global lag_time
        lag_time = module.params["lag_time"]
        global protection_relationship_status
        protection_relationship_status = module.params["protection_relationship_status"]
        global protection_relationship_state
        protection_relationship_state = module.params["protection_relationship_state"]
        global total_bytes_transferred
        total_bytes_transferred = module.params["total_bytes_transferred"]
        global current_transfer_type
        current_transfer_type = module.params["current_transfer_type"]
        global current_snapshot_progress
        current_snapshot_progress = module.params["current_snapshot_progress"]
        global current_transfer_error
        current_transfer_error = module.params["current_transfer_error"]
        global current_transfer_snapshot_key
        current_transfer_snapshot_key = module.params["current_transfer_snapshot_key"]
        global last_snapshot_key
        last_snapshot_key = module.params["last_snapshot_key"]
        global last_snapshot_timestamp
        last_snapshot_timestamp = module.params["last_snapshot_timestamp"]
        global last_transfer_error
        last_transfer_error = module.params["last_transfer_error"]
        global last_transfer_type
        last_transfer_type = module.params["last_transfer_type"]
        global last_transfer_duration
        last_transfer_duration = module.params["last_transfer_duration"]
        global last_transfer_end_timestamp
        last_transfer_end_timestamp = module.params["last_transfer_end_timestamp"]
        global last_transfer_size
        last_transfer_size = module.params["last_transfer_size"]
        global storage_platform_protection_relationship_key
        storage_platform_protection_relationship_key = module.params["storage_platform_protection_relationship_key"]
        global storage_platform_protection_relationship_type
        storage_platform_protection_relationship_type = module.params["storage_platform_protection_relationship_type"]
        global storage_platform_type
        storage_platform_type = module.params["storage_platform_type"]
        global file_share_key
        file_share_key = module.params["file_share_key"]
        global is_healthy
        is_healthy = module.params["is_healthy"]
        global unhealthy_reason
        unhealthy_reason = module.params["unhealthy_reason"]
        global sortBy
        sortBy = module.params["sortBy"]
        global maxRecords
        maxRecords = module.params["maxRecords"]
        global nextTag
        nextTag = module.params["nextTag"]

        global json_response

        # Actions
        if module.params["action"] == "get":
                result=get()
                module.exit_json(changed=False,meta=result)
        elif module.params["action"] == "put":
                result=put()
                module.exit_json(changed=True,meta=result)
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result)


if __name__ == '__main__':
    main()