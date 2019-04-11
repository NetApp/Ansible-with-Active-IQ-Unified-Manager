#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_licenses
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed licenses.
description:
    - Create, update or delete license on NetApp Service Level Manager(NSLM). Users are recommended to use the UI to manage the license. If the users are managing license through APIs, then users are requested to pre-process the license data as they have special characters in it. Users should pre-fix the escape character "\" wherever ' " ' is available. License should be given through playbook only. Since Ansible treats colon(:) as a special character and NSLM license has colon in it hence users should assign the license to a variable with a leading space in the playbook and pass that variable as a parameter input. Please refer the example given below.
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  data:
    description:
    - License data provided by the NetApp Licensing team. Modifiable field.
    required: false
    state_supported: present
'''

EXAMPLES = '''
---
hosts: localhost
  vars:
        license: " <nslm_license>"
  tasks: Manage License
    - name: Manage License
      nslm_licenses:
         hostip=<nslm_hostip>
         port=<nslm_portnumber>
         user=<nslm_username>
         password=<nslm_password>
         state=present
         data={{license}}
      register : jsonResult


'''
RETURN = '''
    "msg": {
    "changed": true,
    "failed": false,
    "meta": {<has the job-response returned from NSLM server> },
    "warnings": [
        "Module did not set no_log for password"
    ]
    }
'''
from ansible.module_utils.basic import AnsibleModule
import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")

HEADERS = {
    'content-type': 'application/hal+json'
}

class NetAppNSLMLicenses(object):
    """Class with license operations"""

    def __init__(self):
        """Initialize module parameters"""
        fields = {
            "state" : {
                "required": True,
                    "choices": ['present', 'absent'],
                    "type": 'str'
                    },
            "hostip" : {"required": True, "type": "str"},
            "port" : {"required": True, "type": "str"},
            "user" : {"required": True, "type": "str"},
            "password" : {"required": True, "type": "str"},
            "data" : {"required":False , "type": "str"},
            }

        global module
        module  = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global job_url_path
        global resource_name
        global resource_url_path
        global server_details
        global url_path

        api_host                = module.params["hostip"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]
        job_url_path            = "/api/management-server/jobs/"
        resource_name           = "licenses"
        resource_url_path       = "/api/management-server/admin/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = resource_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATUS
        global PRESENT
        global RETRY_COUNT

        ABSENT      = "absent"
        JOB_KEY     = "job_key"
        JOB_STATUS  = "COMPLETED"
        PRESENT     = "present"
        RETRY_COUNT = 300

        # Properties details
        global data
        global uuid

        data          = module.params["data"]

    def post(self):
        global resource_url_path
        global url_path
        global data
        payload={}
        if  data != None :
            payload['data']=data
        response = requests.post(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response


    def delete(self):
        global url_path
        url_path+="/"+uuid
        response = requests.delete(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def put(self):
        global url_path
        payload={}
        if data != None :
            payload['data']=data
        url_path += "/" + uuid
        response = requests.put(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response

    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either the License has been already deleted or Please provide a valid License uuid")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.put()
                parse_state_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global uuid
    url_license = server_details + url_path
    uuid = get_resource_uuid(url_license)
    if uuid != None:
        return True
    else:
        return False

def parse_state_response(response):
    """ check the response body and take necessary action according to status code """
    if(response.status_code==202):
        job_key = response.json()['job_key']
        job_response = get_job_status(job_key)
        module.exit_json(changed=True,meta=job_response)
    elif(response.status_code==200):
        module.exit_json(changed=True,meta="job successful")
    elif(response.status_code==201):
        module.exit_json(changed=True,meta=response.json())
    else:
        # Returning error message received from NSLM
        module.exit_json(changed=False,meta=response.json())

def get_job_status(job_key):
    """ verify job status and wait for job to complete """
    # to avoid infinite wait condition, in case of NSLM takes more than 300 sec to respond.
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if (response.status_code==200):
            json_response=response.json()
            if (json_response['state'] == JOB_STATUS) :
                break
            RETRY_COUNT -= 1
            time.sleep(1)
        else:
            json_response=response.json()
            break
    return json_response

def get_resource_uuid(url):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        response_json = response.json()
        if response_json.get('num_records') == 0:
            return None
        else:
            embedded = response_json.get('_embedded')
            for record in embedded['netapp:records']:
                resource_key = record.get('uuid')
                return resource_key
    else:
        # Returning error message received from NSLM
        module.exit_json(changed=False,meta=response.json())


def main():
    """Apply license operations from playbook"""
    obj = NetAppNSLMLicenses()
    obj.apply()

if __name__ == '__main__':
    main()
