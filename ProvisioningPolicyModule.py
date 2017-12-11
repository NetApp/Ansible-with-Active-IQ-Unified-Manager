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
    url_path+="provisioning-policies"

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
    if is_space_thin_provisioned != None:
        if flag is 0:
            url_path+="?is_space_thin_provisioned="+is_space_thin_provisioned
            flag=1
        else:
            url_path+="&is_space_thin_provisioned="+is_space_thin_provisioned
    if snapshot_reservation_percent != None:
        if flag is 0:
            url_path+="?snapshot_reservation_percent="+snapshot_reservation_percent
            flag=1
        else:
            url_path+="&snapshot_reservation_percent="+snapshot_reservation_percent
    if space_oversubscription_percent != None:
        if flag is 0:
            url_path+="?space_oversubscription_percent="+space_oversubscription_percent
            flag=1
        else:
            url_path+="&space_oversubscription_percent="+space_oversubscription_percent
    if deduplication != None:
        if flag is 0:
            url_path+="?deduplication="+deduplication
            flag=1
        else:
            url_path+="&deduplication="+deduplication
    if compression != None:
        if flag is 0:
            url_path+="?compression="+compression
            flag=1
        else:
            url_path+="&compression="+compression
    if is_iops_thin_provisioned != None:
        if flag is 0:
            url_path+="?is_iops_thin_provisioned="+is_iops_thin_provisioned
            flag=1
        else:
            url_path+="&is_iops_thin_provisioned="+is_iops_thin_provisioned
    if absolute_min_iops != None:
        if flag is 0:
            url_path+="?absolute_min_iops="+absolute_min_iops
            flag=1
        else:
            url_path+="&absolute_min_iops="+absolute_min_iops
    if initial_iops_allocation_percent != None:
        if flag is 0:
            url_path+="?initial_iops_allocation_percent="+initial_iops_allocation_percent
            flag=1
        else:
            url_path+="&initial_iops_allocation_percent="+initial_iops_allocation_percent
    if iops_oversubscription_percent != None:
        if flag is 0:
            url_path+="?iops_oversubscription_percent="+iops_oversubscription_percent
            flag=1
        else:
            url_path+="&iops_oversubscription_percent="+iops_oversubscription_percent
    if is_performance_degradation_allowed != None:
        if flag is 0:
            url_path+="?is_performance_degradation_allowed="+is_performance_degradation_allowed
            flag=1
        else:
            url_path+="&is_performance_degradation_allowed="+is_performance_degradation_allowed
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="provisioning-policies"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (is_space_thin_provisioned != None) & (is_space_thin_provisioned != key):
        payload['is_space_thin_provisioned']=is_space_thin_provisioned
    if (snapshot_reservation_percent != None) & (snapshot_reservation_percent != key):
        payload['snapshot_reservation_percent']=snapshot_reservation_percent
    if (space_oversubscription_percent != None) & (space_oversubscription_percent != key):
        payload['space_oversubscription_percent']=space_oversubscription_percent
    if (deduplication != None) & (deduplication != key):
        payload['deduplication']=deduplication
    if (compression != None) & (compression != key):
        payload['compression']=compression
    if (is_iops_thin_provisioned != None) & (is_iops_thin_provisioned != key):
        payload['is_iops_thin_provisioned']=is_iops_thin_provisioned
    if (absolute_min_iops != None) & (absolute_min_iops != key):
        payload['absolute_min_iops']=absolute_min_iops
    if (initial_iops_allocation_percent != None) & (initial_iops_allocation_percent != key):
        payload['initial_iops_allocation_percent']=initial_iops_allocation_percent
    if (iops_oversubscription_percent != None) & (iops_oversubscription_percent != key):
        payload['iops_oversubscription_percent']=iops_oversubscription_percent
    if (is_performance_degradation_allowed != None) & (is_performance_degradation_allowed != key):
        payload['is_performance_degradation_allowed']=is_performance_degradation_allowed
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="provisioning-policies/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_service_level_key != None) & (storage_service_level_key != key):
        payload['storage_service_level_key']=storage_service_level_key
    if (is_space_thin_provisioned != None) & (is_space_thin_provisioned != key):
        payload['is_space_thin_provisioned']=is_space_thin_provisioned
    if (snapshot_reservation_percent != None) & (snapshot_reservation_percent != key):
        payload['snapshot_reservation_percent']=snapshot_reservation_percent
    if (space_oversubscription_percent != None) & (space_oversubscription_percent != key):
        payload['space_oversubscription_percent']=space_oversubscription_percent
    if (deduplication != None) & (deduplication != key):
        payload['deduplication']=deduplication
    if (compression != None) & (compression != key):
        payload['compression']=compression
    if (is_iops_thin_provisioned != None) & (is_iops_thin_provisioned != key):
        payload['is_iops_thin_provisioned']=is_iops_thin_provisioned
    if (absolute_min_iops != None) & (absolute_min_iops != key):
        payload['absolute_min_iops']=absolute_min_iops
    if (initial_iops_allocation_percent != None) & (initial_iops_allocation_percent != key):
        payload['initial_iops_allocation_percent']=initial_iops_allocation_percent
    if (iops_oversubscription_percent != None) & (iops_oversubscription_percent != key):
        payload['iops_oversubscription_percent']=iops_oversubscription_percent
    if (is_performance_degradation_allowed != None) & (is_performance_degradation_allowed != key):
        payload['is_performance_degradation_allowed']=is_performance_degradation_allowed
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
    if(parentStorageservicelevelkey!=None):
        url_path+="storage-service-levels/"+parentStorageservicelevelkey+"/"
    else:
        return "Provide the parent object key"
    url_path+="provisioning-policies/"

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
                "is_space_thin_provisioned" : {"required": False, "type": "str"},
                "snapshot_reservation_percent" : {"required": False, "type": "str"},
                "space_oversubscription_percent" : {"required": False, "type": "str"},
                "deduplication" : {"required": False, "type": "str"},
                "compression" : {"required": False, "type": "str"},
                "is_iops_thin_provisioned" : {"required": False, "type": "str"},
                "absolute_min_iops" : {"required": False, "type": "str"},
                "initial_iops_allocation_percent" : {"required": False, "type": "str"},
                "iops_oversubscription_percent" : {"required": False, "type": "str"},
                "is_performance_degradation_allowed" : {"required": False, "type": "str"},
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
        global is_space_thin_provisioned
        is_space_thin_provisioned = module.params["is_space_thin_provisioned"]
        global snapshot_reservation_percent
        snapshot_reservation_percent = module.params["snapshot_reservation_percent"]
        global space_oversubscription_percent
        space_oversubscription_percent = module.params["space_oversubscription_percent"]
        global deduplication
        deduplication = module.params["deduplication"]
        global compression
        compression = module.params["compression"]
        global is_iops_thin_provisioned
        is_iops_thin_provisioned = module.params["is_iops_thin_provisioned"]
        global absolute_min_iops
        absolute_min_iops = module.params["absolute_min_iops"]
        global initial_iops_allocation_percent
        initial_iops_allocation_percent = module.params["initial_iops_allocation_percent"]
        global iops_oversubscription_percent
        iops_oversubscription_percent = module.params["iops_oversubscription_percent"]
        global is_performance_degradation_allowed
        is_performance_degradation_allowed = module.params["is_performance_degradation_allowed"]
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