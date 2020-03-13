#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: aiqum_active_directories
author:
    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)
short_description: Active IQ Unified Manager(AIQUM) managed active-directory.
description:
     - Create active-directory on Active IQ Unified Manager(AIQUM).
version_added: "2.9.1"
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
      aiqum_active_directories:
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
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

class NetAppAIQUMActiveDirectories(object):
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

        # Active IQ Unified Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global datacenter_url_path
        global job_url_path
        global resource_name
        global storage_provider_url_path
        global server_details
        global url_path

        api_host                  = module.params["hostip"]
        api_port                  = module.params["port"]
        api_user_name             = module.params["user"]
        api_user_password         = module.params["password"]
        datacenter_url_path       = "/api/v2/datacenter/"
        job_url_path              = "/api/v2/management-server/jobs/"
        resource_name             = "active-directories-mappings"
        storage_provider_url_path = "/api/v2/storage-provider/"
        server_details            = "https://"+api_host+":"+api_port
        url_path                  = storage_provider_url_path + resource_name

        # Global Constants
        global JOB_KEY
        global JOB_STATE
        global KEY
        global NUM_RECORDS
        global PRESENT
        global RETRY_COUNT

        JOB_KEY     = "key"
        JOB_STATE   = "completed"
        KEY         = "key"
        NUM_RECORDS = "num_records"
        PRESENT     = "present"
        RETRY_COUNT = 300

        # Properties details
        global cluster
        global dns
        global domain
        global pass_word
        global svm
        global username

        cluster   = module.params["cluster"]
        dns       = module.params["dns"]
        domain    = module.params["domain"]
        pass_word = module.params["pass_word"]
        svm       = module.params["svm"]
        username  = module.params["username"]


    def post(self):
        global url_path
        payload={}
        svm_payload={}

        if dns != None :
            payload['dns']=dns
        if domain != None:
            payload['domain']=domain
        if pass_word != None:
            payload['password']=pass_word
        svm_payload[KEY]=svm_key
        payload['svm']= svm_payload
        if username != None:
            payload['username']=username
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response

    def apply(self):
        # Actions
        if module.params["state"] == PRESENT:
            if exist():
                module.exit_json(changed=False,meta="Storage VM already has an Active Directory configured.")
            else:
                response=self.post()
                parse_action_response(response)

def exist ():
    global svm_key
    if svm != None:
        if cluster != None:
            url_cluster = server_details + datacenter_url_path + "cluster/clusters?name=" + cluster
            cluster_key = get_resource_key(url_cluster)
            if cluster_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
        else:
            module.exit_json(changed=False,meta="Please provide a Cluster name.")
        url_svm = server_details + datacenter_url_path + "svm/svms?cluster.name="+cluster+"&name="+svm
        svm_key = get_resource_key(url_svm)
        if svm_key == None:
            module.exit_json(changed=False,meta="Please provide a valid SVM name.")
        #check if any active-directory is associated with the given svm
        act_dir_url = server_details+url_path + "?svm.name=" + svm
        act_key = get_resource_key(act_dir_url)
        if act_key == None:
            return False
        return True

def parse_action_response(response):
    """ check the response body and take necessary action according to status code """
    if response.status_code==202:
        job_key = response.json().get('job').get(JOB_KEY)
        job_response = get_job_status(job_key)
        module.exit_json(changed=True,meta=job_response)
    elif response.status_code==200:
        module.exit_json(changed=True,meta="job successful")
    elif response.status_code==201:
        module.exit_json(changed=True,meta=response.json())
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def get_job_status(job_key):
    """ verify job status and wait for job to complete """
    # to avoid infinite wait condition, in case of AIQUM takes more than 300 sec to respond.
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if response.status_code==200:
            json_response=response.json()
            if json_response['state'] == JOB_STATE:
                break
            RETRY_COUNT -= 1
            time.sleep(1)
        else:
            json_response=response.json()
            break
    return json_response

def get_resource_key(url):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        response_json = response.json()
        if response_json.get(NUM_RECORDS) == 0:
            return None
        records = response_json.get('records')
        for record in records:
            resource_key = record.get(KEY)
            return resource_key
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def main():
    """Apply active-directory operations from playbook"""
    obj = NetAppAIQUMActiveDirectories()
    obj.apply()

if __name__ == '__main__':
    main()
