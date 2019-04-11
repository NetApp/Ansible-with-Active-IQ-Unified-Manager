#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_luns
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed luns.
description:
     - Create, update or delete LUN on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  aggregate:
    description:
    - Name of the aggregate, NSLM chooses an aggregate if not provided.
    required: false
    state_supported: present
  capacity:
    description:
    - Capacity of the LUN, default capacity_unit is MB. Modifiable field.
    required: false
    state_supported: present
  capacity_unit:
    description:
    - Capacity unit is used to interpret capacity parameter, default is MB. Modifiable field.
    choices: ['MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    required: false
    state_supported: present
  cluster:
    description:
    - Name of the cluster.
    required: true
    state_supported: present,absent
  lun_maps:
    description:
    - Mapping of the LUN with Initiator Group.
    required: false
    state_supported: present
    igroup:
      description:
      - Name of the Initiator group. Modifiable field.
      required: false
      state_supported: present
    lun_id:
      description:
      - ID of the LUN. Modifiable field.
      required: false
      state_supported: present
  name:
    description:
    - Name or Label of the LUN.
    required: true
    state_supported: present,absent
  operational_state:
    description:
    - State of the LUN. Modifiable field.
    choices:  ['ONLINE', 'OFFLINE']
    required: false
    state_supported: present
  os_type:
    description:
    - Platform which can use this LUN.
    choices: ['AIX', 'HPUX', 'HYPER_V', 'LINUX', 'NETWARE', 'OPENVMS', 'SOLARIS', 'SOLARIS_EFI', 'VMWARE', 'WINDOWS', 'WINDOWS_2008', 'WINDOWS_GPT', 'XEN']
    required: false
    state_supported: present
  performance_service_level:
    description:
    - Name of the performance service level. Modifiable field.
    required: false
    state_supported: present
  storage_efficiency_policy:
    description:
    - Name of the storage efficiency policy. Modifiable field.
    required: false
    state_supported: present
  svm:
    description:
    - Name of the SVM.
    required: true
    state_supported: present,absent
  volume_name:
    description:
    - Name of the parent volume, if exists then NSLM will use it as a parent volume for the LUN else NSLM will create a parent volume as NSLM_<volume-name> for the LUN.
    required: true
    state_supported: present, absent
'''

EXAMPLES = '''
---
    - name: Manage LUN
      nslm_luns:
        state=present
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        cluster=netapp-aff300-01-02
        svm=demo_vserver
        name=demo_lun_ansible
        performance_service_level=Value
        capacity=50
        capacity_unit=GB
        os_type=AIX
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

class NetAppNSLMLUNs(object):
    """Class with luns operations"""

    def __init__(self):
        """Initialize module parameters"""
        self._capacity_unit_map = dict(
            MB=1,
            GB=1024,
            TB=1024 ** 2,
            PB=1024 ** 3,
            EB=1024 ** 4,
            ZB=1024 ** 5,
            YB=1024 ** 6
        )
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
            "volume_name": {"required": True, "type": "str"},
            "aggregate" : {"required": False, "type": "str"},
            "capacity" : {"required": False, "type": "float"},
            "capacity_unit" : {"required": False,
                               "choices": ['MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                               "type": 'str'
                               },
            "igroup" : {"required": False, "type": "str"},
            "lun_id" : {"required": False, "type": "int"},
            "operational_state" : {"required": False, "type": "str"},
            "os_type" : {"required": False, "type": "str"},
            "performance_service_level" : {"required": False, "type": "str"},
            "storage_efficiency_policy" : {"required": False, "type": "str"},
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
        resource_name           = "luns"
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
        global capacity
        global capacity_in_mb
        global capacity_unit
        global cluster
        global cluster_key
        global igroup
        global key
        global lun_id
        global name
        global operational_state
        global os_type
        global performance_service_level
        global storage_efficiency_policy
        global svm
        global svm_key
        global volume_key
        global volume_name
        global volume_name_tag
        global fail_response

        aggregate                 = module.params["aggregate"]
        name                      = module.params["name"]
        capacity                  = module.params["capacity"]
        capacity_unit             = module.params["capacity_unit"]
        cluster                   = module.params["cluster"]
        igroup                    = module.params["igroup"]
        lun_id                    = module.params["lun_id"]
        operational_state         = module.params["operational_state"]
        os_type                   = module.params["os_type"]
        performance_service_level = module.params["performance_service_level"]
        storage_efficiency_policy = module.params["storage_efficiency_policy"]
        svm                       = module.params["svm"]
        volume_name               = module.params["volume_name"]

        # converting capacity_unit to mb to feed NSLM server
        if capacity_unit != None:
            capacity_in_mb = capacity * self._capacity_unit_map[capacity_unit]
        else:
            capacity_in_mb = capacity

    def post(self):
        global cluster_key
        global resource_url_path
        global url_path
        global svm_key
        payload={}
        lun_maps=[]
        lunmap_payload={}
        if name != None:
            payload['name']=name
        if capacity != None :
            payload['capacity_in_mb']=capacity_in_mb
        if cluster != None:
            # get cluster key for the given cluster name
            url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
            cluster_key = get_resource_key(url_cluster)
            if cluster_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
        if aggregate != None:
            # get aggregate key for the given aggregate name
            url_aggregate = server_details + resource_url_path +  "aggregates?cluster_key=" + cluster_key
            aggregate_key = parse_for_resource_key(url_aggregate, aggregate)
            if (aggregate_key == None):
                module.exit_json(changed=False,meta="Please provide a valid Aggregate name.")
            payload['aggregate_key']=aggregate_key
        if svm != None:
            # get svm key for the given svm name
            url_svm = server_details + resource_url_path +  "svms?cluster_key=" + cluster_key
            svm_key = parse_for_resource_key(url_svm, svm)
            if (svm_key == None):
                module.exit_json(changed=False,meta="Please provide a valid SVM name.")
            payload['svm_key']= svm_key
        if performance_service_level != None:
            # get performace-service-level key for the given performace-service-level name
            url_psl = server_details + resource_url_path +  "performance-service-levels"
            performance_service_level_uuid = parse_for_resource_key(url_psl, performance_service_level)
            if (performance_service_level_uuid == None):
                module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload['performance_service_level_uuid']=performance_service_level_uuid
        if os_type != None:
            payload['os_type']=os_type
        if storage_efficiency_policy != None:
            # get storage-efficiency-policy key for the given storage-efficiency-policy name
            url_sep = server_details + resource_url_path +  "storage-efficiency-policies"
            storage_efficiency_policy_uuid = parse_for_resource_key(url_sep, storage_efficiency_policy)
            if storage_efficiency_policy_uuid == None:
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            payload['storage_efficiency_policy_uuid']=storage_efficiency_policy_uuid
        # check if volume exists then fetch and pass volume_key to NSLM
        # else pass the volume_name_tag parameter to NSLM
        if volume_name != None:
            url_volume = server_details + resource_url_path +  "file-shares?filter=name eq " + volume_name +" , svm eq "+svm+", cluster eq "+cluster
            brownfield_volume_key = get_resource_key(url_volume)

            # fetching existing volume key first check in file-share
            # if not found then fetch from existing LUN
            nslm_volume_name = "NSLM_" + volume_name
            url_volume = server_details + resource_url_path +  "file-shares?filter=name eq " + nslm_volume_name +" , svm eq "+svm+", cluster eq "+cluster
            nslm_volume_key = get_resource_key(url_volume)
            if nslm_volume_key == None:
                url_lun = server_details + url_path + "?filter=cluster eq "+cluster +", svm eq "+svm +", volume eq "+nslm_volume_name
                nslm_volume_key = fetch_volume_key(url_lun, nslm_volume_name)

            if nslm_volume_key != None:
                volume_key = nslm_volume_key
            else:
                volume_key = brownfield_volume_key

            if volume_key == None:
                payload['volume_name_tag'] = volume_name
            else:
                payload['volume_key']= volume_key
        if igroup == None and lun_id != None:
            module.exit_json(changed=False,meta="Please provide a valid igroup name.")
        if igroup != None:
            # get igroup key for the given igroup name
            url_igroup = server_details + resource_url_path +  "igroups?svm_key=" + svm_key
            igroup_key = parse_for_resource_key(url_igroup, igroup)
            if (igroup_key == None):
                module.exit_json(changed=False,meta="Please provide a valid igroup name.")
            lunmap_payload['igroup_key']=igroup_key
            if lun_id != None:
                lunmap_payload['lun_id']=lun_id
            lun_maps.append(lunmap_payload.copy())
            payload['lun_maps']=lun_maps
        response = requests.post(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response


    def delete(self):
        global url_path
        url_path+="/"+key
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response


    def patch(self):
        global fail_response
        fail_response=None
        igroup_name=None
        global url_path
        url_path+="/"+key
        payload={}
        lun_maps=[]
        lunmap_payload={}
        patch_response_key=[]
        # fetching LUN details and updating multiple values from user input
        lun_response = requests.get(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        lun_json = lun_response.json()

        if capacity != None and capacity_in_mb != lun_json['capacity_total']:
            payload.clear()
            payload['capacity_in_mb']=capacity_in_mb
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)


        if performance_service_level != None and performance_service_level != lun_json['assigned_performance_service_level']['name']:
            if performance_service_level == UNASSIGNED:
                performance_service_level_uuid = UNASSIGNED
            else:
                url_psl = server_details + resource_url_path +  "performance-service-levels"
                performance_service_level_uuid = parse_for_resource_key(url_psl, performance_service_level)
                if (performance_service_level_uuid == None):
                    module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload.clear()
            payload['performance_service_level_uuid']=performance_service_level_uuid
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json()[JOB_KEY])
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        if storage_efficiency_policy != None and storage_efficiency_policy != lun_json['assigned_storage_efficiency_policy']['name']:
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

        if igroup == None and lun_id != None:
            module.exit_json(changed=False,meta="Please provide a igroup name.")
        # fetching igroup name from NSLM by GET on igroup key
        if 'lun_maps' in lun_json:
            url_igroup = resource_url_path + "igroups/"+lun_json['lun_maps']['igroup_key']
            igroup_response = requests.get(server_details+url_igroup, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
            igroup_name = igroup_response.json()['name']
        if igroup != None and igroup != igroup_name:
            # fetching cluster_key for unique svm
            url_cluster = server_details + resource_url_path +  "clusters?name=" + cluster
            cluster_key = get_resource_key(url_cluster)
            # fetching svm_key for igroup
            url_svm = server_details + resource_url_path +  "svms?cluster_key=" + cluster_key
            svm_key = parse_for_resource_key(url_svm, svm)
            # fetching igroup_key for given igroup name
            url_igroup = server_details + resource_url_path +  "igroups?svm_key=" + svm_key
            igroup_key = parse_for_resource_key(url_igroup, igroup)
            if (igroup_key == None):
                module.exit_json(changed=False,meta="Please provide a valid igroup name.")
            lunmap_payload['igroup_key']=igroup_key
            if lun_id != None:
                lunmap_payload['lun_id']=lun_id
            lun_maps.append(lunmap_payload.copy())
            payload.clear()
            payload['lun_maps']=lun_maps
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
                module.exit_json(changed=False,meta="Either LUN has been already deleted or Please provide a valid Cluster name,SVM name,LUN name,Volume name.")
        elif module.params["state"] == PRESENT:
            if exist():
                response=self.patch()
                self.parse_patch_response(response)
            else:
                response=self.post()
                parse_state_response(response)

def exist ():
    global key
    #checking key in case of NSLM volume name is passed
    nslm_volume = "NSLM_"+volume_name
    path = "/vol/"+nslm_volume+"/"+name
    url_lun = server_details + url_path + "?filter=cluster eq "+cluster +", svm eq "+svm +", path eq "+path
    nslm_lun_key = get_resource_key(url_lun)

    #checking key in case of brownfield volume name is passed
    brownfield_path = "/vol/"+volume_name+"/"+name
    url_lun = server_details + url_path + "?filter=cluster eq "+cluster +", svm eq "+svm +", path eq "+brownfield_path
    brownfield_lun_key = get_resource_key(url_lun)

    #check both and assign key
    if nslm_lun_key != None:
        key = nslm_lun_key
    else:
        key = brownfield_lun_key

    if key == None:
        return False
    return True


def parse_state_response(response):
    """ check the response body and take necessary action according to status code """
    if response.status_code==202:
        job_key = response.json()[JOB_KEY]
        job_response = get_job_status(job_key)
        module.exit_json(changed=True, failed=False, meta=job_response)
    elif response.status_code==200:
        module.exit_json(changed=True, failed=False, meta="job successful")
    elif response.status_code==201:
        module.exit_json(changed=True,meta=response.json())
    else:
        # Returning error message received from NSLM
        module.exit_json(changed=False, failed=True, meta=response.json())

def get_job_status(job_key):
    """ verify job status and wait for job to complete """
    # to avoid infinite wait condition, in case of NSLM takes more than 300 sec to respond.
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if response.status_code==200:
            json_response=response.json()
            if json_response['state'] == JOB_STATUS:
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
        if response_json.get('num_records') == 0:
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
    if response.status_code==200:
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

def fetch_volume_key(url, resource_name):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        unique_id=None
        response_json = response.json()
        if response_json.get('num_records') == 0:
            return None
        embedded = response_json.get('_embedded')
        volume = embedded['netapp:records'][0]['volume']['key']
        return volume

def main():
    """Apply LUN operations from playbook"""
    obj = NetAppNSLMLUNs()
    obj.apply()

if __name__ == '__main__':
    main()
