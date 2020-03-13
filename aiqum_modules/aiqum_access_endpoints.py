#!/usr/bin/python



ANSIBLE_METADATA = {

    'metadata_version': '1.1',

    'status': ['preview'],

    'supported_by': 'community'

}



DOCUMENTATION = '''

---

module: aiqum_access_endpoints

author:

    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)

short_description: Active IQ Unified Manager(AIQUM) managed access_endpoints.

description:

     - Create, update or delete Access-endpoint on Active IQ Unified Manager(AIQUM).

version_added: "2.9.1"

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

    - Name of access endpoint. If ip_address and ha_ip_address both are provided then the name is assigned to the LIF on LUN's home node and LIF on partner node is created with suffix "Partner". e.g. if "Lif1" is created on home node than the LIF on partner node will be  "Lif1_Partner". If either of ip_address or ha_ip_address is provided then the name is assigned to LIF on respective node.

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

      aiqum_access_endpoints:

        hostip=<aiqum_hostip>

        port=<aiqum_portnumber>

        user=<aiqum_username>

        password=<aiqum_password>

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



class NetAppAIQUMAccessendpoints(object):

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

        datacenter_url_path         = "/api/v2/datacenter/"

        job_url_path                = "/api/v2/management-server/jobs/"

        resource_name               = "access-endpoints"

        storage_provider_url_path   = "/api/v2/storage-provider/"

        server_details              = "https://"+api_host+":"+api_port

        url_path                    = storage_provider_url_path+resource_name



        # Global Constants

        global ABSENT

        global JOB_KEY

        global JOB_STATUS

        global KEY

        global NUM_RECORDS

        global PRESENT

        global RETRY_COUNT

        global UUID



        ABSENT      = "absent"

        JOB_KEY     = "key"

        JOB_STATUS  = "completed"

        KEY         = 'key'

        NUM_RECORDS = "num_records"

        PRESENT     = "present"

        RETRY_COUNT = 300

        UUID        = 'uuid'



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

        global storage_provider_url_path

        global url_path

        data_protocols_list=[]

        lun_path=None

        payload={}

        if data_protocols != None:

            for protocols in data_protocols:

                data_protocols_list.append(protocols)

            payload['data_protocols']=data_protocols_list

        if fileshare != None:

            if cluster !=None and svm !=None:

                url_fs = server_details + storage_provider_url_path + "file-shares?name=" + fileshare + "&cluster=" + cluster + "&svm=" + svm

                fs_key = get_resource_key(url_fs)

                if fs_key == None:

                    module.exit_json(changed=False,meta="Please provide a valid File-share name.")

                fileshare_key_payload={}

                fileshare_key_payload[KEY]=fs_key

                payload['fileshare']= fileshare_key_payload

            else:

                module.exit_json(changed=False,meta="Please provide a valid Cluster name and SVM name.")

        if gateway != None:

            payload['gateway']=gateway

        ip_payload={}

        if ha_ip_address != None:

            ip_payload['ha_address']=ha_ip_address

        if netmask != None:

            ip_payload['netmask']=netmask

        if ip_address != None:

            ip_payload['address']=ip_address

            payload['ip']=ip_payload

        if lun != None:

            if volume != None:

                lun_path = "/vol/"+volume+"/"+lun

            else:

                module.exit_json(changed=False,meta="Please provide a volume name.")

            if cluster != None and svm !=None:

                url_lun = server_details + storage_provider_url_path + "luns?cluster.name=" + cluster + "&svm.name=" + svm + "&name=" + lun_path

                ln_key = get_resource_key(url_lun)

                if ln_key == None:

                    module.exit_json(changed=False,meta="Please provide a valid LUN name.")

                lun_key_payload={}

                lun_key_payload[KEY]=ln_key

                payload['lun']=lun_key_payload

            else:

                module.exit_json(changed=False,meta="Please provide a valid Cluster name and SVM name.")

        if mtu != None:

            payload['mtu']=mtu

        payload['name']=name

        if fileshare == None and lun_path == None:

            svm_payload={}

            svm_payload[KEY]=svm_key

            payload['svm']=svm_payload

        if vlan != None:

            payload['vlan']= vlan

        module.log(msg='access_endpoint value::: '+str(payload))

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

            ip_payload={}

            ip_payload['address']=ip_address

            payload['ip']=ip_payload

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

    url_svm = server_details + datacenter_url_path + "svm/svms?cluster.name="+cluster+"&name="+svm

    svm_key = get_resource_key(url_svm)

    if svm_key == None:

        module.exit_json(changed=False,meta="Please provide a valid SVM name.")

    url_aep = server_details + url_path + "?resource.key="+svm_key

    key = parse_for_resource_key(url_aep, name)

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

        if response_json.get(NUM_RECORDS) == 0 :

            return None

        records = response_json.get('records')

        for record in records:

            resource_key = record.get(KEY)

            return resource_key

    else:

        # Returning error message received from AIQUM

        module.exit_json(changed=False,meta=response.json())



def parse_for_resource_key(url, resource_name):

    response = requests.get(url, auth=(api_user_name,api_user_password), verify=False, headers=HEADERS)

    if response.status_code==200:

        unique_id=None

        response_json = response.json()

        if response_json.get(NUM_RECORDS) == 0 :

            return None

        records = response_json.get('records')

        for record in records:

            if record.get('name') == resource_name:

                if record.get(KEY) != None:

                    unique_id = record.get(KEY)

                else:

                    unique_id = record.get(UUID)

        if unique_id == None:

            return None

        else:

            return unique_id

    else:

        # Returning error message received from AIQUM

        module.exit_json(changed=False,meta=response.json())



def main():

    """Apply Access-endpoint operations from playbook"""

    obj = NetAppAIQUMAccessendpoints()

    obj.apply()



if __name__ == '__main__':

    main()

