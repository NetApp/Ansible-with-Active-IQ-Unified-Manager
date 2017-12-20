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
    if(filesharekey!=None):
        url_path+="file-shares/"+filesharekey+"/jobs/"
    else:
        return "Provide the parent object key"
    url_path+="clone"

    payload={}
    if (name != None) & (name != key):
        payload['name']=name
    if (parent_snapshot_key != None) & (parent_snapshot_key != key):
        payload['parent_snapshot_key']=parent_snapshot_key
    if (security_group_id != None) & (security_group_id != key):
        payload['security_group_id']=security_group_id
    if (security_user_id != None) & (security_user_id != key):
        payload['security_user_id']=security_user_id

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
                "filesharekey" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "parent_snapshot_key" : {"required": False, "type": "str"},
                "security_group_id" : {"required": False, "type": "str"},
                "security_user_id" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global filesharekey
        filesharekey   = module.params["filesharekey"]
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global name
        name = module.params["name"]
        global parent_snapshot_key
        parent_snapshot_key = module.params["parent_snapshot_key"]
        global security_group_id
        security_group_id = module.params["security_group_id"]
        global security_user_id
        security_user_id = module.params["security_user_id"]

        global json_response

        # Actions
        if module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)

if __name__ == '__main__':
    main()