#!/usr/bin/python



ANSIBLE_METADATA = {

    'metadata_version': '1.1',

    'status': ['preview'],

    'supported_by': 'community'

}



DOCUMENTATION = '''

---

module: aiqum_svms

author:

    - Active IQ Unified Manager Solutions Team (ng-aiqum-solutions@netapp.com)

short_description: Active IQ Unified Manager(AIQUM) managed svms.

description:

     - Create, update or delete SVMs on Active IQ Unified Manager(AIQUM).

version_added: "2.9.1"

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

  cifs_ad_domain_fqdn:

    description:

    - The fully qualified domain name (FQDN) of the Windows Active Directory for this CIFS server.

    required: false

    state_supported: present

  cifs_ad_domain_user:

    description:

    - The user account used to add this CIFS server to the Active Directory.

    required: false

    state_supported: present

  cifs_ad_domain_password:

    description:

    - The account password used to add this CIFS server to the Active Directory. This is not audited.

    required: false

    state_supported: present

  cifs_enabled:

    description:

    - Specifies whether the CIFS server is enabled for administration.

    required: false

    state_supported: present

  cifs_name:

    description:

    - The NetBIOS name of the CIFS server.

    required: false

    state_supported: present

  cluster:

    description:

    - Cluster to which the SVM belongs.

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

  dns_domains:

    description:

    - A list of DNS domains.

    required: false

    state_supported: present

  dns_servers:

    description:

    - The list of IP addresses of the DNS servers. Addresses can be either IPv4 or IPv6 addresses.

    required: false

    state_supported: present

  fcp_enabled:

    description:

    - Setting this value to true creates a service if not already created.

    required: false

    state_supported: present

  ip_interface_enabled:

    description:

    - The administrative state of the interface.

    required: false

    state_supported: present

  ip_interface_address:

    description:

    - IP address.

    required: false

    state_supported: present

  ip_interface_netmask:

    description:

    - Input as netmask length (16) or IPv4 mask (255.255.0.0).

    required: false

    state_supported: present

  ip_interface_home_node_name:

    description:

    - Home node of IP Interface.

    required: false

    state_supported: present

  ip_interface_name:

    description:

    - Interface name.

    required: false

    state_supported: present

  iscsi_enabled:

    description:

    - Setting to true creates a service if not already created.

    required: false

    state_supported: present

  ldap_name:

    description:

    - This parameter specifies name of LDAP.

    required: false

    state_supported: present

  ldap_ad_domain:

    description:

    - This parameter specifies name of Active Directory domain used to discover LDAP servers to use by this cient.

    required: false

    state_supported: present

  ldap_base_dn:

    description:

    - Specifies the default base DN for all searches.

    required: false

    state_supported: present

  ldap_bind_dn:

    description:

    - Specifies the user that binds to the LDAP servers. SVM API supports anonymous binding. For Simple and SASL LDAP binding, use the LDAP API endpoint.

    required: false

    state_supported: present

  ldap_enabled:

    description:

    - Setting this value to true creates a configuration if not already created.

    required: false

    state_supported: present

  ldap_servers:

    description:

    - List of LDAP Servers used for this client configuration. This parameter takes both FQDNs and IP addresses.

    required: false

    state_supported: present

  nfs_enabled:

    description:

    - Setting this value to true creates a service if not already created.

    required: false

    state_supported: present

  nis_domain:

    description:

    - The NIS domain to which this configuration belongs.

    required: false

    state_supported: present

  nis_enabled:

    description:

    - Setting this value to true creates a configuration if not already created.

    required: false

    state_supported: present

  nis_servers:

    description:

    - A list of hostnames or IP addresses of NIS servers used by the NIS domain configuration.

    required: false

    state_supported: present

  nvme_enabled:

    description:

    - Setting this value to true creates a service if not already created.

    required: false

    state_supported: present

  routes_destination_address:

    description:

    - ip_address

    required: false

    state_supported: present

  routes_destination_family:

    description:

    - ip_address_family.

    required: false

    state_supported: present

  routes_destination_netmask:

    description:

    - ip_netmask.

    required: false

    state_supported: present

  routes_gateway:

    description:

    - The IP address of the gateway router leading to the destination.

    required: false

    state_supported: present

  snapshot_policy:

    description:

    - Name of the SnapShot policy.

    required: false

    state_supported: present

  subtype:

    description:

    - SVM subtype. The SVM subtype sync_destination is created automatically when an SVM of subtype sync_source is created on the source MetroCluster cluster.

    required: false

    choices: ['default', 'dp_destination', 'sync_source', 'sync_destination']

  operational_state:

    description:

    - SVM State

    required: false

    choices: ['running', 'stopped']

  language:

    description:

    - Default volume language code. UTF-8 encoded languages are valid in POST or PATCH. Non UTF-8 language encodings are for backward compatibility and are not valid input for POST and PATCH requests.

    required: false

    choices: ['c', 'da', 'de', 'en', 'en_us', 'es', 'fi', 'fr', 'he', 'it', 'ja', 'ja_jp.pck', 'ko', 'no', 'nl', 'pt', 'sv', 'zh', 'zh.gbk', 'zh_tw', 'zh_tw.big5', 'c.utf_8', 'ar', 'ar.utf_8', 'cs', 'cs.utf_8', 'da.utf_8', 'de.utf_8', 'en.utf_8', 'en_us.utf_8', 'es.utf_8', 'fi.utf_8', 'fr.utf_8', 'he.utf_8', 'hr', 'hr.utf_8', 'hu', 'hu.utf_8', 'it.utf_8', 'ja.utf_8', 'ja_v1', 'ja_v1.utf_8', 'ja_jp.pck.utf_8', 'ja_jp.932', 'ja_jp.932.utf_8', 'ja_jp.pck_v2', 'ja_jp.pck_v2.utf_8', 'ko.utf_8', 'no.utf_8', 'nl.utf_8, pl', 'pl.utf_8', 'pt.utf_8', 'ro', 'ro.utf_8', 'ru', 'ru.utf_8', 'sk', 'sk.utf_8', 'sl', 'sl.utf_8', 'sv.utf_8', 'tr', 'tr.utf_8', 'zh.utf_8', 'zh.gbk.utf_8', 'zh_tw.utf_8', 'zh_tw.big5.utf_8', 'utf8mb4']

    state_supported: present

'''



EXAMPLES = '''

---

    - name: Manage SVM

      aiqum_svms:

        hostip=<aiqum_hostip>

        port=<aiqum_portnumber>

        user=<aiqum_username>

        password=<aiqum_password>

        state=present

        cluster=netapp-aff300-01-02

        name=demo_vserver

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



class NetAppAIQUMSVMs(object):

    """Class with svms operations"""



    def __init__(self):

        """Initialize module parameters"""



        fields = {'state': {'required': True,

                            'choices': ['present', 'absent'],

                            'type': 'str'

                           },

                  'hostip': {'required': True, 'type': 'str'},

                  'port': {'required': True, 'type': 'str'},

                  'user': {'required': True, 'type': 'str'},

                  'password': {'required': True, 'type': 'str'},

                  'aggregate': {'required': False, 'type': 'list'},

                  'cifs_name': {'required': False, 'type': 'str'},

                  'cifs_ad_domain_fqdn': {'required': False, 'type': 'str'},

                  'cifs_ad_domain_user': {'required': False, 'type': 'str'},

                  'cifs_ad_domain_password': {'required': False, 'type': 'str'},

                  'cifs_enabled': {'required': False, 'type': 'str'},

                  'cluster': {'required': True, 'type': 'str'},

                  'ip_space_name': {'required': False, 'type': 'str'},

                  'name': {'required': True, 'type': 'str'},

                  'dns_domains': {'required': False, 'type': 'list'},

                  'dns_servers': {'required': False, 'type': 'list'},

                  'fcp_enabled': {'required': False, 'type': 'str'},

                  'iscsi_enabled': {'required': False, 'type': 'str'},

                  'nfs_enabled': {'required': False, 'type': 'str'},

                  'ip_interface_enabled': {'required': False, 'type': 'list'},

                  'ip_interface_address': {'required': False, 'type': 'list'},

                  'ip_interface_netmask': {'required': False, 'type': 'list'},

                  'ip_interface_home_node_name': {'required': False, 'type': 'list'},

                  'ip_interface_name': {'required': False, 'type': 'list'},

                  'ldap_name': {'required': False, 'type': 'str'},

                  'ldap_ad_domain': {'required': False, 'type': 'str'},

                  'ldap_base_dn': {'required': False, 'type': 'str'},

                  'ldap_bind_dn': {'required': False, 'type': 'str'},

                  'ldap_enabled': {'required': False, 'type': 'str'},

                  'ldap_servers': {'required': False, 'type': 'list'},

                  'nis_domain': {'required': False, 'type': 'str'},

                  'nis_enabled': {'required': False, 'type': 'str'},

                  'nis_servers': {'required': False, 'type': 'list'},

                  'nvme_enabled': {'required': False, 'type': 'str'},

                  'operational_state': {'required': False, 'choices': [

                                        'running', 'stopped'],

                                        'type': 'str'

                                       },

                  'routes_destination_address': {'required': False, 'type': 'list'},

                  'routes_destination_family': {'required': False, 'type': 'list'},

                  'routes_destination_netmask': {'required': False, 'type': 'list'},

                  'routes_gateway': {'required': False, 'type': 'list'},

                  'snapshot_policy': {'required': False, 'type': 'str'},

                  'subtype': {'required': False, 'choices': [

                              'default', 'dp_destination', 'sync_source', 'sync_destination'],

                              'type': 'str'

                             },

                  'language': {'required': False, 

                               'choices': ['c', 'da', 'de', 'en', 'en_us', 'es', 'fi', 'fr', 'he', 'it', 'ja', 'ja_jp.pck', 'ko', 'no', 'nl', 'pt', 'sv', 'zh', 'zh.gbk', 'zh_tw', 'zh_tw.big5', 'c.utf_8', 'ar', 'ar.utf_8', 'cs', 'cs.utf_8', 'da.utf_8', 'de.utf_8', 'en.utf_8', 'en_us.utf_8', 'es.utf_8', 'fi.utf_8', 'fr.utf_8', 'he.utf_8', 'hr', 'hr.utf_8', 'hu', 'hu.utf_8', 'it.utf_8', 'ja.utf_8', 'ja_v1', 'ja_v1.utf_8', 'ja_jp.pck.utf_8', 'ja_jp.932', 'ja_jp.932.utf_8', 'ja_jp.pck_v2', 'ja_jp.pck_v2.utf_8', 'ko.utf_8', 'no.utf_8', 'nl.utf_8, pl', 'pl.utf_8', 'pt.utf_8', 'ro', 'ro.utf_8', 'ru', 'ru.utf_8', 'sk', 'sk.utf_8', 'sl', 'sl.utf_8', 'sv.utf_8', 'tr', 'tr.utf_8', 'zh.utf_8', 'zh.gbk.utf_8', 'zh_tw.utf_8', 'zh_tw.big5.utf_8', 'utf8mb4'],

                               'type': 'str'

                              }

                 }



        global module

        module = AnsibleModule(argument_spec=fields)



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



        api_host = module.params['hostip']

        api_port = module.params['port']

        api_user_name = module.params['user']

        api_user_password = module.params['password']

        datacenter_url_path = '/api/v2/datacenter/'

        job_url_path = '/api/v2/management-server/jobs/'

        resource_name = 'svm/svms'

        storage_provider_url_path = '/api/v2/storage-provider/'

        server_details = 'https://' + api_host + ':' + api_port

        url_path = datacenter_url_path + resource_name



        # Global Constants

        global ABSENT

        global JOB_KEY

        global JOB_STATE

        global JOB_STATUS

        global KEY

        global NUM_RECORDS

        global PRESENT

        global RETRY_COUNT

        global UUID



        ABSENT      = 'absent'

        JOB_KEY     = 'key'

        JOB_STATE   = "completed"

        JOB_STATUS  = "normal"

        KEY         = 'key'

        NUM_RECORDS = 'num_records'

        PRESENT     = 'present'

        RETRY_COUNT = 300

        UUID        = 'uuid'



        # Properties details

        global aggregate

        global cifs_ad_domain_fqdn

        global cifs_ad_domain_password

        global cifs_ad_domain_user

        global cifs_enabled

        global cifs_name

        global cluster

        global dns_domains

        global dns_servers

        global fcp_enabled

        global ip_interface_address

        global ip_interface_enabled

        global ip_interface_home_node_name

        global ip_interface_name

        global ip_interface_netmask

        global ip_space_name

        global isDelete

        global isPost

        global iscsi_enabled

        global language

        global ldap_name

        global ldap_ad_domain

        global ldap_base_dn

        global ldap_bind_dn

        global ldap_enabled

        global ldap_servers

        global name

        global nfs_enabled

        global nis_domain

        global nis_enabled

        global nis_servers

        global nvme_enabled

        global operational_state

        global routes_destination_address

        global routes_destination_family

        global routes_destination_netmask

        global routes_gateway

        global snapshot_policy

        global subtype



        aggregate = module.params['aggregate']

        cifs_ad_domain_fqdn = module.params['cifs_ad_domain_fqdn']

        cifs_ad_domain_user = module.params['cifs_ad_domain_user']

        cifs_ad_domain_password = module.params['cifs_ad_domain_password']

        cifs_enabled = module.params['cifs_enabled']

        cifs_name = module.params['cifs_name']

        cluster = module.params['cluster']

        ip_space_name = module.params['ip_space_name']

        name = module.params['name']

        dns_domains = module.params['dns_domains']

        dns_servers = module.params['dns_servers']

        fcp_enabled = module.params['fcp_enabled']

        ip_interface_enabled = module.params['ip_interface_enabled']

        ip_interface_address = module.params['ip_interface_address']

        ip_interface_netmask = module.params['ip_interface_netmask']

        ip_interface_home_node_name = module.params['ip_interface_home_node_name']

        ip_interface_name = module.params['ip_interface_name']

        isDelete = 0

        isPost = 0

        iscsi_enabled = module.params['iscsi_enabled']

        language = module.params['language']

        ldap_name = module.params['ldap_name']

        ldap_ad_domain = module.params['ldap_ad_domain']

        ldap_base_dn = module.params['ldap_base_dn']

        ldap_bind_dn = module.params['ldap_bind_dn']

        ldap_enabled = module.params['ldap_enabled']

        ldap_servers = module.params['ldap_servers']

        nfs_enabled = module.params['nfs_enabled']

        nis_domain = module.params['nis_domain']

        nis_enabled = module.params['nis_enabled']

        nis_servers = module.params['nis_servers']

        nvme_enabled = module.params['nvme_enabled']

        operational_state = module.params['operational_state']

        routes_destination_address = module.params['routes_destination_address']

        routes_destination_family = module.params['routes_destination_family']

        routes_destination_netmask = module.params['routes_destination_netmask']

        routes_gateway = module.params['routes_gateway']

        snapshot_policy = module.params['snapshot_policy']

        subtype = module.params['subtype']



    def post(self):

        payload = {}

        aggregate_key_list = []

        dns_domains_list = []

        dns_servers_list = []

        nis_servers_list = []

        ldap_servers_list = []

        ip_interface_list = []

        route_list = []

        if aggregate != None:

            for aggr in aggregate:

                url_aggregate = server_details + datacenter_url_path + 'storage/aggregates?cluster.name=' + cluster + "&name=" + aggr

                aggregate_key_payload = {}

                aggregate_key_payload[KEY] = parse_for_resource_key(url_aggregate, aggr)

                aggregate_key_list.append(aggregate_key_payload)

            payload['aggregates'] = aggregate_key_list

        if cluster != None:

            cluster_payload = {}

            cluster_payload[KEY] = cluster_key

            payload['cluster'] = cluster_payload

        if ip_space_name != None:

            ipspace_payload = {}

            ipspace_payload['name'] = ip_space_name

            payload['ipspace'] = ipspace_payload

        if name != None:

            payload['name'] = name

        if language != None:

            payload['language'] = language

        if dns_domains != None and dns_servers != None:

            dns_domain_len = dns_domains.__len__()

            count = 0

            dns_payload = {}

            while count < dns_domain_len:

                dns_domains_list.append(dns_domains[count])

                count = count + 1

            dns_payload['domains'] = dns_domains_list



            dns_server_len = dns_servers.__len__()

            count = 0

            while count < dns_server_len:

                dns_servers_list.append(dns_servers[count])

                count = count + 1

            dns_payload['servers'] = dns_servers_list

            payload['dns'] = dns_payload

        if nis_domain != None or nis_servers != None or nis_servers != None:

            nis_payload = {}

            nis_payload['domain'] = nis_domain

            nis_payload['enabled'] = nis_enabled

            for nis_server in nis_servers:

                nis_servers_list.append(nis_server)



            nis_payload['servers'] = nis_servers_list

            payload['nis'] = nis_payload

        if ldap_name != None or ldap_ad_domain != None or ldap_base_dn != None or ldap_bind_dn != None or ldap_enabled != None or ldap_servers != None:

            ldap_payload = {}

            if ldap_name != None:

                ldap_payload['name'] = ldap_name

            if ldap_ad_domain != None:

                ldap_payload['ad_domain'] = ldap_ad_domain

            if ldap_base_dn != None:

                ldap_payload['base_dn'] = ldap_base_dn

            if ldap_bind_dn != None:

                ldap_payload['bind_dn'] = ldap_bind_dn

            if ldap_enabled != None:

                ldap_payload['enabled'] = ldap_enabled

            if ldap_servers != None:

                for ldap_server in ldap_servers:

                    ldap_servers_list.append(ldap_server)



                ldap_payload['servers'] = ldap_servers_list

            payload['ldap'] = ldap_payload

        if ip_interface_name != None or ip_interface_address != None or ip_interface_netmask != None or ip_interface_home_node_name != None or ip_interface_enabled != None:

            ip_interface_name_count = ip_interface_name.__len__()

            ip_interface_address_count = ip_interface_address.__len__()

            ip_interface_netmask_count = ip_interface_netmask.__len__()

            ip_interface_home_node_name_count = ip_interface_home_node_name.__len__()

            ip_interface_enabled_count = ip_interface_enabled.__len__()

            count = 0

            while count < ip_interface_name_count:

                ip_interface_payload = {}

                ip_info_payload = {}

                ip_interface_payload['name'] = ip_interface_name[count]

                if count < ip_interface_address_count:

                    ip_info_payload['address'] = ip_interface_address[count]

                if count < ip_interface_netmask_count:

                    ip_info_payload['netmask'] = ip_interface_netmask[count]

                ip_interface_payload['ip'] = ip_info_payload

                if count < ip_interface_enabled_count:

                    ip_interface_payload['enabled'] = ip_interface_enabled[count]

                if count < ip_interface_home_node_name:

                    ip_interface_location_payload = {}

                    ip_interface_location_home_node_payload = {}

                    ip_interface_location_home_node_payload['name'] = ip_interface_home_node_name[count]

                    ip_interface_location_payload['home_node'] = ip_interface_location_home_node_payload

                    ip_interface_payload['location'] = ip_interface_location_payload

                ip_interface_list.append(ip_interface_payload)

                count = count + 1



            payload['ip_interfaces'] = ip_interface_list

        if routes_destination_address != None or routes_destination_netmask != None or routes_destination_family != None or routes_gateway != None:

            routes_destination_address_count = routes_destination_address.__len__()

            routes_destination_family_count = routes_destination_family.__len__()

            routes_destination_netmask_count = routes_destination_netmask.__len__()

            routes_gateway_count = routes_gateway.__len__()

            count = 0

            while count < routes_gateway_count:

                routes_payload = {}

                routes_destination_payload = {}

                if count < routes_destination_address_count:

                    routes_destination_payload['address'] = routes_destination_address[count]

                if count < routes_destination_netmask_count:

                    routes_destination_payload['netmask'] = routes_destination_netmask[count]

                if count < routes_destination_family_count:

                    routes_destination_payload['ip_address_family'] = routes_destination_family[count]

                routes_payload['destination'] = routes_destination_payload

                if count < routes_gateway_count:

                    routes_payload['gateway'] = routes_gateway[count]

                route_list.append(routes_payload)

                count = count + 1



            payload['routes'] = route_list

        if cifs_name != None or cifs_ad_domain_fqdn != None or cifs_ad_domain_user != None or cifs_ad_domain_password != None or cifs_enabled != None:

            cifs_payload = {}

            if cifs_name != None:

                cifs_payload['name'] = cifs_name

            if cifs_enabled != None:

                cifs_payload['enabled'] = cifs_enabled

            if cifs_ad_domain_fqdn != None or cifs_ad_domain_user != None or cifs_ad_domain_password != None:

                cifs_ad_domain_payload = {}

                if cifs_ad_domain_fqdn != None:

                    cifs_ad_domain_payload['fqdn'] = cifs_ad_domain_fqdn

                if cifs_ad_domain_user != None:

                    cifs_ad_domain_payload['user'] = cifs_ad_domain_user

                if cifs_ad_domain_password != None:

                    cifs_ad_domain_payload['password'] = cifs_ad_domain_password

                cifs_payload['ad_domain'] = cifs_ad_domain_payload

            payload['cifs'] = cifs_payload

        if fcp_enabled != None:

            fcp_payload = {}

            fcp_payload['enabled'] = fcp_enabled

            payload['fcp'] = fcp_payload

        if iscsi_enabled != None:

            iscsi_payload = {}

            iscsi_payload['enabled'] = iscsi_enabled

            payload['iscsi'] = iscsi_payload

        if nfs_enabled != None:

            nfs_payload = {}

            nfs_payload['enabled'] = nfs_enabled

            payload['nfs'] = nfs_payload

        if nvme_enabled != None:

            nvme_payload = {}

            nvme_payload['enabled'] = nvme_enabled

            payload['nvme'] = nvme_payload

        if subtype != None:

            payload['subtype'] = subtype

        if operational_state != None:

            payload['state'] = operational_state

        if snapshot_policy != None:

            snapshot_policy_payload = {}

            snapshot_policy_payload['name'] = snapshot_policy

            payload['snapshot_policy'] = snapshot_policy_payload



        response = requests.post(server_details + url_path, auth=(api_user_name, api_user_password), verify=False, data=json.dumps(payload), headers=HEADERS)



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

        patch_response_key=[]

        if aggregate != None:

            for aggr in aggregate:

                url_aggregate = server_details + datacenter_url_path + 'storage/aggregates?cluster.name=' + cluster + "&name=" + aggr

                aggregate_key_payload = {}

                aggregate_key_payload[KEY] = parse_for_resource_key(url_aggregate, aggr)

                aggregate_key_list.append(aggregate_key_payload)

            payload['aggregates']=aggregate_key_list

            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)

            if response.status_code == 202:

                patch_response_key.append(response.json().get('job').get(JOB_KEY))

            else:

                fail_response = response.json()

                self.parse_patch_response(patch_response_key)

        if operational_state != None:

            payload.clear()

            payload['state']=operational_state

            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)

            if response.status_code == 202:

                patch_response_key.append(response.json().get('job').get(JOB_KEY))

            else:

                fail_response = response.json()

                self.parse_patch_response(patch_response_key)

        if language != None:

            payload.clear()

            payload['language']=language

            response = requests.patch(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)

            if response.status_code == 202:

                patch_response_key.append(response.json().get('job').get(JOB_KEY))

            else:

                fail_response = response.json()

                self.parse_patch_response(patch_response_key)



        if snapshot_policy != None:

            snapshot_policy_payload = {}

            snapshot_policy_payload['name'] = snapshot_policy

            payload['snapshot_policy'] = snapshot_policy_payload

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

    if cluster != None:

        url_cluster = server_details + datacenter_url_path + "cluster/clusters?name=" + cluster

        cluster_key = get_resource_key(url_cluster)

        if cluster_key == None:

            module.exit_json(changed=False,meta="Please provide a valid Cluster name.")

    if cluster != None and name != None:

        url_svm = server_details + datacenter_url_path + resource_name + "?cluster.name=" + cluster + "&name=" + name

        key = get_resource_key(url_svm)

        if (key == None):

            return False

        return True

    else:

        return False



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



def get_post_job_status(job_key):

    """ verify job status and wait for job to complete along with acquisition """

    # to avoid infinite wait condition, in case of AIQUM takes more than 300 sec to respond.

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

            if response_json.get(NUM_RECORDS) != 0:

                embedded = response_json.get('_embedded')

                if any(record['key'] == key for record in embedded['netapp:records']):

                    time.sleep(10)

                else:

                    key_present = 0

        else:

            # Returning error message received from AIQUM

            module.exit_json(changed=False,meta=response.json())

    return



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

    if(response.status_code==200):

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

        if (response_json.get(NUM_RECORDS) == 0) :

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

    """Apply SVM operations from playbook"""

    obj = NetAppAIQUMSVMs()

    obj.apply()



if __name__ == '__main__':

    main()

