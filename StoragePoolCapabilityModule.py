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

    url_path+="storage-pool-capabilitys"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_pool_key != None:
        if flag is 0:
            url_path+="?storage_pool_key="+storage_pool_key
            flag=1
        else:
            url_path+="&storage_pool_key="+storage_pool_key
    if capacity != None:
        if flag is 0:
            url_path+="?capacity="+capacity
            flag=1
        else:
            url_path+="&capacity="+capacity
    if storage_service_level_key != None:
        if flag is 0:
            url_path+="?storage_service_level_key="+storage_service_level_key
            flag=1
        else:
            url_path+="&storage_service_level_key="+storage_service_level_key
    if iops != None:
        if flag is 0:
            url_path+="?iops="+iops
            flag=1
        else:
            url_path+="&iops="+iops
    if allocatable_iops != None:
        if flag is 0:
            url_path+="?allocatable_iops="+allocatable_iops
            flag=1
        else:
            url_path+="&allocatable_iops="+allocatable_iops
    if allocatable_capacity != None:
        if flag is 0:
            url_path+="?allocatable_capacity="+allocatable_capacity
            flag=1
        else:
            url_path+="&allocatable_capacity="+allocatable_capacity
    if allocatable_iops_per_tb != None:
        if flag is 0:
            url_path+="?allocatable_iops_per_tb="+allocatable_iops_per_tb
            flag=1
        else:
            url_path+="&allocatable_iops_per_tb="+allocatable_iops_per_tb
    if projected_iops_utilization != None:
        if flag is 0:
            url_path+="?projected_iops_utilization="+projected_iops_utilization
            flag=1
        else:
            url_path+="&projected_iops_utilization="+projected_iops_utilization
    if projected_capacity_utilization != None:
        if flag is 0:
            url_path+="?projected_capacity_utilization="+projected_capacity_utilization
            flag=1
        else:
            url_path+="&projected_capacity_utilization="+projected_capacity_utilization
    if peak_latency != None:
        if flag is 0:
            url_path+="?peak_latency="+peak_latency
            flag=1
        else:
            url_path+="&peak_latency="+peak_latency
    if is_allowed_for_provisioning != None:
        if flag is 0:
            url_path+="?is_allowed_for_provisioning="+is_allowed_for_provisioning
            flag=1
        else:
            url_path+="&is_allowed_for_provisioning="+is_allowed_for_provisioning
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
    if is_capable != None:
        if flag is 0:
            url_path+="?is_capable="+is_capable
            flag=1
        else:
            url_path+="&is_capable="+is_capable
    if error_message != None:
        if flag is 0:
            url_path+="?error_message="+error_message
            flag=1
        else:
            url_path+="&error_message="+error_message
    if effective_storage_service_level_order != None:
        if flag is 0:
            url_path+="?effective_storage_service_level_order="+effective_storage_service_level_order
            flag=1
        else:
            url_path+="&effective_storage_service_level_order="+effective_storage_service_level_order
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
    url_path+="storage-pool-capabilitys"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (capacity != None) & (capacity != key):
        payload['capacity']=capacity
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (iops != None) & (iops != key):
        payload['iops']=iops
    if (allocatable_iops != None) & (allocatable_iops != key):
        payload['allocatable_iops']=allocatable_iops
    if (allocatable_capacity != None) & (allocatable_capacity != key):
        payload['allocatable_capacity']=allocatable_capacity
    if (allocatable_iops_per_tb != None) & (allocatable_iops_per_tb != key):
        payload['allocatable_iops_per_tb']=allocatable_iops_per_tb
    if (projected_iops_utilization != None) & (projected_iops_utilization != key):
        payload['projected_iops_utilization']=projected_iops_utilization
    if (projected_capacity_utilization != None) & (projected_capacity_utilization != key):
        payload['projected_capacity_utilization']=projected_capacity_utilization
    if (peak_latency != None) & (peak_latency != key):
        payload['peak_latency']=peak_latency
    if (is_allowed_for_provisioning != None) & (is_allowed_for_provisioning != key):
        payload['is_allowed_for_provisioning']=is_allowed_for_provisioning
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (is_capable != None) & (is_capable != key):
        payload['is_capable']=is_capable
    if (error_message != None) & (error_message != key):
        payload['error_message']=error_message
    if (effective_storage_service_level_order != None) & (effective_storage_service_level_order != key):
        payload['effective_storage_service_level_order']=effective_storage_service_level_order
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
    url_path+="storage-pool-capabilitys/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (capacity != None) & (capacity != key):
        payload['capacity']=capacity
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (iops != None) & (iops != key):
        payload['iops']=iops
    if (allocatable_iops != None) & (allocatable_iops != key):
        payload['allocatable_iops']=allocatable_iops
    if (allocatable_capacity != None) & (allocatable_capacity != key):
        payload['allocatable_capacity']=allocatable_capacity
    if (allocatable_iops_per_tb != None) & (allocatable_iops_per_tb != key):
        payload['allocatable_iops_per_tb']=allocatable_iops_per_tb
    if (projected_iops_utilization != None) & (projected_iops_utilization != key):
        payload['projected_iops_utilization']=projected_iops_utilization
    if (projected_capacity_utilization != None) & (projected_capacity_utilization != key):
        payload['projected_capacity_utilization']=projected_capacity_utilization
    if (peak_latency != None) & (peak_latency != key):
        payload['peak_latency']=peak_latency
    if (is_allowed_for_provisioning != None) & (is_allowed_for_provisioning != key):
        payload['is_allowed_for_provisioning']=is_allowed_for_provisioning
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (is_capable != None) & (is_capable != key):
        payload['is_capable']=is_capable
    if (error_message != None) & (error_message != key):
        payload['error_message']=error_message
    if (effective_storage_service_level_order != None) & (effective_storage_service_level_order != key):
        payload['effective_storage_service_level_order']=effective_storage_service_level_order
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
    url_path+="storage-pool-capabilitys/"

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
                "storage_pool_key" : {"required": False, "type": "str"},
                "capacity" : {"required": False, "type": "str"},
                "storage_service_level_key" : {"required": False, "type": "str"},
                "iops" : {"required": False, "type": "str"},
                "allocatable_iops" : {"required": False, "type": "str"},
                "allocatable_capacity" : {"required": False, "type": "str"},
                "allocatable_iops_per_tb" : {"required": False, "type": "str"},
                "projected_iops_utilization" : {"required": False, "type": "str"},
                "projected_capacity_utilization" : {"required": False, "type": "str"},
                "peak_latency" : {"required": False, "type": "str"},
                "is_allowed_for_provisioning" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "is_capable" : {"required": False, "type": "str"},
                "error_message" : {"required": False, "type": "str"},
                "effective_storage_service_level_order" : {"required": False, "type": "str"},
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
        global storage_pool_key
        storage_pool_key = module.params["storage_pool_key"]
        global capacity
        capacity = module.params["capacity"]
        global storage_service_level_key
        storage_service_level_key = module.params["storage_service_level_key"]
        global iops
        iops = module.params["iops"]
        global allocatable_iops
        allocatable_iops = module.params["allocatable_iops"]
        global allocatable_capacity
        allocatable_capacity = module.params["allocatable_capacity"]
        global allocatable_iops_per_tb
        allocatable_iops_per_tb = module.params["allocatable_iops_per_tb"]
        global projected_iops_utilization
        projected_iops_utilization = module.params["projected_iops_utilization"]
        global projected_capacity_utilization
        projected_capacity_utilization = module.params["projected_capacity_utilization"]
        global peak_latency
        peak_latency = module.params["peak_latency"]
        global is_allowed_for_provisioning
        is_allowed_for_provisioning = module.params["is_allowed_for_provisioning"]
        global created_timestamp
        created_timestamp = module.params["created_timestamp"]
        global last_modified_timestamp
        last_modified_timestamp = module.params["last_modified_timestamp"]
        global is_capable
        is_capable = module.params["is_capable"]
        global error_message
        error_message = module.params["error_message"]
        global effective_storage_service_level_order
        effective_storage_service_level_order = module.params["effective_storage_service_level_order"]
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