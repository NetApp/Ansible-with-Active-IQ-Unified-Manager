#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_igroups
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed igroups.
description:
    - Create, update or delete Igroup on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  cluster:
    description:
    - Name of the cluster.
    required: true
    state_supported: present,absent
  initiators:
    description:
    - List of initiators belonging to this group. Modifiable field.
    required: false
    state_supported: present
  name:
    description:
    - Name of the initiator group.
    required: true
    state_supported: present,absent
  os_type:
    description:
    - The operating system of the initiator group. Modifiable field.
    choices:  ['AIX', 'HPUX', 'HYPER_V', 'LINUX', 'NETWARE', 'OPENVMS', 'SOLARIS', 'VMWARE', 'WINDOWS', 'DEFAULAT', 'XEN']
    required: false
    state_supported: present
  rename:
    description:
    - New name of the igroup, to change. Modifiable field.
    required: false
    state_supported: present
  svm:
    description:
    - Name of the SVM object.
    required: true
    state_supported: present,absent
  type:
    description:
    - Type of the initiator group.
    choices:  [fcp, iscsi, mixed]
    required: false
    state_supported: present
'''

EXAMPLES = '''
---
    - name: Manage Igroup
      nslm_igroups:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        name=demo_igroup_ansible
        os_type=AIX
        type=MIXED
        svm=test_vserver
        cluster=netapp-aff300-01-02
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

class NetAppNSLMIgroups(object):
    """Class with igroup operations"""

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
            "cluster" : {"required": True, "type": "str"},
            "initiators" : {"required": False, "type": "list"},
            "name" : {"required": True, "type": "str"},
            "os_type" : {"required": False, "type": "str"},
            "rename" : {"required": False, "type": "str"},
            "svm" : {"required": True, "type": "str"},
            "type" :  {"required": False, "type": "str"},
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
        resource_name           = "igroups"
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
        global cluster
        global initiators
        global key
        global name
        global os_type
        global rename
        global svm
        global svm_key
        global type

        cluster     = module.params["cluster"]
        initiators  = module.params["initiators"]
        name        = module.params["name"]
        os_type     = module.params["os_type"]
        rename      = module.params["rename"]
        svm         = module.params["svm"]
        type        = module.params["type"]

    def post(self):
        global resource_url_path
        global url_path
        payload={}
        initiators_list=[]
        if initiators != None:
            for init in initiators:
                initiators_list.append(init)
            payload['initiators']=initiators_list
        if name != None:
            payload['name']=name
        if os_type != None:
            payload['os_type']=os_type
        payload['svm_key']= svm_key
        if type != None:
            payload['type']= type
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response

    def delete(self):
        global url_path
        url_path+="/"+key
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def patch(self):
        global url_path
        payload={}
        initiators_list=[]
        if initiators != None:
            for init in initiators:
                initiators_list.append(init)
            payload['initiators']=initiators_list
        if rename != None:
            payload['name']=rename
        if os_type != None:
            payload['os_type']=os_type
        url_path+="/"+key
        response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either Igroup has been already deleted or Please provide a valid  Cluster name,SVM name,Igroup name.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                parse_state_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    global svm_key
    if (cluster != None and svm != None and name != None):
        url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
        cluster_key = get_resource_key(url_cluster)
        if cluster_key == None:
            module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
        url_svm = server_details + resource_url_path + "svms?cluster_key="+cluster_key + "&filter=name eq " + svm
        svm_key = get_resource_key(url_svm)
        if svm_key == None:
            module.exit_json(changed=False,meta="Please provide a valid SVM name.")
        url_igroup = server_details + resource_url_path + resource_name + "?svm_key="+svm_key
        key = parse_for_resource_key(url_igroup, name)
        if key == None:
            return False
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

def get_resource_key(url):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if(response.status_code==200):
        response_json = response.json()
        if response_json.get('num_records') == 0:
            return None
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
    '''Apply Igroup operations from playbook'''
    obj = NetAppNSLMIgroups()
    obj.apply()

if __name__ == '__main__':
    main()
