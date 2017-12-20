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

    if(parentLunkey!=None):
        url_path+="luns/"+parentLunkey+"/"
        flag=1
    if(parentNfssharekey!=None):
        url_path+="nfs-shares/"+parentNfssharekey+"/"
        flag=1
    if(parentCifssharekey!=None):
        url_path+="cifs-shares/"+parentCifssharekey+"/"
        flag=1
    if(parentStorageVmkey!=None):
        url_path+="storage-vms/"+parentStorageVmkey+"/"
        flag=1
    if(flag==0):
        return "Provide the parent object key"
    url_path+="ip-access-points"

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
    if ip_address != None:
        if flag is 0:
            url_path+="?ip_address="+ip_address
            flag=1
        else:
            url_path+="&ip_address="+ip_address
    if data_access_protocols != None:
        if flag is 0:
            url_path+="?data_access_protocols="+data_access_protocols
            flag=1
        else:
            url_path+="&data_access_protocols="+data_access_protocols
    if is_optimal != None:
        if flag is 0:
            url_path+="?is_optimal="+is_optimal
            flag=1
        else:
            url_path+="&is_optimal="+is_optimal
    if container_key != None:
        if flag is 0:
            url_path+="?container_key="+container_key
            flag=1
        else:
            url_path+="&container_key="+container_key
    if container_type != None:
        if flag is 0:
            url_path+="?container_type="+container_type
            flag=1
        else:
            url_path+="&container_type="+container_type
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
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
    if(parentLunkey!=None):
        url_path+="luns/"+parentLunkey+"/"
    if(parentNfssharekey!=None):
        url_path+="nfs-shares/"+parentNfssharekey+"/"
    if(parentCifssharekey!=None):
        url_path+="cifs-shares/"+parentCifssharekey+"/"
    if(parentStorageVmkey!=None):
        url_path+="storage-vms/"+parentStorageVmkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="ip-access-points"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (ip_address != None) & (ip_address != key):
        payload['ip_address']=ip_address
    if (data_access_protocols != None) & (data_access_protocols != key):
        payload['data_access_protocols']=data_access_protocols
    if (is_optimal != None) & (is_optimal != key):
        payload['is_optimal']=is_optimal
    if (container_key != None) & (container_key != key):
        payload['container_key']=container_key
    if (container_type != None) & (container_type != key):
        payload['container_type']=container_type
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
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
    if(parentLunkey!=None):
        url_path+="luns/"+parentLunkey+"/"
    if(parentNfssharekey!=None):
        url_path+="nfs-shares/"+parentNfssharekey+"/"
    if(parentCifssharekey!=None):
        url_path+="cifs-shares/"+parentCifssharekey+"/"
    if(parentStorageVmkey!=None):
        url_path+="storage-vms/"+parentStorageVmkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="ip-access-points/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (ip_address != None) & (ip_address != key):
        payload['ip_address']=ip_address
    if (data_access_protocols != None) & (data_access_protocols != key):
        payload['data_access_protocols']=data_access_protocols
    if (is_optimal != None) & (is_optimal != key):
        payload['is_optimal']=is_optimal
    if (container_key != None) & (container_key != key):
        payload['container_key']=container_key
    if (container_type != None) & (container_type != key):
        payload['container_type']=container_type
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (storage_platform_resource_key != None) & (storage_platform_resource_key != key):
        payload['storage_platform_resource_key']=storage_platform_resource_key
    if (storage_platform_resource_type != None) & (storage_platform_resource_type != key):
        payload['storage_platform_resource_type']=storage_platform_resource_type
    if (storage_platform_type != None) & (storage_platform_type != key):
        payload['storage_platform_type']=storage_platform_type
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
    if(parentLunkey!=None):
        url_path+="luns/"+parentLunkey+"/"
    if(parentNfssharekey!=None):
        url_path+="nfs-shares/"+parentNfssharekey+"/"
    if(parentCifssharekey!=None):
        url_path+="cifs-shares/"+parentCifssharekey+"/"
    if(parentStorageVmkey!=None):
        url_path+="storage-vms/"+parentStorageVmkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="ip-access-points/"

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
                "parentLunkey" : {"required": False, "type": "str"},
                "parentNfssharekey" : {"required": False, "type": "str"},
                "parentCifssharekey" : {"required": False, "type": "str"},
                "parentStorageVmkey" : {"required": False, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "ip_address" : {"required": False, "type": "str"},
                "data_access_protocols" : {"required": False, "type": "str"},
                "is_optimal" : {"required": False, "type": "str"},
                "container_key" : {"required": False, "type": "str"},
                "container_type" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "storage_platform_resource_key" : {"required": False, "type": "str"},
                "storage_platform_resource_type" : {"required": False, "type": "str"},
                "storage_platform_type" : {"required": False, "type": "str"},
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

        global parentLunkey
        parentLunkey   = module.params["parentLunkey"]
        global parentNfssharekey
        parentNfssharekey   = module.params["parentNfssharekey"]
        global parentCifssharekey
        parentCifssharekey   = module.params["parentCifssharekey"]
        global parentStorageVmkey
        parentStorageVmkey   = module.params["parentStorageVmkey"]
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
        global ip_address
        ip_address = module.params["ip_address"]
        global data_access_protocols
        data_access_protocols = module.params["data_access_protocols"]
        global is_optimal
        is_optimal = module.params["is_optimal"]
        global container_key
        container_key = module.params["container_key"]
        global container_type
        container_type = module.params["container_type"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global storage_platform_resource_key
        storage_platform_resource_key = module.params["storage_platform_resource_key"]
        global storage_platform_resource_type
        storage_platform_resource_type = module.params["storage_platform_resource_type"]
        global storage_platform_type
        storage_platform_type = module.params["storage_platform_type"]
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