#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: aiqum_performance_service_levels
author:
    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)
short_description: Active IQ Unified Manager(AIQUM) managed performance-service-levels.
description:
     - Create, update or delete performance-service-level on Active IQ Unified Manager(AIQUM).
version_added: "2.9.1"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  absolute_min_iops:
    description:
    - The absolute minimum IOPS value that is used as an override when the expected IOPS is less than this value. Modifiable field.
    required: false
    state_supported: present
  description:
    description:
    - Description of the performance-service-level. Modifiable field.
    required: false
    state_supported: present
  expected_iops_per_tb:
    description:
    - Minimum number of IOPS, per terabyte (TB) of storage space, guaranteed to a client that is using the storage object where this performance-service-level is applied. Modifiable field.
    required: false
    state_supported: present
  expected_latency:
    description:
    - Target latency, in milliseconds, the clients may observe for read/write operations on the Storage object. Modifiable field.
    required: false
    state_supported: present
  name:
    description:
    - Name of the performance-service-level.
    required: true
    state_supported: present,absent
  peak_iops_allocation_policy:
    description:
    - Peak IOPS allocation policy to be used. Modifiable field.
    choices: ['USED_SPACE', 'ALLOCATED_SPACE', 'used_space', 'allocated_space']
    required: false
    state_supported: present
  peak_iops_per_tb:
    description:
    - Maximum number of IOPS, per terabyte (TB) of storage space, that a client can perform on the storage object where this performance-service-level is applied. Modifiable field.
    required: false
    state_supported: present
  rename:
    description:
    - New name of the performance-service-level, to change. Modifiable field.
    required: false
    state_supported: present
'''

EXAMPLES = '''
---
    - name: Manage performance-service-level
      aiqum_performance_service_levels:
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
        state=present
        absolute_min_iops=175
        expected_latency= 10
        expected_iops_per_tb=128
        name=demo_psl_ansible
        peak_iops_allocation_policy=USED_SPACE
        peak_iops_per_tb=512
      register : jsonResult

'''
RETURN = '''
    "msg": {
    "changed": true,
    "failed": false,
    "meta": {<has the job-response returned from AIQUM server> },
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
    'content-type': 'application/json'
}

class NetAppAIQUMPSLs(object):
    """Class with performance-service-level operations"""

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
            "name" : {"required": True, "type": "str"},
            "absolute_min_iops" : {"required":False , "type": "int"},
            "description" : {"required": False, "type": "str"},
            "expected_iops_per_tb" : {"required": False, "type": "int"},
            "expected_latency" : {"required": False, "type": "int"},
            "peak_iops_allocation_policy" : {"required": False,
                                             "choices": ['USED_SPACE', 'ALLOCATED_SPACE', 'used_space', 'allocated_space'],
                                             "type": 'str'},
            "peak_iops_per_tb" : {"required": False, "type": "int"},
            "rename" : {"required": False, "type": "str"},
            }

        global module
        module  = AnsibleModule(argument_spec=fields)

        # Active IQ Unified Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global job_url_path
        global resource_name
        global server_details
        global storage_provider_url_path
        global url_path

        api_host                  = module.params["hostip"]
        api_port                  = module.params["port"]
        api_user_name             = module.params["user"]
        api_user_password         = module.params["password"]
        job_url_path              = "/api/v2/management-server/jobs/"
        resource_name             = "performance-service-levels"
        server_details            = "https://"+api_host+":"+api_port
        storage_provider_url_path = "/api/v2/storage-provider/"
        url_path                  = storage_provider_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATE
        global KEY
        global NUM_RECORDS
        global PRESENT
        global RETRY_COUNT

        ABSENT      = "absent"
        JOB_KEY     = "key"
        JOB_STATE   = "completed"
        KEY         = "key"
        NUM_RECORDS = "num_records"
        PRESENT     = "present"
        RETRY_COUNT = 300

        # Properties details
        global absolute_min_iops
        global description
        global expected_iops_per_tb
        global expected_latency
        global name
        global peak_iops_allocation_policy
        global peak_iops_per_tb
        global rename
        global key

        absolute_min_iops           = module.params["absolute_min_iops"]
        description                 = module.params["description"]
        expected_iops_per_tb        = module.params["expected_iops_per_tb"]
        expected_latency            = module.params["expected_latency"]
        name                        = module.params["name"]
        peak_iops_allocation_policy = module.params["peak_iops_allocation_policy"]
        peak_iops_per_tb            = module.params["peak_iops_per_tb"]
        rename                      = module.params["rename"]

    def post(self):
        global resource_url_path
        global url_path
        payload={}
        latency={}
        iops={}
        if absolute_min_iops != None:
            iops['absolute_min_iops'] = absolute_min_iops
        if expected_iops_per_tb != None:
            iops['expected_iops_per_tb'] = expected_iops_per_tb
        if expected_latency != None:
            latency['expected'] = expected_latency
            payload['latency'] = latency
        if name != None:
            payload['name']=name
        if peak_iops_allocation_policy != None:
            iops['peak_iops_allocation_policy']=peak_iops_allocation_policy.lower()
        if peak_iops_per_tb != None:
            iops['peak_iops_per_tb'] = peak_iops_per_tb
        if description != None:
            payload['description'] = description
        if iops != None:
            payload['iops'] = iops
        response = requests.post(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def delete(self):
        global url_path
        url_path += "/" + key
        response = requests.delete(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def patch(self):
        global url_path
        payload={}
        iops={}
        latency={}
        if absolute_min_iops != None:
            iops['absolute_min_iops'] = absolute_min_iops
        if expected_iops_per_tb != None:
            iops['expected_iops_per_tb'] = expected_iops_per_tb
        if expected_latency != None:
            latency['expected'] = expected_latency
            payload['latency'] = latency
        if peak_iops_allocation_policy != None:
            iops['peak_iops_allocation_policy'] = peak_iops_allocation_policy.lower()
        if peak_iops_per_tb != None:
            iops['peak_iops_per_tb'] = peak_iops_per_tb
        if description != None:
            payload['description'] = description
        if iops != None:
            payload['iops'] = iops
        if name != None:
            payload['name']=name
        if rename != None:
            payload['name']=rename
        url_path += "/" + key
        response = requests.patch(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response

    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either performance-service-level has been already deleted or Please provide a valid performance-service-level name")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                parse_state_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    url_psl = server_details + url_path + "?name=" + name
    key = get_resource_key(url_psl)
    if key != None:
        return True
    else:
        return False

def get_resource_key(url):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if(response.status_code==200):
        response_json = response.json()
        if response_json.get('NUM_RECORDS') == 0 :
            return None
        records = response_json.get('records')
        for record in records:
            resource_key = record.get(KEY)
            return resource_key
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def parse_state_response(response):
    """ check the response body and take necessary action according to status code """
    if(response.status_code==202):
        response_json = response.json()
        job = response_json.get('job')
        job_key = job.get(JOB_KEY)
        job_response = get_job_status(job_key)
        module.exit_json(changed=True,meta=job_response)
    elif(response.status_code==200):
        module.exit_json(changed=True,meta="job successful")
    elif(response.status_code==201):
        module.exit_json(changed=True,meta=response.json())
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def get_job_status(job_key):
    """ verify job status and wait for job to complete """
    # to avoid infinite wait condition, in case of AIQUM takes more than 300 sec to respond.
    global job_url_path
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if (response.status_code==200):
            json_response=response.json()
            if (json_response['state'] == JOB_STATE) :
                break
            RETRY_COUNT -= 1
            time.sleep(1)
        else:
            json_response=response.json()
            break
    return json_response

def main():
    """Apply performance-service-level operations from playbook"""
    obj = NetAppAIQUMPSLs()
    obj.apply()

if __name__ == '__main__':
    main()
