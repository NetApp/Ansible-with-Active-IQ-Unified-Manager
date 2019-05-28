#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_storage_efficiency_policies
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed storage-efficiency-policies.
description:
     - Create, update or delete storage-efficiency-policy on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  compression:
    description:
    - Specifies whether compression will be applied to the provisioned data and the type of compression. Modifiable field.
    choices: ['INLINE', 'BACKGROUND', 'NONE']
    required: false
    state_supported: present
  deduplication:
    description:
    - Specifies whether deduplication will be applied to the provisioned data and the type of deduplication. Modifiable field.
    choices: ['INLINE', 'BACKGROUND', 'NONE']
    required: false
    state_supported: present
  description:
    description:
    - Description of the storage-efficiency-policy. Modifiable field.
    required: false
    state_supported: present
  name:
    description:
    - Name of the storage-efficiency-policy.
    required: true
    state_supported: present,absent
  rename:
    description:
    - New name of the performance-service-level, to change. Modifiable field.
    required: false
    state_supported: present
  space_thin_provisioned:
    description:
    - Specifies whether to use thin-provisioning for space. Modifiable field.
    required: false
    state_supported: present
'''

EXAMPLES = '''
---
    - name: Manage Storage-Efficiency-Policy
      nslm_storage_efficiency_policies:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        compression=INLINE
        deduplication=INLINE
        description=Storage Efficiency Policy includes technologies such as thin provisioning for the space reserve, deduplication, and data compression that increase storage utilization and decrease storage costs.
        name=demo_sep
        space_thin_provisioned=false
      register : jsonResultPresent

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

class NetAppNSLMStorageEfficiencyPolicies(object):
    """Class with storage-efficiency-policy operations"""

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
            "compression" : {"required": False,
                             "choices": ['INLINE', 'BACKGROUND', 'NONE'],
                             "type": "str"},
            "deduplication" : {"required": False,
                             "choices": ['INLINE', 'BACKGROUND', 'NONE'],
                             "type": "str"},
            "description" : {"required": False, "type": "str"},
            "space_thin_provisioned" : {"required": False, "type": "bool"},
            "rename" : {"required": False, "type": "str"},
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
        resource_name           = "storage-efficiency-policies"
        resource_url_path       = "/api/storage-provider/"
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
        global compression
        global deduplication
        global description
        global name
        global space_thin_provisioned
        global rename
        global uuid

        compression               = module.params["compression"]
        deduplication             = module.params["deduplication"]
        description               = module.params["description"]
        name                      = module.params["name"]
        space_thin_provisioned    = module.params["space_thin_provisioned"]
        rename                    = module.params["rename"]

    def post(self):
        global url_path
        payload={}
        if compression != None:
            payload['compression']=compression
        if deduplication != None :
            payload['deduplication']=deduplication
        if description != None:
            payload['description']= description
        if name != None:
            payload['name']=name
        if space_thin_provisioned != None:
            payload['space_thin_provisioned']=space_thin_provisioned
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def delete(self):
        global url_path
        url_path+="/"+uuid
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response


    def put(self):
        global url_path
        payload={}
        # fetching SEP details and overriding with user input
        sep_response = requests.get(server_details+url_path+"/"+uuid, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        sep_json = sep_response.json()
        if compression != None:
            payload['compression']=compression
        else:
            payload['compression']=sep_json['compression']
        if deduplication != None :
            payload['deduplication']=deduplication
        else:
            payload['deduplication']=sep_json['deduplication']
        if description != None:
            payload['description']= description
        else:
            payload['description']=sep_json['description']
        if name != None:
            payload['name']=name
        if rename != None:
            payload['name']=rename
        if space_thin_provisioned != None:
            payload['space_thin_provisioned']=space_thin_provisioned
        url_path+="/"+uuid
        response = requests.put(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either Storage-efficiency-policy has been already deleted or Please provide a valid Storagge-efficiency-policy uuid.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.put()
                parse_state_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global uuid
    url_sep = server_details + url_path
    uuid = parse_for_resource_key(url_sep, name)
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

def parse_for_resource_key(url, resource_name):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        unique_id=None
        response_json = response.json()
        if response_json.get('num_records') == 0:
            return None
        embedded = response_json.get('_embedded')
        for record in embedded['netapp:records']:
            if record.get('name') == resource_name:
                if record.get('key') != None:
                    unique_id = record.get('key')
                else:
                   unique_id = record.get('uuid')
        if unique_id == None:
            return None
        else:
            return unique_id
    else:
        # Returning error message received from NSLM
        module.exit_json(changed=False,meta=response.json())

def main():
    """Apply Storage-Efficiency-Policy operations from playbook"""
    obj = NetAppNSLMStorageEfficiencyPolicies()
    obj.apply()

if __name__ == '__main__':
    main()
