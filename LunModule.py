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

    url_path+="luns"

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
    if size != None:
        if flag is 0:
            url_path+="?size="+size
            flag=1
        else:
            url_path+="&size="+size
    if used != None:
        if flag is 0:
            url_path+="?used="+used
            flag=1
        else:
            url_path+="&used="+used
    if serial_number != None:
        if flag is 0:
            url_path+="?serial_number="+serial_number
            flag=1
        else:
            url_path+="&serial_number="+serial_number
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if storage_pool_key != None:
        if flag is 0:
            url_path+="?storage_pool_key="+storage_pool_key
            flag=1
        else:
            url_path+="&storage_pool_key="+storage_pool_key
    if storage_service_level_key != None:
        if flag is 0:
            url_path+="?storage_service_level_key="+storage_service_level_key
            flag=1
        else:
            url_path+="&storage_service_level_key="+storage_service_level_key
    if host_usage != None:
        if flag is 0:
            url_path+="?host_usage="+host_usage
            flag=1
        else:
            url_path+="&host_usage="+host_usage
    if storage_compliance_state != None:
        if flag is 0:
            url_path+="?storage_compliance_state="+storage_compliance_state
            flag=1
        else:
            url_path+="&storage_compliance_state="+storage_compliance_state
    if protection_compliance_state != None:
        if flag is 0:
            url_path+="?protection_compliance_state="+protection_compliance_state
            flag=1
        else:
            url_path+="&protection_compliance_state="+protection_compliance_state
    if operational_state != None:
        if flag is 0:
            url_path+="?operational_state="+operational_state
            flag=1
        else:
            url_path+="&operational_state="+operational_state
    if is_read_only != None:
        if flag is 0:
            url_path+="?is_read_only="+is_read_only
            flag=1
        else:
            url_path+="&is_read_only="+is_read_only
    if storage_platform_resource_key != None:
        if flag is 0:
            url_path+="?storage_platform_resource_key="+storage_platform_resource_key
            flag=1
        else:
            url_path+="&storage_platform_resource_key="+storage_platform_resource_key
    if storage_platform_resource_type != None:
        if flag is 0:
            url_path+="?storage_platform_resource_type="+storage_platform_resource_type
            flag=1
        else:
            url_path+="&storage_platform_resource_type="+storage_platform_resource_type
    if storage_platform_type != None:
        if flag is 0:
            url_path+="?storage_platform_type="+storage_platform_type
            flag=1
        else:
            url_path+="&storage_platform_type="+storage_platform_type
    if budgeted_iops != None:
        if flag is 0:
            url_path+="?budgeted_iops="+budgeted_iops
            flag=1
        else:
            url_path+="&budgeted_iops="+budgeted_iops
    if budgeted_capacity != None:
        if flag is 0:
            url_path+="?budgeted_capacity="+budgeted_capacity
            flag=1
        else:
            url_path+="&budgeted_capacity="+budgeted_capacity
    if space_efficiency_saved_size != None:
        if flag is 0:
            url_path+="?space_efficiency_saved_size="+space_efficiency_saved_size
            flag=1
        else:
            url_path+="&space_efficiency_saved_size="+space_efficiency_saved_size
    if max_iops != None:
        if flag is 0:
            url_path+="?max_iops="+max_iops
            flag=1
        else:
            url_path+="&max_iops="+max_iops
    if measured_io_density != None:
        if flag is 0:
            url_path+="?measured_io_density="+measured_io_density
            flag=1
        else:
            url_path+="&measured_io_density="+measured_io_density
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
    if parent_lun_key != None:
        if flag is 0:
            url_path+="?parent_lun_key="+parent_lun_key
            flag=1
        else:
            url_path+="&parent_lun_key="+parent_lun_key
    if is_clone != None:
        if flag is 0:
            url_path+="?is_clone="+is_clone
            flag=1
        else:
            url_path+="&is_clone="+is_clone
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
    url_path+="luns"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (size != None) & (size != key):
        payload['size']=size
    if (used != None) & (used != key):
        payload['used']=used
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (host_usage != None) & (host_usage != key):
        payload['host_usage']=host_usage
    if (storage_compliance_state != None) & (storage_compliance_state != key):
        payload['storage_compliance_state']=storage_compliance_state
    if (protection_compliance_state != None) & (protection_compliance_state != key):
        payload['protection_compliance_state']=protection_compliance_state
    if (operational_state != None) & (operational_state != key):
        payload['operational_state']=operational_state
    if (is_read_only != None) & (is_read_only != key):
        payload['is_read_only']=is_read_only
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (budgeted_capacity != None) & (budgeted_capacity != key):
        payload['budgeted_capacity']=budgeted_capacity
    if (space_efficiency_saved_size != None) & (space_efficiency_saved_size != key):
        payload['space_efficiency_saved_size']=space_efficiency_saved_size
    if (max_iops != None) & (max_iops != key):
        payload['max_iops']=max_iops
    if (measured_io_density != None) & (measured_io_density != key):
        payload['measured_io_density']=measured_io_density
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (parent_lun_key != None) & (parent_lun_key != key):
        payload['parent_lun_key']=parent_lun_key
    if (is_clone != None) & (is_clone != key):
        payload['is_clone']=is_clone
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
    url_path+="luns/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (size != None) & (size != key):
        payload['size']=size
    if (used != None) & (used != key):
        payload['used']=used
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (host_usage != None) & (host_usage != key):
        payload['host_usage']=host_usage
    if (storage_compliance_state != None) & (storage_compliance_state != key):
        payload['storage_compliance_state']=storage_compliance_state
    if (protection_compliance_state != None) & (protection_compliance_state != key):
        payload['protection_compliance_state']=protection_compliance_state
    if (operational_state != None) & (operational_state != key):
        payload['operational_state']=operational_state
    if (is_read_only != None) & (is_read_only != key):
        payload['is_read_only']=is_read_only
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (budgeted_capacity != None) & (budgeted_capacity != key):
        payload['budgeted_capacity']=budgeted_capacity
    if (space_efficiency_saved_size != None) & (space_efficiency_saved_size != key):
        payload['space_efficiency_saved_size']=space_efficiency_saved_size
    if (max_iops != None) & (max_iops != key):
        payload['max_iops']=max_iops
    if (measured_io_density != None) & (measured_io_density != key):
        payload['measured_io_density']=measured_io_density
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (parent_lun_key != None) & (parent_lun_key != key):
        payload['parent_lun_key']=parent_lun_key
    if (is_clone != None) & (is_clone != key):
        payload['is_clone']=is_clone
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
    url_path+="luns/"

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
                "size" : {"required": False, "type": "str"},
                "used" : {"required": False, "type": "str"},
                "serial_number" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "storage_pool_key" : {"required": False, "type": "str"},
                "storage_service_level_key" : {"required": False, "type": "str"},
                "host_usage" : {"required": False, "type": "str"},
                "storage_compliance_state" : {"required": False, "type": "str"},
                "protection_compliance_state" : {"required": False, "type": "str"},
                "operational_state" : {"required": False, "type": "str"},
                "is_read_only" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "budgeted_iops" : {"required": False, "type": "str"},
                "budgeted_capacity" : {"required": False, "type": "str"},
                "space_efficiency_saved_size" : {"required": False, "type": "str"},
                "max_iops" : {"required": False, "type": "str"},
                "measured_io_density" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "parent_lun_key" : {"required": False, "type": "str"},
                "is_clone" : {"required": False, "type": "str"},
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
        global size
        size = module.params["size"]
        global used
        used = module.params["used"]
        global serial_number
        serial_number = module.params["serial_number"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global storage_pool_key
        storage_pool_key = module.params["storage_pool_key"]
        global storage_service_level_key
        storage_service_level_key = module.params["storage_service_level_key"]
        global host_usage
        host_usage = module.params["host_usage"]
        global storage_compliance_state
        storage_compliance_state = module.params["storage_compliance_state"]
        global protection_compliance_state
        protection_compliance_state = module.params["protection_compliance_state"]
        global operational_state
        operational_state = module.params["operational_state"]
        global is_read_only
        is_read_only = module.params["is_read_only"]
        global storage_platform_resource_key
        storage_platform_resource_key = module.params["storage_platform_resource_key"]
        global storage_platform_resource_type
        storage_platform_resource_type = module.params["storage_platform_resource_type"]
        global storage_platform_type
        storage_platform_type = module.params["storage_platform_type"]
        global budgeted_iops
        budgeted_iops = module.params["budgeted_iops"]
        global budgeted_capacity
        budgeted_capacity = module.params["budgeted_capacity"]
        global space_efficiency_saved_size
        space_efficiency_saved_size = module.params["space_efficiency_saved_size"]
        global max_iops
        max_iops = module.params["max_iops"]
        global measured_io_density
        measured_io_density = module.params["measured_io_density"]
        global created_timestamp
        created_timestamp = module.params["created_timestamp"]
        global last_modified_timestamp
        last_modified_timestamp = module.params["last_modified_timestamp"]
        global parent_lun_key
        parent_lun_key = module.params["parent_lun_key"]
        global is_clone
        is_clone = module.params["is_clone"]
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