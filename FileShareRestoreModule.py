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
    url_path+="$title"

    payload={}
    if (snapshot_key != None) & (snapshot_key != key):
        payload['snapshot_key']=snapshot_key
    if (protection_node_name != None) & (protection_node_name != key):
        payload['protection_node_name']=protection_node_name
    if (destination_file_share_key != None) & (destination_file_share_key != key):
        payload['destination_file_share_key']=destination_file_share_key
    if (source_file_path != None) & (source_file_path != key):
        payload['source_file_path']=source_file_path
    if (destination_file_path != None) & (destination_file_path != key):
        payload['destination_file_path']=destination_file_path

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
                "snapshot_key" : {"required": False, "type": "str"},
                "protection_node_name" : {"required": False, "type": "str"},
                "destination_file_share_key" : {"required": False, "type": "str"},
                "source_file_path" : {"required": False, "type": "str"},
                "destination_file_path" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global snapshot_key
        snapshot_key = module.params["snapshot_key"]
        global protection_node_name
        protection_node_name = module.params["protection_node_name"]
        global destination_file_share_key
        destination_file_share_key = module.params["destination_file_share_key"]
        global source_file_path
        source_file_path = module.params["source_file_path"]
        global destination_file_path
        destination_file_path = module.params["destination_file_path"]

        global json_response

        # Actions
        if module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)

if __name__ == '__main__':
    main()