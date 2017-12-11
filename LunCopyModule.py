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


def post():
    url_path        = "/api/1.0/slo/"
    if(lunskey!=None):
        url_path+="luns/"+lunskey+"/jobs/"
    else:
        return "Provide the parent object key"
    url_path+="copy"

    payload={}
    if (name != None) & (name != key):
        payload['name']=name
    if (lun_key != None) & (lun_key != key):
        payload['lun_key']=lun_key
    if (storage_container_key != None) & (storage_container_key != key):
        payload['storage_container_key']=storage_container_key
    if (service_level_class_key != None) & (service_level_class_key != key):
        payload['service_level_class_key']=service_level_class_key

    response=http_request_for_post(url_path,**payload)
    json_response=response.json()
    return json_response


def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": [ 'post' ],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "lunskey" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "lun_key" : {"required": False, "type": "str"},
                "storage_container_key" : {"required": False, "type": "str"},
                "service_level_class_key" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global lunskey
        lunskey   = module.params["lunskey"]
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global name
        name = module.params["name"]
        global lun_key
        lun_key = module.params["lun_key"]
        global storage_container_key
        storage_container_key = module.params["storage_container_key"]
        global service_level_class_key
        service_level_class_key = module.params["service_level_class_key"]

        global json_response

        # Actions
        if module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)

if __name__ == '__main__':
    main()