ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_file_shares
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed file-shares.
description:
    - Create, update or delete file-share on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  access_control:
    description:
    - Provide access to the file-share.
    required: false
    state_supported: present
    acl:
      description:
      - List of CIFS share access controls. Modifiable field.
      required: false
      state_supported: present
      permission:
        description:
        - Permissions to be allowed for the user or group. Modifiable field.
        choices: ['NO_ACCESS', 'READ', 'CHANGE', 'FULL_CONTROL']
        required: false
        state_supported: present
      user_or_group:
        description:
	- User or group of the Active Directory to provide access. To provide access to everyone, use 'everyone' as the input. Modifiable field.
        required: false
        state_supported: present
    attach_active_directory:
      description:
      - Search active directory associated with SVM and provide as input to Fileshare.
      required: false
      state_supported: present
    export_policy:
      description:
      - Export policy for the file-share. Optional for NFS share creation.
      required: false
      state_supported: present
      rules:
        description:
        - List of export rules. Modifiable field.
        required: false
        state_supported: present
        allowed_clients:
          description:
          - Client match specifications. Modifiable field.
          required: false
          state_supported: present
        cifs:
          description:
          - Enable/Disable CIFS protocol. One of the protocol must be enabled - NFS or CIFS. Modifiable field.
          required: false
          state_supported: present
          index:
            description:
            - Precedence of the export rule. Modifiable field.
            required: false
            state_supported: present
          nfsv3:
            description:
            - Enable/Disable NFS v3 protocol. NFS must be enabled. Modifiable field.
            required: false
            state_supported: present
          nfsv4:
            description:
            - Enable/Disable NFS v4 protocol. NFS must be enabled. Modifiable field.
            required: false
            state_supported: present
          read_only_rule:
            description:
            - Read-only rule specified as comma-separated values. Modifiable field.
            choices: [SYS, NTLM, KERBEROS5, KERBEROS5I, KERBEROS5P, NONE, NEVER, ANY]
            required: false
            state_supported: present
          read_write_rule:
            description:
            - Read-write rule specified as comma-separated values. Modifiable field.
            choices: [SYS, NTLM, KERBEROS5, KERBEROS5I, KERBEROS5P, NONE, NEVER, ANY]
            required: false
            state_supported: present
  aggregate:
    description:
    - Name of the aggregate to be used.
    required: false
    state_supported: present
  capacity:
    description:
    - Capacity of the file-share in MB. Modifiable field.
    required: false
    state_supported: present
  capacity_unit:
    description:
    - Capacity unit used to interpret the capacity parameter. Modifiable field.
    choices: ['mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb']
    required: false
    state_supported: present
  cluster:
    description:
    - Name of the cluster.
    required: true
    state_supported: present,absent
  mountpoint:
    description:
    - Mount point of the file-share. Should be prefixed with '/'.
    required: false
    state_supported: present
  name:
    description:
    - Name of the file-share.
    required: true
    state_supported: present,absent
  operational_state:
    description:
    - State of the file-share. Modifiable field.
    choices:  ['ONLINE', 'OFFLINE']
    required: false
    state_supported: present
  performance_service_level:
    description:
    - Unique identifier of the performance service level. Modifiable field.
    required: false
    state_supported: present
  storage_efficiency_policy:
    description:
    - Unique identifier of the storage efficiency policy. Modifiable field.
    required: false
    state_supported: present
  svm:
    description:
    - Name of the SVM.
    required: true
    state_supported: present,absent
'''
EXAMPLES = '''
---
    - name: Manage file-share
      nslm_file_shares:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        name=demo_fileshare_ansible
        capacity=500
        performance_service_level=Value
        svm=demo_vserver
        cluster=netapp-aff300-01-02
        mountpoint: /demo_fileshare_ansible
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
warnings.filterwarnings('ignore')

HEADERS = {
    'content-type': 'application/hal+json'
}

class NetAppNSLMFileshares(object):
    """Class with file-share operations"""

    def __init__(self):
        """Initialize module parameters"""
        self._capacity_unit_map = dict(
            mb=1,
            gb=1024,
            tb=1024 ** 2,
            pb=1024 ** 3,
            eb=1024 ** 4,
            zb=1024 ** 5,
            yb=1024 ** 6
        )
        fields = {
            'state': {
                'required': True,
                'choices': ['present', 'absent'],
                'type': 'str'
            },
            'hostip': {'required': True, 'type': 'str'},
            'password': {'required':True, 'type': 'str'},
            'port': {'required': True, 'type': 'str'},
            'user': {'required': True, 'type': 'str'},
            'aggregate': {'required': False, 'type': 'str'},
            'allowed_clients': {'required': False, 'type': 'str'},
            "capacity" : {"required": False, "type": "float"},
            "capacity_unit" : {"required": False,
                               "choices": ['mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'],
                               "type": 'str'
                               },
            'cifs': {'required': False, 'type': 'bool'},
            'cluster': {'required': True, 'type': 'str'},
            'index': {'required': False, 'type': 'int'},
            'mountpoint': {'required': False, 'type': 'str'},
            'name': {'required': True, 'type': 'str'},
            'nfsv3': {'required': False, 'type': 'bool'},
            'nfsv4': {'required': False, 'type': 'bool'},
            'operational_state': {'required': False,
                                  "choices": ['ONLINE','OFFLINE'],
                                  'type': 'str'
                                 },
            'performance_service_level': {'required': False, 'type': 'str'},
            'permission': {'required': False, 'type': 'str'},
            'read_only_rule': {'required': False, 'type': 'list'},
            'read_write_rule': {'required': False, 'type': 'list'},
            'storage_efficiency_policy': {'required': False, 'type': 'str'},
            'attach_active_directory': {'required': False, 'type': 'bool'},
            'svm': {'required': True, 'type': 'str'},
            'user_or_group': {'required': False, 'type': 'str'},
        }

        global module
        module = AnsibleModule(argument_spec=fields)

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
        api_port                = module.params['port']
        api_user_name           = module.params['user']
        api_user_password       = module.params['password']
        job_url_path            = "/api/management-server/jobs/"
        resource_name           = "file-shares"
        resource_url_path       = "/api/storage-provider/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = resource_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATUS
        global PRESENT
        global RETRY_COUNT
        global UNASSIGNED

        ABSENT      = "absent"
        JOB_KEY     = "job_key"
        JOB_STATUS  = "COMPLETED"
        PRESENT     = "present"
        RETRY_COUNT = 300
        UNASSIGNED  = "Unassigned"

        # Properties details
        global aggregate
        global allowed_clients
        global capacity
        global capacity_in_mb
        global capacity_unit
        global cluster
        global cifs
        global fail_response
        global index
        global key
        global name
        global nfsv3
        global nfsv4
        global mountpoint
        global operational_state
        global performance_service_level
        global permission
        global read_only_rule
        global read_write_rule
        global storage_efficiency_policy
        global svm
        global attach_active_directory
        global user_or_group
        global json_response

        aggregate                 = module.params['aggregate']
        allowed_clients           = module.params['allowed_clients']
        capacity                  = module.params["capacity"]
        capacity_unit             = module.params["capacity_unit"]
        cifs                      = module.params['cifs']
        cluster                   = module.params['cluster']
        index                     = module.params['index']
        mountpoint                = module.params['mountpoint']
        name                      = module.params['name']
        nfsv3                     = module.params['nfsv3']
        nfsv4                     = module.params['nfsv4']
        operational_state         = module.params['operational_state']
        performance_service_level = module.params['performance_service_level']
        permission                = module.params['permission']
        read_only_rule            = module.params['read_only_rule']
        read_write_rule           = module.params['read_write_rule']
        storage_efficiency_policy = module.params['storage_efficiency_policy']
        svm                       = module.params['svm']
        attach_active_directory   = module.params['attach_active_directory']
        user_or_group             = module.params['user_or_group']

        # converting capacity_unit to mb to feed NSLM server
        if capacity_unit != None:
            capacity_in_mb = capacity * self._capacity_unit_map[capacity_unit]
        else:
            capacity_in_mb = capacity

    def post(self):
        global url_path
        global resource_url_path
        access_control={}
        acl=[]
        acl_payload={}
        export_policy={}
        rules=[]
        rules_payload={}
        read_only_rule_list=[]
        read_write_rule_list=[]
	payload={}

	if capacity != None:
	    payload['capacity_in_mb']=capacity_in_mb
	if mountpoint != None:
	    payload['mountpoint']=mountpoint
        if name != None:
            payload['name']=name
        if cluster != None:
            url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
            cluster_key = get_resource_key(url_cluster)
            if cluster_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
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
            if svm_key ==None:
                module.exit_json(changed=False,meta="Please provide a valid SVM name.")
            payload['svm_key']= svm_key
        if attach_active_directory != None and attach_active_directory == True:
            if cluster != None:
                url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
                cluster_key = get_resource_key(url_cluster)
                if cluster_key == None:
                    module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
            else:
                    module.exit_json(changed=False,meta="Please provide a Cluster name.")
            url_svm = server_details + resource_url_path +  "svms?cluster_key=" + cluster_key
            svm_key = parse_for_resource_key(url_svm, svm)
            if svm_key ==None:
                module.exit_json(changed=False,meta="Please provide a valid SVM name.")
	    url_active_directory = server_details + resource_url_path +  "active-directories?svm_key=" + svm_key
	    active_directory_key = get_resource_key(url_active_directory)
	    if active_directory_key == None:
                module.exit_json(changed=False,meta="Please provide a SVM having active directory configured.")
            payload['active_directory_key']= active_directory_key
        if aggregate != None:
            url_aggregate = server_details + resource_url_path +  "aggregates?cluster_key=" + cluster_key
            aggregate_key = parse_for_resource_key(url_aggregate, aggregate)
            if aggregate_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Aggregate name.")
            payload['aggregate_key']=aggregate_key
        if performance_service_level != None:
            url_psl = server_details + resource_url_path +  "performance-service-levels"
            performance_service_level_uuid = parse_for_resource_key(url_psl, performance_service_level)
            if performance_service_level_uuid == None:
                module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload['performance_service_level_uuid']=performance_service_level_uuid
        if storage_efficiency_policy != None:
            url_sep = server_details + resource_url_path +  "storage-efficiency-policies"
            storage_efficiency_policy_uuid = parse_for_resource_key(url_sep, storage_efficiency_policy)
            if storage_efficiency_policy_uuid == None:
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            payload['storage_efficiency_policy_uuid']=storage_efficiency_policy_uuid
        if permission != None:
            acl_payload['permission']= permission
        if user_or_group != None:
            acl_payload['user_or_group']= user_or_group
        if acl_payload :
            acl.append(acl_payload)
            access_control['acl']= acl
        if allowed_clients != None:
            rules_payload['allowed_clients']=allowed_clients
        if cifs != None:
            rules_payload['cifs']=cifs
        if index != None:
            rules_payload['index']=index
        if nfsv3 != None:
            rules_payload['nfsv3']=nfsv3
        if nfsv4 != None:
            rules_payload['nfsv4']=nfsv4
        if read_only_rule != None:
            for read_only in read_only_rule:
                read_only_rule_list.append(read_only)
            rules_payload['read_only_rule']=read_only_rule_list
        if read_write_rule != None:
            for read_write in read_write_rule:
                read_write_rule_list.append(read_write)
            rules_payload['read_write_rule']=read_write_rule_list
        if rules_payload:
            rules.append(rules_payload)
            export_policy['rules']= rules
            access_control['export_policy']=export_policy
        if access_control :
            payload['access_control']=access_control
        response = requests.post(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response

    def delete(self):
        global url_path
        url_path+='/' + key
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def patch(self):
        global url_path
        access_control={}
        acl=[]
        acl_payload={}
        export_policy={}
        rules=[]
        global fail_response
        fail_response=None
        patch_response_key=[]
        rules_payload={}
        read_only_rule_list=[]
        read_write_rule_list=[]
        payload={}
        url_path+="/"+key
        # fetching file-share details and updating multiple values from user input
        file_share_response = requests.get(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        file_share_json = file_share_response.json()
        if capacity != None and capacity_in_mb != file_share_json['capacity_total']:
            payload.clear()
            payload['capacity_in_mb']=capacity_in_mb
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if performance_service_level != None and performance_service_level != file_share_json['assigned_performance_service_level']['name']:
            if performance_service_level == UNASSIGNED:
                performance_service_level_uuid = UNASSIGNED
            else:
                url_psl = server_details + resource_url_path +  "performance-service-levels"
                performance_service_level_uuid = parse_for_resource_key(url_psl, performance_service_level)
                if (performance_service_level_uuid == None):
                    module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload.clear()
            payload['performance_service_level_uuid']=performance_service_level_uuid
            module.log(msg='PSL PAYLOAD:'+str(payload))
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if storage_efficiency_policy != None and storage_efficiency_policy != file_share_json['assigned_storage_efficiency_policy']['name']:
            url_sep = server_details + resource_url_path +  "storage-efficiency-policies"
            storage_efficiency_policy_uuid = parse_for_resource_key(url_sep, storage_efficiency_policy)
            if (storage_efficiency_policy_uuid == None):
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            payload.clear()
            payload['storage_efficiency_policy_uuid']=storage_efficiency_policy_uuid
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if permission != None:
            acl_payload['permission']= permission
        if user_or_group != None:
            acl_payload['user_or_group']= user_or_group
        if acl_payload :
            acl.append(acl_payload)
            access_control['acl']= acl
            payload.clear()
            payload['access_control']=access_control
            module.log(msg='PSL PAYLOAD:'+str(payload))
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if allowed_clients != None:
            rules_payload['allowed_clients']=allowed_clients
        if cifs != None:
            rules_payload['cifs']=cifs
        if index != None:
            rules_payload['index']=index
        if nfsv3 != None:
            rules_payload['nfsv3']=nfsv3
        if nfsv4 != None:
            rules_payload['nfsv4']=nfsv4
        if read_only_rule != None:
            for read_only in read_only_rule:
                read_only_rule_list.append(read_only)
            rules_payload['read_only_rule']=read_only_rule_list
        if read_write_rule != None:
            for read_write in read_write_rule:
                read_write_rule_list.append(read_write)
            rules_payload['read_write_rule']=read_write_rule_list
        if rules_payload:
            rules.append(rules_payload)
            export_policy['rules']= rules
            access_control.clear()
            access_control['export_policy']=export_policy
            payload.clear()
            payload['access_control']=access_control
            module.log(msg='PSL PAYLOAD:'+str(payload))
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if operational_state != None:
            payload.clear()
            payload['operational_state']=operational_state
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
            module.exit_json(changed=True, failed=False, meta=status)
        else:
            module.exit_json(changed=False, failed=False, meta="no action to perform")

    def apply(self):
        # Actions
        if module.params["state"] == ABSENT:
            if exist():
                response = self.delete()
                parse_state_response(response)
            else:
                module.exit_json(changed=False,meta="File-share has been already deleted or provide a valid file-share key/Cluster name,SVM name,file-share name.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                self.parse_patch_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    if (cluster != None and svm != None and name != None):
        url_fs = server_details + url_path + "?filter=cluster eq "+cluster +", svm eq "+svm +", name eq "+name
        key = get_resource_key(url_fs)
        if (key == None):
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
    global job_url_path
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
    """Apply File-share operations from playbook"""
    obj = NetAppNSLMFileshares()
    obj.apply()


if __name__ == '__main__':
    main()
