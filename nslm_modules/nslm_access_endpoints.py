#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_access_endpoints
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed access_endpoints.
description:
     - Create, update or delete Access-endpoint on NetApp Service Level Manager(NSLM).
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
    action_supported: present,absent
  data_protocols:
    description:
    - Comma-separated list of data protocols allowed for access endpoint.
    choices: [nfs, cifs, iscsi, fcp ]
    required: false
    state_supported: present
  fileshare:
    description:
    - Name of file share for which access endpoint needs to be created.
    required: false
    state_supported: present
  gateway:
    description:
    - Gateway for access endpoint. This is optional for CIFS, NFS and iSCSI protocols. This parameter is not required for FCP protocol. Modifiable field.
    required: false
    state_supported: present
  ha_ip_address:
    description:
    - IPv4 address of access endpoint on ha partner node. This parameter is mandatory to create iSCSI access endpoint at ha partner of lun's home node. This parameter is not supported for access endpoint creation at fileshare or SVM level.
    required: false
    state_supported: present
  ip_address:
    description:
    -  IPv4 address of access endpoint. This is mandatory for CIFS, NFS and iSCSI protocol. This parameter is not required for FCP protocol. Modifiable field.
    required: false
    state_supported: present
  lun:
    description:
    - Name of the LUN for which access endpoint needs to be created. Please provide volume name (so lun path can be created to uniquely identify the lun).
    required: false
    state_supported: present
  mtu:
    description:
    - MTU for access endpoint. This is optional for CIFS, NFS and iSCSI protocols. This parameter is not required for FCP protocol.
    required: false
    state_supported: present
  name:
    description:
    - Name of access endpoint. If not provided then it auto generates the name.
    required: true
    state_supported: present,absent
  netmask:
    description:
    - Netmask for access endpoint. This is mandatory for CIFS, NFS and iSCSI protocol. This parameter is not required for FCP protocol.
    required: false
    state_supported: present
  svm:
    description:
    - Name of the SVM object.
    required: true
    action_supported: present,absent
  vlan:
    description:
    - VLAN ID of access endpoint. This is optional for CIFS, NFS and iSCSI protocols. This parameter is not required for FCP protocol.
    required: false
    state_supported: present
  volume:
    description:
    - Name of the volume to pass when user is passing lun name to create a unique path.
    required: false
    state_supported: present
'''

EXAMPLES = '''
---
    - name: Manage Access-endpoint
      nslm_access_endpoints:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        data_protocols=iscsi
        ip_address=10.11.12.13
        name=test_active_directory
        cluster=netapp-aff300-01-02
        svm=test_vserver
        netmask=255.255.255.0
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

class NetAppNSLMAccessendpoints(object):
    """Class with access_endpoint operations"""

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
            "name" : {"required": True, "type": "str"},
            "svm" : {"required": True, "type": "str"},
            "data_protocols" : {"required": False, "type": "list"},
            "fileshare" : {"required": False, "type": "str"},
            "gateway" : {"required": False, "type": "str"},
            "ha_ip_address" : {"required": False, "type": "str"},
            "ip_address" : {"required": False, "type": "str"},
            "lun" : {"required": False, "type": "str"},
            "netmask" : {"required": False, "type": "str"},
            "mtu" : {"required": False, "type": "int"},
            "vlan" :  {"required": False, "type": "int"},
            "volume" : {"required": False, "type": "str"},
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
        resource_name           = "access-endpoints"
        resource_url_path       = "/api/storage-provider/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = resource_url_path+resource_name

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
        global data_protocols
        global fileshare
        global fileshare_key
        global gateway
        global ha_ip_address
        global ip_address
        global key
        global lun
        global lun_key
        global name
        global netmask
        global mtu
        global svm
        global vlan
        global volume

        cluster        = module.params["cluster"]
        data_protocols = module.params["data_protocols"]
        fileshare      = module.params["fileshare"]
        gateway        = module.params["gateway"]
        ha_ip_address  = module.params["ha_ip_address"]
        ip_address     = module.params["ip_address"]
        lun            = module.params["lun"]
        name           = module.params["name"]
        netmask        = module.params["netmask"]
        mtu            = module.params["mtu"]
        svm            = module.params["svm"]
        vlan           = module.params["vlan"]
        volume         = module.params["volume"]

    def post(self):
        global fileshare_key
        global lun_key
        global resource_url_path
        global url_path
        lun_path=None
        payload={}
        data_protocols_list=[]
        if data_protocols != None:
            for protocols in data_protocols:
                data_protocols_list.append(protocols)
            payload['data_protocols']=data_protocols_list
        if fileshare != None:
            if cluster !=None and svm !=None:
                url_fs = server_details + resource_url_path + "file-shares?filter=cluster eq "+cluster + ", svm eq "+svm+", name eq "+fileshare
                fs_key = get_resource_key(url_fs)
                if fs_key == None:
                    module.exit_json(changed=False,meta="Please provide a valid File-share name.")
                payload['fileshare_key']= fs_key
            else:
                module.exit_json(changed=False,meta="Please provide a valid Cluster name and SVM name.")
        if gateway != None:
            payload['gateway']=gateway
        if ha_ip_address != None:
            payload['ha_ip_address']=ha_ip_address
        if ip_address != None :
            payload['ip_address']=ip_address
        if lun != None:
            if volume != None:
                lun_path = "/vol/"+volume+"/"+lun
            else:
                module.exit_json(changed=False,meta="Please provide a volume name.")
            if cluster != None and svm !=None:
                url_lun = server_details + resource_url_path + "luns?filter=cluster eq "+cluster + ", svm eq "+svm+", path eq "+lun_path
                ln_key = get_resource_key(url_lun)
                if ln_key == None:
                    module.exit_json(changed=False,meta="Please provide a valid LUN name.")
                payload['lun_key']=ln_key
            else:
                module.exit_json(changed=False,meta="Please provide a valid Cluster name and SVM name.")
        if mtu != None:
            payload['mtu']=mtu
        payload['name']=name
        if netmask != None:
            payload['netmask']=netmask
        if fileshare == None and lun_path == None:
            payload['svm_key']= svm_key
        if vlan != None:
            payload['vlan']= vlan
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

        if gateway != None:
            payload['gateway']=gateway
        if ip_address != None:
            payload['ip_address']=ip_address
        response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response


    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="Either Access-endpoint has been already deleted or Please provide a valid Cluater name, SVM name, Access-endpont name.")
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
    url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
    cluster_key = get_resource_key(url_cluster)
    if cluster_key == None:
        module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
    url_svm = server_details + resource_url_path + "svms?filter=cluster eq "+cluster_key
    svm_key = parse_for_resource_key(url_svm, svm)
    if svm_key == None:
        module.exit_json(changed=False,meta="Please provide a valid SVM name.")
    url_ad = server_details + url_path + "?resource_key="+svm_key
    key = parse_for_resource_key(url_ad, name)
    if (key == None):
        return False
    return True

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
        if (response_json.get('num_records') == 0) :
            return None
        else:
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
    """Apply Access-endpoint operations from playbook"""
    obj = NetAppNSLMAccessendpoints()
    obj.apply()

if __name__ == '__main__':
    main()
