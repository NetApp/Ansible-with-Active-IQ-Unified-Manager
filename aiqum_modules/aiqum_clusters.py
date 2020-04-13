#!/usr/bin/python
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: aiqum_clusters
author:
    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)
short_description: Active IQ Unified Manager(AIQUM) managed clusters.
description:
     - Add, update or delete cluster on Active IQ Unified Manager(AIQUM).
version_added: "2.9.1"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  cluster_address:
    description:
    - Hostname or IP address of the cluster.
    required: true
    state_supported: present,absent
  cluster_password:
    description:
    - Password for accessing the cluster.
    required: false
    state_supported: present
  cluster_port:
    description:
    - Port for accessing the cluster.
    required: false
    state_supported: present
  cluster_protocol:
    description:
    - Protocol for accessing the cluster.
    required: false
    state_supported: present
  cluster_username:
    description:
    - Username for accessing the cluster.
    required: false
    state_supported: present

'''

EXAMPLES = '''
---
    - name: Manage Cluster
      aiqum_clusters:
        state=present
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
        cluster_address=10.11.12.13
        cluster_password=demo_password
        cluster_port=443
        cluster_protocol=https
        cluster_username=demo_username
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

class NetAppAIQUMClusters(object):
    """Class with cluster operations"""

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
            "cluster_address" : {"required": True, "type": "str"},
            "cluster_password" : {"required": False, "type": "str"},
            "cluster_port" : {"required": False, "type": "int"},
            "cluster_protocol" : {"required": False, "type": "str"},
            "cluster_username" : {"required": False, "type": "str"},
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
        global admin_url_path
        global server_details
        global url_path

        api_host                    = module.params["hostip"]
        api_port                    = module.params["port"]
        api_user_name               = module.params["user"]
        api_user_password           = module.params["password"]
        job_url_path                = "/api/v2/management-server/jobs/"
        resource_name               = "clusters"
        admin_url_path              = "/api/v2/admin/datasources/"
        server_details              = "https://"+api_host+":"+api_port
        url_path                    = admin_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATE
        global JOB_STATUS
        global KEY
        global NUM_RECORDS
        global PRESENT
        global RETRY_COUNT

        ABSENT      = "absent"
        JOB_KEY     = "key"
        JOB_STATE   = "completed"
        JOB_STATUS  = "normal"
        KEY         = "key"
        NUM_RECORDS = "num_records"
        PRESENT     = "present"
        RETRY_COUNT = 300

        # Properties details
        global cluster_address
        global cluster_password
        global cluster_port
        global cluster_protocol
        global cluster_username
        global key

        cluster_address     = module.params["cluster_address"]
        cluster_password    = module.params["cluster_password"]
        cluster_port        = module.params["cluster_port"]
        cluster_protocol    = module.params["cluster_protocol"]
        cluster_username    = module.params["cluster_username"]



    def post(self):
        global url_path
        payload={}

        if cluster_address != None:
            payload['address']=cluster_address
        if cluster_password != None:
            payload['password']=cluster_password
        if cluster_port != None:
            payload['port']=cluster_port
        if cluster_protocol != None:
            payload['protocol']=cluster_protocol
        if cluster_username != None:
            payload['username']=cluster_username
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def delete(self):
        global url_path
        url_path+="/"+key
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response


    def patch(self):
        global url_path
        url_path+="/"+key
        payload={}

        if cluster_username != None:
            payload['username']=cluster_username
        if cluster_password != None:
            payload['password']=cluster_password
        response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either Cluster has been already deleted or Please provide a valid Cluster IP.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                parse_state_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    # validate the given cluster name
    if cluster_address != None:
        url_cluster = server_details + url_path
        key = get_resource_key(url_cluster, cluster_address)

    if key == None:
        return False
    return True


def parse_state_response(response):
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

def get_resource_key(url, resource):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        response_json = response.json()
        if response_json.get(NUM_RECORDS) == 0:
            return None
        records = response_json.get('records')
        for record in records:
            if record.get('address') == resource:
                resource_key = record.get(KEY)
                return resource_key
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def main():
    """Apply cluster operations from playbook"""
    obj = NetAppAIQUMClusters()
    obj.apply()

if __name__ == '__main__':
    main()
