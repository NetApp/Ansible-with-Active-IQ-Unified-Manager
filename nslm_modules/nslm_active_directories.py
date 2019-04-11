#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_active_directories
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed active-directory.
description:
     - Create active-directory on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present']
    required: true
  cluster:
    description:
    - Name of the cluster.
    required: true
    action_supported: present
  dns:
    description:
    - Fully qualified domain name or IP address of DNS server for the Active Directory.
    required: true
    action_supported: present
  domain:
    description:
    - Domain of the Active Directory.
    required: true
    action_supported: present
  pass_word:
    description:
    - Password for the Active Directory.
    required: true
    action_supported: present
  svm:
    description:
    - The name of the SVM for which you want to create the Active Directory.
    required: true
    action_supported: present
  username:
    description:
    - Username for the Active Directory.
    required: true
    action_supported: present
'''

EXAMPLES = '''
---
    - name: Manage active-directory
      nslm_active_directories:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        cluster=netapp-aff300-01-02
        dns=10.20.30.40
        domain=NETAPP.COM
        pass_word=netapp
        svm=demo_vserver
        username=admin
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

class NetAppNSLMActiveDirectories(object):
    """Class with active-directory operations"""

    def __init__(self):
        """Initialize module parameters"""
        fields = {
            "state" : {
                "required": True,
                    "choices": ['present'],
                    "type": 'str'
                    },
            "hostip" : {"required": True, "type": "str"},
            "port" : {"required": True, "type": "str"},
            "user" : {"required": True, "type": "str"},
            "password" : {"required": True, "type": "str"},
            "cluster" : {"required": True, "type": "str"},
            "dns" : {"required": True, "type": "str"},
            "domain" : {"required": True, "type": "str"},
            "pass_word" : {"required": True, "type": "str"},
            "svm" : {"required": True, "type": "str"},
            "username" : {"required": True, "type": "str"},
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
        resource_name           = "active-directories"
        resource_url_path       = "/api/storage-provider/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = resource_url_path + resource_name

        # Global Constants
        global JOB_KEY
        global JOB_STATUS
        global PRESENT
        global RETRY_COUNT

        JOB_KEY     = "job_key"
        JOB_STATUS  = "COMPLETED"
        PRESENT     = "present"
        RETRY_COUNT = 300

        # Properties details
        global cluster
        global dns
        global domain
        global pass_word
        global svm
        global username
        global json_response

        cluster   = module.params["cluster"]
        dns       = module.params["dns"]
        domain    = module.params["domain"]
        pass_word = module.params["pass_word"]
        svm       = module.params["svm"]
        username  = module.params["username"]


    def post(self):
        global url_path
        payload={}
        if dns != None :
            payload['dns']=dns
        if domain != None:
            payload['domain']=domain
        if pass_word != None:
            payload['password']=pass_word
        if svm != None:
            if cluster != None:
                url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
                cluster_key = get_resource_key(url_cluster)
                if cluster_key == None:
                    module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
            else:
                module.exit_json(changed=False,meta="Please provide a Cluster name.")
            url_svm = server_details + resource_url_path +  "svms?cluster_key=" + cluster_key
            svm_key = parse_for_resource_key(url_svm, svm)
            if (svm_key == None):
                module.exit_json(changed=False,meta="Please provide a valid SVM name.")
            payload['svm_key']= svm_key
        if username != None:
            payload['username']=username
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response

    def apply(self):
        # Actions
        response=self.post()
        parse_action_response(response)

def exist ():
        return False

def parse_action_response(response):
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

def get_resource_key(url):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if(response.status_code==200):
        response_json = response.json()
        if (response_json.get('num_records') == 0) :
            return None
        else:
            embedded = response_json.get('_embedded')
            for record in embedded['netapp:records']:
                resource_key = record.get('key')
                return resource_key
    else:
        # Returning error message received from NSLM
        module.exit_json(changed=False,meta=response.json())

def parse_for_resource_key(url, resource_name):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if(response.status_code==200):
        unique_id=None
        response_json = response.json()
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
    """Apply active-directory operations from playbook"""
    obj = NetAppNSLMActiveDirectories()
    obj.apply()

if __name__ == '__main__':
    main()
