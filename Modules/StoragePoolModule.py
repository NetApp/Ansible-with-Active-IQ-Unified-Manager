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

    url_path+="storage-pools"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if name != None:
        if flag is 0:
            url_path+="?name="+name
            flag=1
        else:
            url_path+="&name="+name
    if type != None:
        if flag is 0:
            url_path+="?type="+type
            flag=1
        else:
            url_path+="&type="+type
    if controller_key != None:
        if flag is 0:
            url_path+="?controller_key="+controller_key
            flag=1
        else:
            url_path+="&controller_key="+controller_key
    if storage_system_key != None:
        if flag is 0:
            url_path+="?storage_system_key="+storage_system_key
            flag=1
        else:
            url_path+="&storage_system_key="+storage_system_key
    if total_capacity != None:
        if flag is 0:
            url_path+="?total_capacity="+total_capacity
            flag=1
        else:
            url_path+="&total_capacity="+total_capacity
    if used_capacity != None:
        if flag is 0:
            url_path+="?used_capacity="+used_capacity
            flag=1
        else:
            url_path+="&used_capacity="+used_capacity
    if allocated_capacity != None:
        if flag is 0:
            url_path+="?allocated_capacity="+allocated_capacity
            flag=1
        else:
            url_path+="&allocated_capacity="+allocated_capacity
    if allocatable_capacity != None:
        if flag is 0:
            url_path+="?allocatable_capacity="+allocatable_capacity
            flag=1
        else:
            url_path+="&allocatable_capacity="+allocatable_capacity
    if budgeted_capacity != None:
        if flag is 0:
            url_path+="?budgeted_capacity="+budgeted_capacity
            flag=1
        else:
            url_path+="&budgeted_capacity="+budgeted_capacity
    if maximum_iops != None:
        if flag is 0:
            url_path+="?maximum_iops="+maximum_iops
            flag=1
        else:
            url_path+="&maximum_iops="+maximum_iops
    if actual_iops != None:
        if flag is 0:
            url_path+="?actual_iops="+actual_iops
            flag=1
        else:
            url_path+="&actual_iops="+actual_iops
    if allocatable_iops != None:
        if flag is 0:
            url_path+="?allocatable_iops="+allocatable_iops
            flag=1
        else:
            url_path+="&allocatable_iops="+allocatable_iops
    if budgeted_iops != None:
        if flag is 0:
            url_path+="?budgeted_iops="+budgeted_iops
            flag=1
        else:
            url_path+="&budgeted_iops="+budgeted_iops
    if provisioned_peak_iops != None:
        if flag is 0:
            url_path+="?provisioned_peak_iops="+provisioned_peak_iops
            flag=1
        else:
            url_path+="&provisioned_peak_iops="+provisioned_peak_iops
    if operating_storage_service_level_key != None:
        if flag is 0:
            url_path+="?operating_storage_service_level_key="+operating_storage_service_level_key
            flag=1
        else:
            url_path+="&operating_storage_service_level_key="+operating_storage_service_level_key
    if storage_platform_type != None:
        if flag is 0:
            url_path+="?storage_platform_type="+storage_platform_type
            flag=1
        else:
            url_path+="&storage_platform_type="+storage_platform_type
    if storage_platform_resource_type != None:
        if flag is 0:
            url_path+="?storage_platform_resource_type="+storage_platform_resource_type
            flag=1
        else:
            url_path+="&storage_platform_resource_type="+storage_platform_resource_type
    if storage_platform_resource_key != None:
        if flag is 0:
            url_path+="?storage_platform_resource_key="+storage_platform_resource_key
            flag=1
        else:
            url_path+="&storage_platform_resource_key="+storage_platform_resource_key
    if created_timestamp != None:
        if flag is 0:
            url_path+="?created_timestamp="+created_timestamp
            flag=1
        else:
            url_path+="&created_timestamp="+created_timestamp
    if last_modified_timestamp != None:
        if flag is 0:
            url_path+="?last_modified_timestamp="+last_modified_timestamp
            flag=1
        else:
            url_path+="&last_modified_timestamp="+last_modified_timestamp
    if supported_storage_service_level_keys != None:
        if flag is 0:
            url_path+="?supported_storage_service_level_keys="+supported_storage_service_level_keys
            flag=1
        else:
            url_path+="&supported_storage_service_level_keys="+supported_storage_service_level_keys
    if allowed_storage_service_level_keys != None:
        if flag is 0:
            url_path+="?allowed_storage_service_level_keys="+allowed_storage_service_level_keys
            flag=1
        else:
            url_path+="&allowed_storage_service_level_keys="+allowed_storage_service_level_keys
    if bottleneck_type != None:
        if flag is 0:
            url_path+="?bottleneck_type="+bottleneck_type
            flag=1
        else:
            url_path+="&bottleneck_type="+bottleneck_type
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
    url_path+="storage-pools"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (type != None) & (type != key):
        payload['type']=type
    if (controller_key != None) & (controller_key != key):
        payload['controller_key']=controller_key
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
    if (total_capacity != None) & (total_capacity != key):
        payload['total_capacity']=total_capacity
    if (used_capacity != None) & (used_capacity != key):
        payload['used_capacity']=used_capacity
    if (allocated_capacity != None) & (allocated_capacity != key):
        payload['allocated_capacity']=allocated_capacity
    if (allocatable_capacity != None) & (allocatable_capacity != key):
        payload['allocatable_capacity']=allocatable_capacity
    if (budgeted_capacity != None) & (budgeted_capacity != key):
        payload['budgeted_capacity']=budgeted_capacity
    if (maximum_iops != None) & (maximum_iops != key):
        payload['maximum_iops']=maximum_iops
    if (actual_iops != None) & (actual_iops != key):
        payload['actual_iops']=actual_iops
    if (allocatable_iops != None) & (allocatable_iops != key):
        payload['allocatable_iops']=allocatable_iops
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (provisioned_peak_iops != None) & (provisioned_peak_iops != key):
        payload['provisioned_peak_iops']=provisioned_peak_iops
    if (operating_storage_service_level_key != None) & (operating_storage_service_level_key != key):
        payload['operating_storage_service_level_key']=operating_storage_service_level_key
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
    if (allowed_storage_service_level_keys != None) & (allowed_storage_service_level_keys != key):
        payload['allowed_storage_service_level_keys']=allowed_storage_service_level_keys
    if (bottleneck_type != None) & (bottleneck_type != key):
        payload['bottleneck_type']=bottleneck_type
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
    url_path+="storage-pools/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (type != None) & (type != key):
        payload['type']=type
    if (controller_key != None) & (controller_key != key):
        payload['controller_key']=controller_key
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
    if (total_capacity != None) & (total_capacity != key):
        payload['total_capacity']=total_capacity
    if (used_capacity != None) & (used_capacity != key):
        payload['used_capacity']=used_capacity
    if (allocated_capacity != None) & (allocated_capacity != key):
        payload['allocated_capacity']=allocated_capacity
    if (allocatable_capacity != None) & (allocatable_capacity != key):
        payload['allocatable_capacity']=allocatable_capacity
    if (budgeted_capacity != None) & (budgeted_capacity != key):
        payload['budgeted_capacity']=budgeted_capacity
    if (maximum_iops != None) & (maximum_iops != key):
        payload['maximum_iops']=maximum_iops
    if (actual_iops != None) & (actual_iops != key):
        payload['actual_iops']=actual_iops
    if (allocatable_iops != None) & (allocatable_iops != key):
        payload['allocatable_iops']=allocatable_iops
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (provisioned_peak_iops != None) & (provisioned_peak_iops != key):
        payload['provisioned_peak_iops']=provisioned_peak_iops
    if (operating_storage_service_level_key != None) & (operating_storage_service_level_key != key):
        payload['operating_storage_service_level_key']=operating_storage_service_level_key
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
    if (allowed_storage_service_level_keys != None) & (allowed_storage_service_level_keys != key):
        payload['allowed_storage_service_level_keys']=allowed_storage_service_level_keys
    if (bottleneck_type != None) & (bottleneck_type != key):
        payload['bottleneck_type']=bottleneck_type
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
    url_path+="storage-pools/"

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
                "name" : {"required": False, "type": "str"},
                "type" : {"required": False, "type": "str"},
                "controller_key" : {"required": False, "type": "str"},
                "storage_system_key" : {"required": False, "type": "str"},
                "total_capacity" : {"required": False, "type": "str"},
                "used_capacity" : {"required": False, "type": "str"},
                "allocated_capacity" : {"required": False, "type": "str"},
                "allocatable_capacity" : {"required": False, "type": "str"},
                "budgeted_capacity" : {"required": False, "type": "str"},
                "maximum_iops" : {"required": False, "type": "str"},
                "actual_iops" : {"required": False, "type": "str"},
                "allocatable_iops" : {"required": False, "type": "str"},
                "budgeted_iops" : {"required": False, "type": "str"},
                "provisioned_peak_iops" : {"required": False, "type": "str"},
                "operating_storage_service_level_key" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "supported_storage_service_level_keys" : {"required": False, "type": "str"},
                "allowed_storage_service_level_keys" : {"required": False, "type": "str"},
                "bottleneck_type" : {"required": False, "type": "str"},
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
        global name
        name = module.params["name"]
        global type
        type = module.params["type"]
        global controller_key
        controller_key = module.params["controller_key"]
        global storage_system_key
        storage_system_key = module.params["storage_system_key"]
        global total_capacity
        total_capacity = module.params["total_capacity"]
        global used_capacity
        used_capacity = module.params["used_capacity"]
        global allocated_capacity
        allocated_capacity = module.params["allocated_capacity"]
        global allocatable_capacity
        allocatable_capacity = module.params["allocatable_capacity"]
        global budgeted_capacity
        budgeted_capacity = module.params["budgeted_capacity"]
        global maximum_iops
        maximum_iops = module.params["maximum_iops"]
        global actual_iops
        actual_iops = module.params["actual_iops"]
        global allocatable_iops
        allocatable_iops = module.params["allocatable_iops"]
        global budgeted_iops
        budgeted_iops = module.params["budgeted_iops"]
        global provisioned_peak_iops
        provisioned_peak_iops = module.params["provisioned_peak_iops"]
        global operating_storage_service_level_key
        operating_storage_service_level_key = module.params["operating_storage_service_level_key"]
        global storage_platform_type
        storage_platform_type = module.params["storage_platform_type"]
        global storage_platform_resource_type
        storage_platform_resource_type = module.params["storage_platform_resource_type"]
        global storage_platform_resource_key
        storage_platform_resource_key = module.params["storage_platform_resource_key"]
        global created_timestamp
        created_timestamp = module.params["created_timestamp"]
        global last_modified_timestamp
        last_modified_timestamp = module.params["last_modified_timestamp"]
        global supported_storage_service_level_keys
        supported_storage_service_level_keys = module.params["supported_storage_service_level_keys"]
        global allowed_storage_service_level_keys
        allowed_storage_service_level_keys = module.params["allowed_storage_service_level_keys"]
        global bottleneck_type
        bottleneck_type = module.params["bottleneck_type"]
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