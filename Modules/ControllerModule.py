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

    url_path+="controllers"

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
    if storage_system_key != None:
        if flag is 0:
            url_path+="?storage_system_key="+storage_system_key
            flag=1
        else:
            url_path+="&storage_system_key="+storage_system_key
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
    if estimated_max_iops != None:
        if flag is 0:
            url_path+="?estimated_max_iops="+estimated_max_iops
            flag=1
        else:
            url_path+="&estimated_max_iops="+estimated_max_iops
    if budgeted_iops != None:
        if flag is 0:
            url_path+="?budgeted_iops="+budgeted_iops
            flag=1
        else:
            url_path+="&budgeted_iops="+budgeted_iops
    if supported_storage_service_level_keys != None:
        if flag is 0:
            url_path+="?supported_storage_service_level_keys="+supported_storage_service_level_keys
            flag=1
        else:
            url_path+="&supported_storage_service_level_keys="+supported_storage_service_level_keys
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
    url_path+="controllers"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
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
    if (estimated_max_iops != None) & (estimated_max_iops != key):
        payload['estimated_max_iops']=estimated_max_iops
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
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
    url_path+="controllers/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
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
    if (estimated_max_iops != None) & (estimated_max_iops != key):
        payload['estimated_max_iops']=estimated_max_iops
    if (budgeted_iops != None) & (budgeted_iops != key):
        payload['budgeted_iops']=budgeted_iops
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
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
    url_path+="controllers/"

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
                "storage_system_key" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "estimated_max_iops" : {"required": False, "type": "str"},
                "budgeted_iops" : {"required": False, "type": "str"},
                "supported_storage_service_level_keys" : {"required": False, "type": "str"},
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
        global storage_system_key
        storage_system_key = module.params["storage_system_key"]
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
        global estimated_max_iops
        estimated_max_iops = module.params["estimated_max_iops"]
        global budgeted_iops
        budgeted_iops = module.params["budgeted_iops"]
        global supported_storage_service_level_keys
        supported_storage_service_level_keys = module.params["supported_storage_service_level_keys"]
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