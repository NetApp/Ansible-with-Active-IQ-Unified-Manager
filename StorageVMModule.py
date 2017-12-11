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

    url_path+="storage-vms"

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
    if dns_servers != None:
        if flag is 0:
            url_path+="?dns_servers="+dns_servers
            flag=1
        else:
            url_path+="&dns_servers="+dns_servers
    if dns_domains != None:
        if flag is 0:
            url_path+="?dns_domains="+dns_domains
            flag=1
        else:
            url_path+="&dns_domains="+dns_domains
    if nis_servers != None:
        if flag is 0:
            url_path+="?nis_servers="+nis_servers
            flag=1
        else:
            url_path+="&nis_servers="+nis_servers
    if nis_domains != None:
        if flag is 0:
            url_path+="?nis_domains="+nis_domains
            flag=1
        else:
            url_path+="&nis_domains="+nis_domains
    if protocols != None:
        if flag is 0:
            url_path+="?protocols="+protocols
            flag=1
        else:
            url_path+="&protocols="+protocols
    if is_secured != None:
        if flag is 0:
            url_path+="?is_secured="+is_secured
            flag=1
        else:
            url_path+="&is_secured="+is_secured
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
    if supported_storage_service_level_keys != None:
        if flag is 0:
            url_path+="?supported_storage_service_level_keys="+supported_storage_service_level_keys
            flag=1
        else:
            url_path+="&supported_storage_service_level_keys="+supported_storage_service_level_keys
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
    url_path+="storage-vms"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
    if (dns_servers != None) & (dns_servers != key):
        payload['dns_servers']=dns_servers
    if (dns_domains != None) & (dns_domains != key):
        payload['dns_domains']=dns_domains
    if (nis_servers != None) & (nis_servers != key):
        payload['nis_servers']=nis_servers
    if (nis_domains != None) & (nis_domains != key):
        payload['nis_domains']=nis_domains
    if (protocols != None) & (protocols != key):
        payload['protocols']=protocols
    if (is_secured != None) & (is_secured != key):
        payload['is_secured']=is_secured
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
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
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
    url_path+="storage-vms/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_system_key != None) & (storage_system_key != key):
        payload['storage_system_key']=storage_system_key
    if (dns_servers != None) & (dns_servers != key):
        payload['dns_servers']=dns_servers
    if (dns_domains != None) & (dns_domains != key):
        payload['dns_domains']=dns_domains
    if (nis_servers != None) & (nis_servers != key):
        payload['nis_servers']=nis_servers
    if (nis_domains != None) & (nis_domains != key):
        payload['nis_domains']=nis_domains
    if (protocols != None) & (protocols != key):
        payload['protocols']=protocols
    if (is_secured != None) & (is_secured != key):
        payload['is_secured']=is_secured
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
    if (supported_storage_service_level_keys != None) & (supported_storage_service_level_keys != key):
        payload['supported_storage_service_level_keys']=supported_storage_service_level_keys
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
    url_path+="storage-vms/"

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
                "dns_servers" : {"required": False, "type": "str"},
                "dns_domains" : {"required": False, "type": "str"},
                "nis_servers" : {"required": False, "type": "str"},
                "nis_domains" : {"required": False, "type": "str"},
                "protocols" : {"required": False, "type": "str"},
                "is_secured" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "supported_storage_service_level_keys" : {"required": False, "type": "str"},
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
        global dns_servers
        dns_servers = module.params["dns_servers"]
        global dns_domains
        dns_domains = module.params["dns_domains"]
        global nis_servers
        nis_servers = module.params["nis_servers"]
        global nis_domains
        nis_domains = module.params["nis_domains"]
        global protocols
        protocols = module.params["protocols"]
        global is_secured
        is_secured = module.params["is_secured"]
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
        global supported_storage_service_level_keys
        supported_storage_service_level_keys = module.params["supported_storage_service_level_keys"]
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