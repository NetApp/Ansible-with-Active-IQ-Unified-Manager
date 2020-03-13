#!/usr/bin/python
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: aiqum_luns
author:
    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)
short_description: Active IQ Unified Manager(AIQUM) managed luns.
description:
     - Create, update or delete LUN on Active IQ Unified Manager(AIQUM).
version_added: "2.9.1"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present', 'absent']
    required: true
  aggregate:
    description:
    - Name of the aggregate, AIQUM chooses an aggregate if not provided.
    required: false
    state_supported: present
  capacity:
    description:
    - Capacity of the LUN, default capacity unit is in bytes. Please either verify on server or provide capacity value greater than(atleast 0.01% recommended) existing value to modify the capacity. Modifiable field.
    required: false
    state_supported: present
  capacity_unit:
    description:
    - Capacity unit is used to interpret capacity parameter, default is MB. Modifiable field.
    choices: ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb']
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
    choices: ['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'solaris_efi', 'vmware', 'windows', 'windows_2008', 'windows_gpt', 'xen',  'AIX', 'HPUX', 'HYPER_V', 'LINUX', 'NETWARE', 'OPENVMS', 'SOLARIS', 'SOLARIS_EFI', 'VMWARE', 'WINDOWS', 'WINDOWS_2008', 'WINDOWS_GPT', 'XEN']
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
    - Name of the parent volume.When not provided defaults to AIQUM_vol_<name>(where name is LUN name).If passed then AIQUM will use it as a parent volume.
    required: false
    state_supported: present, absent
'''

EXAMPLES = '''
---
    - name: Manage LUN
      aiqum_luns:
        state=present
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
        cluster=netapp-aff300-01-02
        svm=demo_vserver
        name=demo_lun_ansible
        performance_service_level=Value
        capacity=50
        capacity_unit=GB
        os_type=aix
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

class NetAppAIQUMLUNs(object):
    """Class with luns operations"""

    def __init__(self):
        """Initialize module parameters"""
        self._capacity_unit_map = dict(
            B =1,        b =1,
            KB=1024,     kb=1024,
            MB=1024 ** 2,mb=1024 ** 2,
            GB=1024 ** 3,gb=1024 ** 3,
            TB=1024 ** 4,tb=1024 ** 4,
            PB=1024 ** 5,pb=1024 ** 5,
            EB=1024 ** 6,eb=1024 ** 6,
            ZB=1024 ** 7,zb=1024 ** 7,
            YB=1024 ** 8,yb=1024 ** 8
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
            "aggregate" : {"required": False, "type": "str"},
            "capacity" : {"required": False, "type": "int"},
            "capacity_unit" : {"required": False,
                               "choices": ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'],
                               "type": 'str'
                               },
            "igroup" : {"required": False, "type": "str"},
            "lun_id" : {"required": False, "type": "str"},
            "operational_state" : {"required": False, "type": "str"},
            "os_type" : {"required": False,
                         "choices": ['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'solaris_efi', 'vmware', 'windows', 'windows_2008', 'windows_gpt', 'xen',  'AIX', 'HPUX', 'HYPER_V', 'LINUX', 'NETWARE', 'OPENVMS', 'SOLARIS', 'SOLARIS_EFI', 'VMWARE', 'WINDOWS', 'WINDOWS_2008', 'WINDOWS_GPT', 'XEN'],
                         "type": "str"},
            "performance_service_level" : {"required": False, "type": "str"},
            "storage_efficiency_policy" : {"required": False, "type": "str"},
            "volume_name": {"required": False, "type": "str"},
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

        api_host                    = module.params["hostip"]
        api_port                    = module.params["port"]
        api_user_name               = module.params["user"]
        api_user_password           = module.params["password"]
        datacenter_url_path        = "/api/v2/datacenter/"
        job_url_path                = "/api/v2/management-server/jobs/"
        resource_name               = "luns"
        storage_provider_url_path   = "/api/v2/storage-provider/"
        server_details              = "https://"+api_host+":"+api_port
        url_path                    = storage_provider_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATE
        global JOB_STATUS
        global KEY
        global NUM_RECORDS
        global PRESENT
        global RETRY_COUNT
        global UNASSIGNED

        ABSENT      = "absent"
        JOB_KEY     = "key"
        JOB_STATE   = "completed"
        JOB_STATUS  = "normal"
        KEY         = "key"
        NUM_RECORDS = "num_records"
        PRESENT     = "present"
        RETRY_COUNT = 300
        UNASSIGNED  = "Unassigned"

        # Properties details
        global aggregate
        global capacity
        global capacity_unit
        global cluster
        global fail_response
        global igroup
        global key
        global logical_unit_number
        global name
        global operational_state
        global os_type
        global performance_service_level
        global size
        global storage_efficiency_policy
        global svm
        global svm_key
        global volume_name

        aggregate                 = module.params["aggregate"]
        name                      = module.params["name"]
        capacity                  = module.params["capacity"]
        capacity_unit             = module.params["capacity_unit"]
        cluster                   = module.params["cluster"]
        igroup                    = module.params["igroup"]
        logical_unit_number       = module.params["lun_id"]
        operational_state         = module.params["operational_state"]
        os_type                   = module.params["os_type"]
        performance_service_level = module.params["performance_service_level"]
        storage_efficiency_policy = module.params["storage_efficiency_policy"]
        svm                       = module.params["svm"]
        volume_name               = module.params["volume_name"]

        # forming volume name in case user has not passed anything
        if volume_name == None:
            volume_name = "vol_"+name

        # converting capacity_unit to bytes to feed AIQUM server
        if capacity_unit != None:
            size = capacity * self._capacity_unit_map[capacity_unit]
        else:
            size = capacity

    def post(self):
        global storage_provider_url_path
        global url_path
        global svm_key
        payload={}
        lun_maps=[]
        lunmap_payload={}

        if name != None:
            payload['name']=name
        if capacity != None:
            space={}
            space['size']=size
            payload['space']=space
        if aggregate != None:
            # get aggregate key for the given aggregate name
            url_aggregate = server_details + datacenter_url_path + "storage/aggregates?name=" + aggregate + "&cluster.name=" + cluster
            aggregate_key = get_resource_key(url_aggregate)
            if (aggregate_key == None):
                module.exit_json(changed=False,meta="Please provide a valid Aggregate name.")
            aggregate_payload={}
            aggregate_payload[KEY]=aggregate_key
            payload['aggregate']=aggregate_payload
        svm_payload={}
        svm_payload[KEY]= svm_key
        payload['svm']= svm_payload
        if performance_service_level != None:
            # get performace-service-level key for the given performace-service-level name
            url_psl = server_details + storage_provider_url_path +  "performance-service-levels?name=" + performance_service_level
            performance_service_level_key = get_resource_key(url_psl)
            if (performance_service_level_key == None):
                module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            performance_service_level_payload={}
            performance_service_level_payload[KEY]=performance_service_level_key
            payload['performance_service_level']=performance_service_level_payload
        if os_type != None:
            payload['os_type']=os_type.lower()
        if storage_efficiency_policy != None:
            # get storage-efficiency-policy key for the given storage-efficiency-policy name
            url_sep = server_details + storage_provider_url_path +  "storage-efficiency-policies?name=" + storage_efficiency_policy
            storage_efficiency_policy_key = get_resource_key(url_sep)
            if storage_efficiency_policy_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            storage_efficiency_policy_payload={}
            storage_efficiency_policy_payload[KEY]=storage_efficiency_policy_key
            payload['storage_efficiency_policy']=storage_efficiency_policy_payload
        # check if volume exists then fetch and pass volume_key to AIQUM
        # else pass the volume_name_tag parameter to AIQUM
        if volume_name != None:
            url_volume = server_details +storage_provider_url_path +"file-shares?name=" +volume_name +"&svm.name="+svm +"&cluster.name="+cluster
            brownfield_volume_key = get_resource_key(url_volume)

            # fetching existing volume key first check in file-share
            # if not found then fetch from existing LUN
            aiqum_volume_name = "AIQUM_" + volume_name
            url_volume = server_details +storage_provider_url_path +"file-shares?name=" +aiqum_volume_name +"&svm.name="+svm+"&cluster.name="+cluster
            aiqum_volume_key = get_resource_key(url_volume)
            if aiqum_volume_key == None:
                url_lun = server_details + url_path + "?cluster.name="+cluster +"&svm.name="+svm +"&volume.name="+aiqum_volume_name
                aiqum_volume_key = fetch_volume_key(url_lun, aiqum_volume_name)

                #checking the case where user has created a LUN without volume name and trying to create another LUN in same volume
                # by passing the volume name as an input
                if aiqum_volume_key == None:
                    url_lun = server_details + url_path + "?cluster="+cluster +"&svm.name="+svm +"&volume.name="+volume_name
                    aiqum_volume_key = fetch_volume_key(url_lun, volume_name)

            if aiqum_volume_key != None:
                volume_key = aiqum_volume_key
            else:
                volume_key = brownfield_volume_key

            volume_payload={}
            if volume_key == None:
                volume_payload['name_tag'] = volume_name
                payload['volume'] = volume_payload
            else:
                volume_payload[KEY]= volume_key
                payload['volume']= volume_payload
        igroup_payload={}
        if igroup == None and logical_unit_number != None:
            module.exit_json(changed=False,meta="Please provide a valid igroup name.")
        if igroup != None and logical_unit_number != None:
            igroup_list = igroup.split(',')
            logical_unit_number_list = logical_unit_number.split(',')
            if len(igroup_list) != len(logical_unit_number_list):
                module.exit_json(changed=False,meta="Missing parameters in lun-maps. The number of parameters specified for igroup and lun-id should be equal.")
        elif igroup != None and logical_unit_number == None:
            igroup_list = igroup.split(',')
            #loop through all the igroups and put it to payload
            for i in range(0, len(igroup_list)):
                # get igroup key for the given igroup name
                url_igroup = server_details + datacenter_url_path + "protocols/san/igroups?name=" + igroup_list[i] + "&svm.name=" + svm
                igroup_key = get_resource_key(url_igroup)
                if (igroup_key == None):
                    module.exit_json(changed=False,meta="Please provide a valid igroup name.")
                igroup_payload[KEY]=igroup_key
                lunmap_payload['igroup']=igroup_payload
                if logical_unit_number != None:
                    lunmap_payload['logical_unit_number']=int(logical_unit_number_list[i])
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
        global igroup
        global url_path
        fail_response=None
        igroup_list=None
        igroup_payload={}
        logical_unit_number_list=None
        lun_maps=[]
        lunmap_flag=None
        lunmap_payload={}
        patch_response_key=[]
        payload={}
        url_path+="/"+key

        # fetching LUN details and updating multiple values from user input
        lun_response = requests.get(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        lun_json = lun_response.json()
        if capacity != None and capacity != lun_json['space']['size']:
            if capacity > lun_json['space']['size']:
                payload.clear()
                space={}
                space['size']=size
                payload['space']=space
                response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
                if response.status_code == 202:
                    patch_response_key.append(response.json().get('job').get(JOB_KEY))
                else:
                    fail_response = response.json()
                    self.parse_patch_response(patch_response_key)
            else:
                module.exit_json(changed=False,meta="Please remember capacity cannot be zero or less than the existing value. Existing Value: "+str(lun_json['space']['size']))

        if performance_service_level != None and performance_service_level != lun_json['assigned_performance_service_level']['name']:
            if performance_service_level == UNASSIGNED:
                performance_service_level_key = UNASSIGNED
            else:
                url_psl = server_details + storage_provider_url_path +  "performance-service-levels?name=" + performance_service_level
                performance_service_level_key = get_resource_key(url_psl)
                if (performance_service_level_key == None):
                    module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload.clear()
            performance_service_level_payload={}
            performance_service_level_payload[KEY]=performance_service_level_key
            payload['performance_service_level']=performance_service_level_payload
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get(JOB_KEY))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        if storage_efficiency_policy != None and storage_efficiency_policy != lun_json['assigned_storage_efficiency_policy']['name']:
            url_sep = server_details + storage_provider_url_path +  "storage-efficiency-policies?name=" + storage_efficiency_policy
            storage_efficiency_policy_key = get_resource_key(url_sep)
            if (storage_efficiency_policy_key == None):
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            payload.clear()
            storage_efficiency_policy_payload={}
            storage_efficiency_policy_payload[KEY]=storage_efficiency_policy_key
            payload['storage_efficiency_policy']=storage_efficiency_policy_payload
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get(JOB_KEY))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if igroup == None and logical_unit_number != None:
            module.exit_json(changed=False,meta="Please provide a igroup name.")
        # GET  and validate the list of igroups and logical_unit_number from playbook
        if igroup != None and logical_unit_number != None:
            igroup_list = igroup.split(',')
            logical_unit_number_list = logical_unit_number.split(',')
            if len(igroup_list) != len(logical_unit_number_list):
                module.exit_json(changed=False,meta="Missing parameters in lun-maps. The number of parameters specified for igroup and lun-id should be equal.")
        elif igroup != None and logical_unit_number == None:
            igroup_list = igroup.split(',')
        # fetching igroup name from AIQUM by GET on igroup key
        if 'lun_maps' in lun_json:
            # GET the list of assigned igroups from GET by key on LUN
            for i in range(0, len(lun_json['lun_maps'])):
                igroup_name_list = lun_json['lun_maps'][i]['igroup']['name']
                lun_id_list = lun_json['lun_maps'][i]['logical_unit_number']

            # compare playbook igroup_list with already attached igroup list to find out any difference
            # if any difference is found then we will do the patch with the list given in playbook
            if len(igroup_list) == len(igroup_name_list):
                for i in range(0, len(igroup_list)):
                    if igroup_list[i] not in igroup_name_list:
                        lunmap_flag = True
            elif len(igroup_list) != len(igroup_name_list):
                lunmap_flag = True

        else:
            lunmap_flag = True

        # add igroup given in the playbook to the payload for patch operation
        if lunmap_flag:
            for i in range(0, len(igroup_list)):
                # fetching igroup_key for given igroup name
                igroup={}
                url_igroup = server_details + datacenter_url_path + "protocols/san/igroups?name=" + igroup_list[i] + "&svm.name=" + svm
                igroup_key = get_resource_key(url_igroup)
                if (igroup_key == None):
                    module.exit_json(changed=False,meta="Please provide a valid igroup name.")
                igroup[KEY]=igroup_key
                lunmap_payload['igroup']=igroup
                if logical_unit_number != None:
                    lunmap_payload['logical_unit_number']=logical_unit_number_list[i]
                lun_maps.append(lunmap_payload.copy())
            payload.clear()
            payload['lun_maps']=lun_maps
        response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)

        if response.status_code == 202:
            patch_response_key.append(response.json().get('job').get(JOB_KEY))
        else:
            fail_response = response.json()
            self.parse_patch_response(patch_response_key)

        if operational_state != None:
            payload.clear()
            payload['operational_state']=operational_state
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get(JOB_KEY))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        return patch_response_key

    def parse_patch_response(self, response):
        """ check the patch response body for all the jobs and take necessary action according to status code """
        status=[]
        for job_key in response:
            job_response = get_job_status(job_key)
            if job_response['state'] == JOB_STATE and job_response['status'] == JOB_STATUS:
                status.append(" name: "+job_response['name'] +" status: "+ job_response['status'] +" state: " +job_response['state'] + " job key: "+job_response[JOB_KEY])
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
    global svm_key
    # validate the given cluster name
    if cluster != None:
        url_cluster = server_details + datacenter_url_path + "cluster/clusters?name=" + cluster
        cluster_key = get_resource_key(url_cluster)
        if cluster_key == None:
            module.exit_json(changed=False,meta="Please provide a valid Cluster name.")
    # validate the given svm name
    if svm != None:
        url_svm = server_details + datacenter_url_path + "svm/svms?cluster.name=" + cluster + "&name=" + svm
        svm_key = get_resource_key(url_svm)
        if (svm_key == None):
            module.exit_json(changed=False,meta="Please provide a valid SVM name.")

    #checking key in case of AIQUM volume name is passed
    aiqum_volume = "AIQUM_"+volume_name
    path = "/vol/"+aiqum_volume+"/"+name
    url_lun = server_details + url_path + "?cluster.name="+cluster +"&svm.name="+svm +"&name="+path
    aiqum_lun_key = get_resource_key(url_lun)


    #check both and assign key
    if aiqum_lun_key != None:
        key = aiqum_lun_key
    else:
    #checking key in case of brownfield volume name is passed
        brownfield_path = "/vol/"+volume_name+"/"+name
        url_lun = server_details + url_path + "?cluster.name="+cluster +"&svm.name="+svm +"&name="+brownfield_path
        brownfield_lun_key = get_resource_key(url_lun)
        key = brownfield_lun_key

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

def fetch_volume_key(url, resource_name):
    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
    if response.status_code==200:
        unique_id=None
        response_json = response.json()
        if response_json.get(NUM_RECORDS) == 0:
            return None
        records = response_json.get('records')
        volume = records[0]['volume'][KEY]
        return volume

def main():
    """Apply LUN operations from playbook"""
    obj = NetAppAIQUMLUNs()
    obj.apply()

if __name__ == '__main__':
    main()
