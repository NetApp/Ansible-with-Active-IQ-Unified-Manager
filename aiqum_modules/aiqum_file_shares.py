ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: aiqum_file_shares
author:
    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)
short_description: Active IQ Unified Manager(AIQUM) managed file-shares.
description:
    - Create, update or delete file-share on Active IQ Unified Manager(AIQUM).
version_added: "2.9.1"
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
      - List of CIFS share access controls. In order to provide multiple access controls, permission and user_or_group should be multi valued(as many as access controls) separated by comma. Please refer the example given below. Modifiable field.
      required: false
      state_supported: present
      permission:
        description:
        - Permissions to be allowed for the user or group. Modifiable field.
        choices: ['NO_ACCESS', 'READ', 'CHANGE', 'FULL_CONTROL', 'no_access', 'read', 'change', 'full_control']
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
      export_policy_name:
        description:
        - Name of the existing export-policy which will be used to create the Fileshare. If this field is provided, then no other input for export-policy is expected.
        required: false
        state_supported: present
      export_policy_name_tag:
        description:
        - Name Tag of the export policy which is used in POST and PATCH of export policy.
        required: false
        state_supported: present
      rules:
        description:
        - List of export rules. In order to specify multiple export rules, parameters- cifs, nfsv3, nfsv4 can either be single valued as the same value will be repeated for all the rules or multi valued (count equal to the number of rules), seperated by comma. Parameter- index should be multi valued(as many as rules) separated by comma. Parameters: allowed_clients, read_only_rule and read_write_rule should be multi valued with two separaters, semicolon to separate two lists/strings and comma to separate elements in list/string. Please refer the example given below. Modifiable field.
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
          choices: [SYS, NTLM, KERBEROS5, KERBEROS5I, KERBEROS5P, NONE, NEVER, ANY, any, none, never, kerberos5, kerberos5i, kerberos5p, ntlm, sys]
          required: false
          state_supported: present
        read_write_rule:
          description:
          - Read-write rule specified as comma-separated values. Modifiable field.
          choices: [SYS, NTLM, KERBEROS5, KERBEROS5I, KERBEROS5P, NONE, NEVER, ANY, any, none, never, kerberos5, kerberos5i, kerberos5p, ntlm, sys]
          required: false
          state_supported: present
  aggregate:
    description:
    - Name of the aggregate to be used.
    required: false
    state_supported: present
  capacity:
    description:
    - Capacity of the file-share in Bytes. Modifiable field.
    required: false
    state_supported: present
  capacity_unit:
    description:
    - Capacity unit used to interpret the capacity parameter, default is Bytes. Modifiable field.
    choices: ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb']
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
    choices:  ['ONLINE', 'OFFLINE', 'online', 'offline']
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
      aiqum_file_shares:
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
        state=present
        name=demo_fileshare_ansible
        capacity=5
        capacity_unit=GB
        performance_service_level=Value
        svm=demo_vserver
        cluster=netapp-aff300-01-02
        mountpoint: /demo_fileshare_ansible
        cifs=false,true,false
        nfsv3=true,false,true
        nfsv4=true,false,false
        index=5,6,7
        allowed_clients=10.12.13.14,10.11.22.65;10.11.22.33;10.32.43.54,10.21.31.41
        read_only_rule=SYS,NEVER;NTLM,ANY;KERBEROS5P
        read_write_rule=SYS,NONE;ANY;KERBEROS5P
      register : jsonResult

    - name: Manage file-share
      aiqum_file_shares:
        hostip=<aiqum_hostip>
        port=<aiqum_portnumber>
        user=<aiqum_username>
        password=<aiqum_password>
        state=present
        name=demo_fileshare_ansible
        capacity=5000000
        performance_service_level=Value
        svm=demo_vserver
        cluster=netapp-aff300-01-02
        mountpoint: /demo_fileshare_ansible
        user_or_group=CTLAdmin,EVERYONE
        permission=READ,NO_ACCESS
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
warnings.filterwarnings('ignore')

HEADERS = {
    'content-type': 'application/json'
}

class NetAppAIQUMFileshares(object):
    """Class with file-share operations"""

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
                               "choices": ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'],
                               "type": 'str'
                               },
            'cifs': {'required': False, 'type': 'list'},
            'cluster': {'required': True, 'type': 'str'},
            'export_policy_name': {'required': False, 'type':'str'},
            'export_policy_name_tag': {'required': False, 'type':'str'},
            'index': {'required': False, 'type': 'list'},
            'mountpoint': {'required': False, 'type': 'str'},
            'name': {'required': True, 'type': 'str'},
            'nfsv3': {'required': False, 'type': 'list'},
            'nfsv4': {'required': False, 'type': 'list'},
            'operational_state': {'required': False,
                                  "choices": ['ONLINE', 'OFFLINE', 'online', 'offline'],
                                  'type': 'str'
                                 },
            'performance_service_level': {'required': False, 'type': 'str'},
            'permission': {'required': False,
                           'choices': ['NO_ACCESS', 'READ', 'CHANGE', 'FULL_CONTROL', 'no_access', 'read', 'change', 'full_control'],
                           'type': 'list'},
            'read_only_rule': {'required': False,
                               'type': 'str'
                              },
            'read_write_rule': {'required': False,
                                'type': 'str'
                              },
            'storage_efficiency_policy': {'required': False, 'type': 'str'},
            'attach_active_directory': {'required': False, 'type': 'bool'},
            'svm': {'required': True, 'type': 'str'},
            'user_or_group': {'required': False, 'type': 'list'},
        }

        global module
        module = AnsibleModule(argument_spec=fields)

        # Active IQ Unified Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global job_url_path
        global resource_name
        global storage_provider_url_path
        global datacenter_url_path
        global server_details
        global url_path

        api_host                           = module.params["hostip"]
        api_port                           = module.params['port']
        api_user_name                      = module.params['user']
        api_user_password                  = module.params['password']
        job_url_path                       = "/api/v2/management-server/jobs/"
        resource_name                      = "file-shares"
        storage_provider_url_path          = "/api/v2/storage-provider/"
        datacenter_url_path                = "/api/v2/datacenter/"
        server_details                     = "https://"+api_host+":"+api_port
        url_path                           = storage_provider_url_path + resource_name

        # Global Constants
        global ABSENT
        global JOB_KEY
        global JOB_STATE
        global JOB_STATUS
        global PRESENT
        global RETRY_COUNT
        global UNASSIGNED
        global CIFS
        global NFS3
        global NFS4

        ABSENT      = "absent"
        JOB_KEY     = "job_key"
        JOB_STATE   = "completed"
        JOB_STATUS  = "normal"
        PRESENT     = "present"
        RETRY_COUNT = 300
        UNASSIGNED  = "Unassigned"
        CIFS        = "cifs"
        NFS3        = "nfs3"
        NFS4        = "nfs4"

        # Properties details
        global aggregate_name
        global allowed_clients
        global capacity
        global size
        global capacity_unit
        global capacity_in_mb
        global cluster_name
        global cifs
        global export_policy_name
        global export_policy_name_tag
        global fail_response
        global index
        global key
        global name
        global nfsv3
        global nfsv4
        global mountpoint
        global operational_state
        global performance_service_level_name
        global permission
        global read_only_rule
        global read_write_rule
        global storage_efficiency_policy_name
        global svm_name
        global attach_active_directory
        global user_or_group
        global json_response

        aggregate_name                 = module.params['aggregate']
        allowed_clients                = module.params['allowed_clients']
        capacity                       = module.params["capacity"]
        capacity_unit                  = module.params["capacity_unit"]
        cifs                           = module.params['cifs']
        cluster_name                   = module.params['cluster']
        export_policy_name             = module.params['export_policy_name']
        export_policy_name_tag         = module.params['export_policy_name_tag']
        index                          = module.params['index']
        mountpoint                     = module.params['mountpoint']
        name                           = module.params['name']
        nfsv3                          = module.params['nfsv3']
        nfsv4                          = module.params['nfsv4']
        operational_state              = module.params['operational_state']
        performance_service_level_name = module.params['performance_service_level']
        permission                     = module.params['permission']
        read_only_rule                 = module.params['read_only_rule']
        read_write_rule                = module.params['read_write_rule']
        storage_efficiency_policy_name = module.params['storage_efficiency_policy']
        svm_name                       = module.params['svm']
        attach_active_directory        = module.params['attach_active_directory']
        user_or_group                  = module.params['user_or_group']

        # converting capacity_unit to mb to feed AIQUM server
        if capacity_unit != None:
            capacity_in_mb = capacity * self._capacity_unit_map[capacity_unit]
        else:
            capacity_in_mb = capacity

    def post(self):
        global url_path
        global resource_url_path
        global CIFS
        global NFS3
        global NFS4

        access_control={}
        acl=[]
        acl_payload={}
        export_policy={}
        rules=[]
        clients=[]
        read_only_rule_list=[]
        read_write_rule_list=[]
        payload={}
        space={}
        svm={}
        active_directory_mapping={}
        performance_service_level={}
        aggregate={}
        storage_efficiency_policy={}

        if capacity != None:
            space['size']=capacity_in_mb;
            payload['space']=space
        if mountpoint != None:
            payload['mountpoint']=mountpoint
        if name != None:
            payload['name']=name
        if svm_name != None:
            url_svm = server_details + datacenter_url_path +  "svm/svms?cluster.name=" + cluster_name + "&name=" + svm_name
            svm_key = get_resource_key(url_svm)
            if svm_key ==None:
                module.exit_json(changed=False,meta="Please provide a valid SVM name.")
            svm['key']= svm_key
            payload['svm']= svm
        if attach_active_directory != None and attach_active_directory == True:
            url_active_directory = server_details + storage_provider_url_path +  "active-directories-mappings?svm.name=" + svm_name
            active_directory_key = get_resource_key(url_active_directory)
            if active_directory_key == None:
                module.exit_json(changed=False,meta="Please provide a SVM having active directory configured.")
            active_directory_mapping['key'] = active_directory_key
            access_control['active_directory_mapping']= active_directory_mapping
        if aggregate_name != None:
            url_aggregate = server_details + datacenter_url_path +  "storage/aggregates?cluster.name=" + cluster_name + "&name=" + aggregate_name
            aggregate_key = get_resource_key(url_aggregate)
            if aggregate_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Aggregate name.")
            aggregate['key'] = aggregate_key
            payload['aggregate']=aggregate
        if performance_service_level_name != None:
            url_psl = server_details + storage_provider_url_path +  "performance-service-levels?name=" + performance_service_level_name
            performance_service_level_key = get_resource_key(url_psl)
            if performance_service_level_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            performance_service_level['key']=performance_service_level_key
            payload['performance_service_level']=performance_service_level
        if storage_efficiency_policy_name != None:
            url_sep = server_details + storage_provider_url_path +  "storage-efficiency-policies?name=" + storage_efficiency_policy_name
            storage_efficiency_policy_key = get_resource_key(url_sep)
            if storage_efficiency_policy_key == None:
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            storage_efficiency_policy['key']=storage_efficiency_policy_key
            payload['storage_efficiency_policy']=storage_efficiency_policy
        if permission != None and user_or_group != None:
            if len(permission) == len(user_or_group):
                for i in range(0,len(permission)):
                    acl.append({"permission":permission[i].lower(), "user_or_group":user_or_group[i]})
                access_control['acl']= acl
            else:
                module.exit_json(changed=False,meta="Every user_or_group should have a corresponding permission specified and vice versa.")
        elif permission != None or user_or_group != None:
               module.exit_json(changed=False,meta="Both user_or_group and permission should be specified.")
        if export_policy_name != None and cifs == None and index == None and nfsv3 == None and nfsv4 == None and read_only_rule == None and read_write_rule == None and allowed_clients == None:
            url_export_policy = server_details + datacenter_url_path +  "protocols/nfs/export-policies?name=" + export_policy_name + "&svm.name=" + svm_name + "&cluster.name=" + cluster_name
            export_policy_key = get_resource_key(url_export_policy)
            if export_policy_key == None:
                module.exit_json(changed=False,meta="Please provide a valid export policy name.")
            export_policy['key']=export_policy_key
            access_control['export_policy']=export_policy
        elif export_policy_name != None and (cifs != None or index != None or nfsv3 != None or nfsv4 != None or read_only_rule != None or read_write_rule != None or allowed_clients != None):
            module.exit_json(changed=False,meta="No parameter is allowed with the export policy key.")
        if read_only_rule != None and read_write_rule != None and allowed_clients != None:
            export_policy = export_policy_check()
            access_control['export_policy']=export_policy
        elif cifs != None or index != None or nfsv3 != None or nfsv4 != None or read_only_rule or read_write_rule or allowed_clients:
            module.exit_json(changed=False,meta="Parameters: index, read_only_rule, read_write_rule, allowed_clients, must be provided for an Export Policy.")
        if access_control :
            payload['access_control']=access_control
        response = requests.post(server_details + url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
        module.log(msg='PAYLOAD:'+str(payload))
        return response

    def delete(self):
        global url_path
        url_path+='/' + key
        response = requests.delete(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        return response

    def patch(self):
        global url_path
        global resource_url_path
        global CIFS
        global NFS3
        global NFS4
        global fail_response

        access_control={}
        acl=[]
        acl_payload={}
        export_policy={}
        rules=[]
        clients=[]
        read_only_rule_list=[]
        read_write_rule_list=[]
        payload={}
        space={}
        svm={}
        active_directory_mapping={}
        performance_service_level={}
        aggregate={}
        storage_efficiency_policy={}
        fail_response=None
        patch_response_key=[]
        rules_payload={}
        payload={}

        url_path+="/"+key
        # fetching file-share details and updating multiple values from user input
        file_share_response = requests.get(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)
        file_share_json = file_share_response.json()
        if capacity != None and capacity_in_mb != file_share_json['space']['size']:
            payload.clear()
            space['size']=capacity_in_mb;
            payload['space']=space
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if performance_service_level_name != None and performance_service_level_name != file_share_json['assigned_performance_service_level']['name']:
            if performance_service_level_name == UNASSIGNED:
                performance_service_level_key = UNASSIGNED
            else:
                url_psl = server_details + storage_provider_url_path +  "performance-service-levels?name=" + performance_service_level_name
                performance_service_level_key = get_resource_key(url_psl)
                if (performance_service_level_key == None):
                    module.exit_json(changed=False,meta="Please provide a valid Performance service level name.")
            payload.clear()
            performance_service_level['key']=performance_service_level_key
            payload['performance_service_level']=performance_service_level
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if storage_efficiency_policy_name != None and storage_efficiency_policy_name != file_share_json['assigned_storage_efficiency_policy']['name']:
            url_sep = server_details + storage_provider_url_path +  "storage-efficiency-policies?name=" + storage_efficiency_policy_name
            storage_efficiency_policy_key = get_resource_key(url_sep)
            if (storage_efficiency_policy_key == None):
                module.exit_json(changed=False,meta="Please provide a valid Storage efficiency policy name.")
            payload.clear()
            storage_efficiency_policy['key']=storage_efficiency_policy_key
            payload['storage_efficiency_policy']=storage_efficiency_policy
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        if permission != None and user_or_group != None:
            if len(permission) == len(user_or_group):
                for i in range(0,len(permission)):
                    acl.append({"permission":permission[i].lower(), "user_or_group":user_or_group[i]})
                access_control['acl']= acl
            else:
                module.exit_json(changed=False,meta="Every user_or_group should have a corresponding permission specified and vice versa.")
            payload.clear()
            payload['access_control']=access_control
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        elif permission != None or user_or_group != None:
               module.exit_json(changed=False,meta="Both user_or_group and permission should be specified.")
        if export_policy_name != None and cifs == None and index == None and nfsv3 == None and nfsv4 == None and read_only_rule == None and read_write_rule == None and allowed_clients == None:
            url_export_policy = server_details + datacenter_url_path +  "protocols/nfs/export-policies?name=" + export_policy_name + "&svm.name=" + svm_name + "&cluster.name=" + cluster_name
            export_policy_key = get_resource_key(url_export_policy)
            if export_policy_key == None:
                module.exit_json(changed=False,meta="Please provide a valid export policy name.")
            export_policy['key']=export_policy_key
            access_control.clear()
            access_control['export_policy']=export_policy
            payload.clear()
            payload['access_control']=access_control
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)

        elif export_policy_name != None and (cifs != None or index != None or nfsv3 != None or nfsv4 != None or read_only_rule != None or read_write_rule != None or allowed_clients != None):
            module.exit_json(changed=False,meta="No parameter is allowed with the export policy key.")
        if read_only_rule != None and read_write_rule != None and allowed_clients != None:
            export_policy = export_policy_check()
            access_control.clear()
            access_control['export_policy']=export_policy
            payload.clear()
            payload['access_control']=access_control
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
            else:
                fail_response = response.json()
                self.parse_patch_response(patch_response_key)
        elif cifs != None or index != None or nfsv3 != None or nfsv4 != None or read_only_rule or read_write_rule or allowed_clients:
               module.exit_json(changed=False,meta="Parameters: index, read_only_rule, read_write_rule, allowed_clients, must be provided for an Export Policy.")
        if operational_state != None:
            payload.clear()
            payload['operational_state']=operational_state.lower()
            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
            if response.status_code == 202:
                patch_response_key.append(response.json().get('job').get('key'))
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

def export_policy_check ():
    global CIFS
    global NFS3
    global NFS4

    export_policy={}
    rules_payload={}

    rules=[]
    read_only_rule_list = read_only_rule.split(';')
    read_only_rule_lists = [i.split(",") for i in read_only_rule_list]
    read_write_rule_list = read_write_rule.split(';')
    read_write_rule_lists = [i.strip(";").split(",") for i in read_write_rule_list]
    allowed_clients_list = allowed_clients.split(';')
    rules_count = len(allowed_clients_list)
    if len(read_only_rule_lists) == len(read_write_rule_lists) == len(allowed_clients_list):
        for i in range(0,rules_count):
            clients_payload={}
            clients=[]
            protocols=[]
            clients_payload['match']=allowed_clients_list[i]
            clients.append(clients_payload)
            rules_payload={}
            ro_rule=read_only_rule_lists[i]
            ro_rule = [rule.lower() for rule in ro_rule]
            rw_rule=read_write_rule_lists[i]
            rw_rule = [rule.lower() for rule in rw_rule]
            rules_payload["ro_rule"]=ro_rule
            rules_payload["rw_rule"]=rw_rule
            rules_payload["clients"]=clients
            if index != None and len(index)== rules_count:
                rules_payload["index"]=index[i]
            if cifs != None:
                if len(cifs) == rules_count:
                    if cifs[i] == 'true':
                        protocols.append(CIFS)
                elif len(cifs) == 1:
                    if cifs[0] == 'true':
                        protocols.append(CIFS)
                else:
                    module.exit_json(changed=False,meta="Input length for cifs protocols should be either 1 or be equal to the number of rules.")
            if nfsv3 != None:
                if len(nfsv3) == rules_count:
                    if nfsv3[i] == 'true':
                        protocols.append(NFS3)
                elif len(nfsv3) == 1:
                    if nfsv3[0] == 'true':
                        protocols.append(NFS3)
                else:
                    module.exit_json(changed=False,meta="Input length for nfsv3 protocols should be either 1 or be equal to the number of rules.")
            if nfsv4 != None:
                if len(nfsv4) == rules_count:
                    if nfsv4[i] == 'true':
                        protocols.append(NFS4)
                elif len(nfsv4) == 1:
                    if nfsv4[0] == 'true':
                        protocols.append(NFS4)
                else:
                    module.exit_json(changed=False,meta="Input length for nfsv4 protocols should be either 1 or be equal to the number of rules.")
            if cifs==None and nfsv3==None and nfsv4==None:
                module.exit_json(changed=False,meta="Export rule parameters cannot be null")
            rules_payload["protocols"]=protocols
            rules.append(rules_payload)
        export_policy['rules']= rules
        if export_policy_name_tag != None:
            export_policy['name-tag']=export_policy_name_tag
    else:
        module.exit_json(changed=False,meta="Missing parameters in export policy rule. The number of parameters specified for read_only_rule, read_write_rule, allowed_clients should be equal.")
    return export_policy

def exist ():
    global key
    if (cluster_name != None and svm_name != None and name != None):
        url_fs = server_details + url_path + "?cluster.name="+cluster_name +"&svm.name="+svm_name +"&name="+name
        key = get_resource_key(url_fs)
        if (key == None):
            return False
        return True
    else:
        return False

def parse_state_response(response):
    """ check the response body and take necessary action according to status code """
    if(response.status_code==202):
        response_json = response.json()
        job = response_json.get('job')
        job_key = job.get('key')
        job_response = get_job_status(job_key)
        module.exit_json(changed=True,meta=job_response)
    elif(response.status_code==200):
        module.exit_json(changed=True,meta="job successful")
    elif(response.status_code==201):
        module.exit_json(changed=True,meta=response.json())
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def get_job_status(job_key):
    """ verify job status and wait for job to complete """
    # to avoid infinite wait condition, in case of AIQUM takes more than 300 sec to respond.
    global job_url_path
    global RETRY_COUNT
    url = server_details+job_url_path+job_key
    while RETRY_COUNT > 0:
        response = requests.get(url, auth=(api_user_name,api_user_password), headers=HEADERS, verify=False)
        if (response.status_code==200):
            json_response=response.json()
            if (json_response['state'] == JOB_STATE) :
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
        if response_json.get('num_records') == 0 :
            return None
        records = response_json.get('records')
        for record in records:
            resource_key = record.get('key')
            return resource_key
    else:
        # Returning error message received from AIQUM
        module.exit_json(changed=False,meta=response.json())

def main():
    """Apply File-share operations from playbook"""
    obj = NetAppAIQUMFileshares()
    obj.apply()


if __name__ == '__main__':
    main()
