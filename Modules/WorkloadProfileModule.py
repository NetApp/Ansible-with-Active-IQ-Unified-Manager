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

    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
        flag=1
    if(flag==0):
        return "Provide the parent object key"
    url_path+="workload-profiles"

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
    if storage_service_level_key != None:
        if flag is 0:
            url_path+="?storage_service_level_key="+storage_service_level_key
            flag=1
        else:
            url_path+="&storage_service_level_key="+storage_service_level_key
    if random_read_percent != None:
        if flag is 0:
            url_path+="?random_read_percent="+random_read_percent
            flag=1
        else:
            url_path+="&random_read_percent="+random_read_percent
    if random_write_percent != None:
        if flag is 0:
            url_path+="?random_write_percent="+random_write_percent
            flag=1
        else:
            url_path+="&random_write_percent="+random_write_percent
    if sequential_read_percent != None:
        if flag is 0:
            url_path+="?sequential_read_percent="+sequential_read_percent
            flag=1
        else:
            url_path+="&sequential_read_percent="+sequential_read_percent
    if sequential_write_percent != None:
        if flag is 0:
            url_path+="?sequential_write_percent="+sequential_write_percent
            flag=1
        else:
            url_path+="&sequential_write_percent="+sequential_write_percent
    if active_working_set != None:
        if flag is 0:
            url_path+="?active_working_set="+active_working_set
            flag=1
        else:
            url_path+="&active_working_set="+active_working_set
    if random_read_size != None:
        if flag is 0:
            url_path+="?random_read_size="+random_read_size
            flag=1
        else:
            url_path+="&random_read_size="+random_read_size
    if random_write_size != None:
        if flag is 0:
            url_path+="?random_write_size="+random_write_size
            flag=1
        else:
            url_path+="&random_write_size="+random_write_size
    if sequential_read_size != None:
        if flag is 0:
            url_path+="?sequential_read_size="+sequential_read_size
            flag=1
        else:
            url_path+="&sequential_read_size="+sequential_read_size
    if sequential_write_size != None:
        if flag is 0:
            url_path+="?sequential_write_size="+sequential_write_size
            flag=1
        else:
            url_path+="&sequential_write_size="+sequential_write_size
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
    if protocol != None:
        if flag is 0:
            url_path+="?protocol="+protocol
            flag=1
        else:
            url_path+="&protocol="+protocol
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="workload-profiles"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (random_read_percent != None) & (random_read_percent != key):
        payload['random_read_percent']=random_read_percent
    if (random_write_percent != None) & (random_write_percent != key):
        payload['random_write_percent']=random_write_percent
    if (sequential_read_percent != None) & (sequential_read_percent != key):
        payload['sequential_read_percent']=sequential_read_percent
    if (sequential_write_percent != None) & (sequential_write_percent != key):
        payload['sequential_write_percent']=sequential_write_percent
    if (active_working_set != None) & (active_working_set != key):
        payload['active_working_set']=active_working_set
    if (random_read_size != None) & (random_read_size != key):
        payload['random_read_size']=random_read_size
    if (random_write_size != None) & (random_write_size != key):
        payload['random_write_size']=random_write_size
    if (sequential_read_size != None) & (sequential_read_size != key):
        payload['sequential_read_size']=sequential_read_size
    if (sequential_write_size != None) & (sequential_write_size != key):
        payload['sequential_write_size']=sequential_write_size
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (protocol != None) & (protocol != key):
        payload['protocol']=protocol
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="workload-profiles/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (random_read_percent != None) & (random_read_percent != key):
        payload['random_read_percent']=random_read_percent
    if (random_write_percent != None) & (random_write_percent != key):
        payload['random_write_percent']=random_write_percent
    if (sequential_read_percent != None) & (sequential_read_percent != key):
        payload['sequential_read_percent']=sequential_read_percent
    if (sequential_write_percent != None) & (sequential_write_percent != key):
        payload['sequential_write_percent']=sequential_write_percent
    if (active_working_set != None) & (active_working_set != key):
        payload['active_working_set']=active_working_set
    if (random_read_size != None) & (random_read_size != key):
        payload['random_read_size']=random_read_size
    if (random_write_size != None) & (random_write_size != key):
        payload['random_write_size']=random_write_size
    if (sequential_read_size != None) & (sequential_read_size != key):
        payload['sequential_read_size']=sequential_read_size
    if (sequential_write_size != None) & (sequential_write_size != key):
        payload['sequential_write_size']=sequential_write_size
    if (created_timestamp != None) & (created_timestamp != key):
        payload['created_timestamp']=created_timestamp
    if (last_modified_timestamp != None) & (last_modified_timestamp != key):
        payload['last_modified_timestamp']=last_modified_timestamp
    if (protocol != None) & (protocol != key):
        payload['protocol']=protocol
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="workload-profiles/"

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
                "parentStorageservicelevelkey" : {"required": False, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "storage_service_level_key" : {"required": False, "type": "str"},
                "random_read_percent" : {"required": False, "type": "str"},
                "random_write_percent" : {"required": False, "type": "str"},
                "sequential_read_percent" : {"required": False, "type": "str"},
                "sequential_write_percent" : {"required": False, "type": "str"},
                "active_working_set" : {"required": False, "type": "str"},
                "random_read_size" : {"required": False, "type": "str"},
                "random_write_size" : {"required": False, "type": "str"},
                "sequential_read_size" : {"required": False, "type": "str"},
                "sequential_write_size" : {"required": False, "type": "str"},
                "created_timestamp" : {"required": False, "type": "str"},
                "last_modified_timestamp" : {"required": False, "type": "str"},
                "protocol" : {"required": False, "type": "str"},
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

        global parentStorageservicelevelkey
        parentStorageservicelevelkey   = module.params["parentStorageservicelevelkey"]
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
        global storage_service_level_key
        storage_service_level_key = module.params["storage_service_level_key"]
        global random_read_percent
        random_read_percent = module.params["random_read_percent"]
        global random_write_percent
        random_write_percent = module.params["random_write_percent"]
        global sequential_read_percent
        sequential_read_percent = module.params["sequential_read_percent"]
        global sequential_write_percent
        sequential_write_percent = module.params["sequential_write_percent"]
        global active_working_set
        active_working_set = module.params["active_working_set"]
        global random_read_size
        random_read_size = module.params["random_read_size"]
        global random_write_size
        random_write_size = module.params["random_write_size"]
        global sequential_read_size
        sequential_read_size = module.params["sequential_read_size"]
        global sequential_write_size
        sequential_write_size = module.params["sequential_write_size"]
        global created_timestamp
        created_timestamp = module.params["created_timestamp"]
        global last_modified_timestamp
        last_modified_timestamp = module.params["last_modified_timestamp"]
        global protocol
        protocol = module.params["protocol"]
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