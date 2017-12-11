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

    url_path+="lun-maps"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if lun_key != None:
        if flag is 0:
            url_path+="?lun_key="+lun_key
            flag=1
        else:
            url_path+="&lun_key="+lun_key
    if initiator_group_key != None:
        if flag is 0:
            url_path+="?initiator_group_key="+initiator_group_key
            flag=1
        else:
            url_path+="&initiator_group_key="+initiator_group_key
    if lun_id != None:
        if flag is 0:
            url_path+="?lun_id="+lun_id
            flag=1
        else:
            url_path+="&lun_id="+lun_id
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
    url_path+="lun-maps"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (lun_key != None) & (lun_key != key):
        payload['lun_key']=lun_key
    if (initiator_group_key != None) & (initiator_group_key != key):
        payload['initiator_group_key']=initiator_group_key
    if (lun_id != None) & (lun_id != key):
        payload['lun_id']=lun_id
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
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
    url_path+="lun-maps/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (lun_key != None) & (lun_key != key):
        payload['lun_key']=lun_key
    if (initiator_group_key != None) & (initiator_group_key != key):
        payload['initiator_group_key']=initiator_group_key
    if (lun_id != None) & (lun_id != key):
        payload['lun_id']=lun_id
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
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
    url_path+="lun-maps/"

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
                "lun_key" : {"required": False, "type": "str"},
                "initiator_group_key" : {"required": False, "type": "str"},
                "lun_id" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
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
        global lun_key
        lun_key = module.params["lun_key"]
        global initiator_group_key
        initiator_group_key = module.params["initiator_group_key"]
        global lun_id
        lun_id = module.params["lun_id"]
        global storage_platform_resource_key
        storage_platform_resource_key = module.params["storage_platform_resource_key"]
        global storage_platform_resource_type
        storage_platform_resource_type = module.params["storage_platform_resource_type"]
        global storage_platform_type
        storage_platform_type = module.params["storage_platform_type"]
        global created_timestamp
        created_timestamp = module.params["created_timestamp"]
        global last_modified_timestamp
        last_modified_timestamp = module.params["last_modified_timestamp"]
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