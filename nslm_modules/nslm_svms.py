#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_svms
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed svms.
description:
     - Create, update or delete SVMs on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  aggregate:
    description:
    - List of aggregates assigned to SVM for volume operations. Modifiable field.
    required: false
    state_supported: present
  allowed_protocols:
    description:
    - Allowed protocols for the SVM. Modifiable field.
    choices: [nfs, cifs, fcp, iscsi, ndmp, nvme]
    required: false
    state_supported: present
  cluster:
    description:
    - Cluster to which the SVM belongs..
    required: true
    state_supported: present,absent
  ip_space_name:
    description:
    - Specifies the Network IPspace of the SVM.
    required: false
    state_supported: present
  name:
    description:
    - Name of the SVM to be created.
    required: true
    state_supported: present,absent
  root_volume_aggregate:
    description:
    - Root volume aggregate of the SVM. Optional for ONTAP 9.2 and later. Mandatory for ONTAP 9.1.
    required: false
    state_supported: present
  root_volume_security_style:
    description:
    - Security style of the root volume.
    choices: ['mixed', 'ntfs', 'unix']
    required: false
    state_supported: present

'''

EXAMPLES = '''
---
    - name: Manage SVM
      nslm_svms:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        cluster=netapp-aff300-01-02
        name=demo_vserver
        allowed_protocols=nfs
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

class NetAppNSLMSVMs(object):
    """Class with svms operations"""

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
            "aggregate" : {"required": False, "type": "list"},
            "allowed_protocols" : {"required": False, "type": "list"},
            "cluster" : {"required": True, "type": "str"},
            "ip_space_name" : {"required": False, "type": "str"},
            "name" : {"required": True, "type": "str"},
            "root_volume_aggregate" : {"required": False, "type": "str"},
            "root_volume_security_style" : {"required": False,
                                       "choices": ['mixed', 'ntfs', 'unix'],
                                       "type": "str"},
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
        resource_name           = "svms"
        resource_url_path       = "/api/storage-provider/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = "/api/storage-provider/"+resource_name

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
        global aggregate
        global allowed_protocols
        global cluster
        global cluster_key
        global ip_space_name
        global isPost
        global isDelete
        global key
        global name
        global root_volume_aggregate
        global root_volume_security_style
        global fail_response
        global json_response

        aggregate                  = module.params["aggregate"]
        allowed_protocols          = module.params["allowed_protocols"]
        cluster                    = module.params["cluster"]
        ip_space_name              = module.params["ip_space_name"]
        name                       = module.params["name"]
        root_volume_aggregate      = module.params["root_volume_aggregate"]
        root_volume_security_style = module.params["root_volume_security_style"]

        isPost = 0
        isDelete = 0

    def post(self):
        global url_path
        payload={}
        aggregate_key_list=[]
        allowed_protocols_list=[]
        if aggregate != None:
            for aggr in aggregate:
                url_aggregate = server_details + resource_url_path + "aggregates?cluster_key="+cluster_key
                aggregate_key = parse_for_resource_key(url_aggregate, aggr)
                aggregate_key_list.append(aggregate_key)
            payload['aggregate_keys']=aggregate_key_list
        if allowed_protocols != None :
            for protocols in allowed_protocols:
                allowed_protocols_list.append(protocols)
            payload['allowed_protocols']=allowed_protocols_list
        if cluster != None:
            payload['cluster_key']= cluster_key
        if ip_space_name != None:
            payload['ip_space_name']=ip_space_name
        if name != None:
            payload['name']=name
        if root_volume_aggregate != None:
            payload['root_volume_aggregate']=root_volume_aggregate
        if root_volume_security_style != None:
            payload['root_volume_security_style']=root_volume_security_style

        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        return response


    def delete(self):
        url = url_path+"/"+key
        response = requests.delete(server_details+url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def patch(self):
        global cluster_key
        global url_path
        global fail_response
        fail_response=None
        url_path +="/"+key
        payload={}
        aggregate_key_list=[]
        allowed_protocols_list=[]
        patch_response_key=[]
        if aggregate != None:
            if cluster != None:
                url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
                cluster_key = get_resource_key(url_cluster)
                if cluster_key == None:
                    module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
            for aggr in aggregate:
                url_aggregate = server_details + resource_url_path + "aggregates?cluster_key="+cluster_key
                aggregate_key = parse_for_resource_key(url_aggregate, aggr)
                aggregate_key_list.append(aggregate_key)
            payload.clear()
            payload['aggregate_keys']=aggregate_key_list
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        if allowed_protocols != None:
            for protocols in allowed_protocols:
                allowed_protocols_list.append(protocols)
            payload.clear()
            payload['allowed_protocols']=allowed_protocols_list
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        return patch_response_key

    def parse_patch_response(self, response):
        """ check the patch response body for all the jobs and take necessary action according to status code """
        status=[]
        for job_key in response:
            job_response = get_job_status(job_key)
            if job_response['state'] == "COMPLETED" and job_response['status'] == "NORMAL":
                status.append(" name: "+job_response['name'] +" status: "+ job_response['status'] +" state: " +job_response['state'] + " job key: "+job_response['key'])
            else:
                status.append(job_response)
        if status != None:
            if fail_response != None:
                status.append(fail_response)
            module.exit_json(changed=True, meta=status)
        else:
            module.exit_json(changed=False, meta="no action to perform")

    def apply(self):
        # Actions
        global isPost
        global isDelete
        if module.params["state"] == ABSENT:
            if exist():
                isDelete = 1
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either SVM has been already deleted or Please provide a valid Cluster name, SVM name.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                self.parse_patch_response(response)
            else:
                isPost = 1
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    global cluster_key
    if (cluster != None and name != None):
        url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
        cluster_key = get_resource_key(url_cluster)
        if cluster_key == None:
            module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
        url_svm = server_details + resource_url_path + resource_name+"?cluster_key="+cluster_key + "&filter=name eq " + name
        key = get_resource_key(url_svm)
        if (key == None):
            return False
        return True
    else:
        return False


def parse_state_response(response):
    """ check the response body and take necessary action according to status code """
    if(response.status_code==202):
        job_key = response.json()['job_key']
        if isPost:
            job_response=get_post_job_status(job_key)
        elif isDelete:
            job_response=get_job_status(job_key)
            if job_response['state'] == JOB_STATUS and job_response['status'] == 'NORMAL':
                acquisition_delete()
        else:
            job_response=get_job_status(job_key)
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

def get_post_job_status(job_key):
    """ verify job status and wait for job to complete along with acquisition """
    # to avoid infinite wait condition, in case of NSLM takes more than 300 sec to respond.
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if (response.status_code==200):
            job_response=response.json()
            if (job_response['state'] == JOB_STATUS) :
                if(job_response['status'] == 'NORMAL'):
                    key = get_key_from_job(job_response)
                    acquisition_post(key)
                break
            RETRY_COUNT -= 1
            time.sleep(1)
        else:
            job_response=response.json()
            break
    return job_response

def get_key_from_job(json_response):
    for job_results in json_response['job_results']:
        if (job_results.get('name') == "svmKey"):
            key = job_results.get('value')
            return key

def acquisition_post(key):
    global json_response
    global url_path
    url = server_details+url_path+'/'+key
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    json_response = response.json()
    while('cluster' not in json_response):
        time.sleep(10)
        response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        json_response = response.json()
    return

def acquisition_delete():
    key_present = 1
    url_svm = server_details +url_path
    while(key_present):
        response = requests.get(url_svm, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        if(response.status_code==200):
            response_json = response.json()
            if response_json.get('num_records') != 0:
                embedded = response_json.get('_embedded')
                if any(record['key'] == key for record in embedded['netapp:records']):
                    time.sleep(10)
                else:
                    key_present = 0
        else:
            # Returning error message received from NSLM
            module.exit_json(changed=False,meta=response.json())
    return

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
    """Apply SVM operations from playbook"""
    obj = NetAppNSLMSVMs()
    obj.apply()

if __name__ == '__main__':
    main()
