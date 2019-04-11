#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nslm_backup_settings
author:
    - NetApp Service Level Manager Solutions Team (ng-nslm-solutions@netapp.com)
short_description: NetApp Service Level Manager(NSLM) managed backup-settings.
description:
     - Update backup-setting on NetApp Service Level Manager(NSLM).
version_added: "2.7"
options:
  state:
    description:
    - Which state user wants for the object.
    choices: ['present']
    required: true
  day_of_week:
    description:
    - Day of the week when backup is scheduled.  Modifiable field.
    choices: ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    required: false
    state_supported: present
  frequency:
    description:
    - Frequency at which a database backup is scheduled. Among possible values, NONE implies that backup is not scheduled.  Modifiable field.
    choices: ['daily', 'weekly', 'none']
    required: true
    state_supported: present
  hour:
    description:
    - Hour of the day when backup is scheduled. The value is specified in 24-hour format.  Modifiable field.
    required: false
    state_supported: present
  minute:
    description:
    - Minute of the hour when backup is scheduled.  Modifiable field.
    required: false
    state_supported: present
  path:
    description:
    - Path to the location where backup files are stored.  Modifiable field.
    required: true
    state_supported: present
  retention_count:
    description:
    - Maximum number of backup files to be retained.  Modifiable field.
    required: true
    state_supported: present
'''

EXAMPLES = '''
---
    - name: Manage backup-setting
      nslm_backup_settings:
        hostip=<nslm_hostip>
        port=<nslm_portnumber>
        user=<nslm_username>
        password=<nslm_password>
        state=present
        frequency=none
        path=/root/
        retention_count=2
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

class NetAppNSLMBackupSettings(object):
    """Class with backup-setting operations"""

    def __init__(self):
        """Initialize module parameters"""
        fields = {
            "state" : {
                "required": True,
                    "choices": ['present'],
                    "type": 'str'
                    },
            "hostip" : {"required": True, "type": "str"},
            "port" : {"required": True, "type": "str"},
            "user" : {"required": True, "type": "str"},
            "password" : {"required": True, "type": "str"},
            "path" : {"required": True, "type": "str"},
            "retention_count" : {"required": True, "type": "int"},
            "frequency" : {"required": True,
                           "choices": ['daily', 'weekly', 'none'],
                           "type": "str"},
            "day_of_week" : {"required": False,
                             "choices": ['sunday', 'monday', 'tuesday', 'wednesday',
                                         'thursday', 'friday', 'saturday'],
                             "type": "str"},
            "hour" : {"required": False, "type": "int"},
            "minute" : {"required": False, "type": "int"},
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
        resource_name           = "backup-settings"
        resource_url_path       = "/api/management-server/admin/"
        server_details          = "https://"+api_host+":"+api_port
        url_path                = resource_url_path + resource_name

        # Global Constants
        global JOB_KEY
        global JOB_STATUS
        global RETRY_COUNT

        JOB_KEY     = "job_key"
        JOB_STATUS  = "COMPLETED"
        RETRY_COUNT = 300

        # Properties details
        global day_of_week
        global frequency
        global hour
        global minute
        global path
        global retention_count
        global json_response

        day_of_week      = module.params["day_of_week"]
        frequency        = module.params["frequency"]
        hour             = module.params["hour"]
        minute           = module.params["minute"]
        path             = module.params["path"]
        retention_count  = module.params["retention_count"]


    def put(self):
        global url_path
        payload={}
        if day_of_week != None :
            payload['day_of_week']=day_of_week
        if frequency != None :
            payload['frequency']=frequency
        if hour != None:
            payload['hour']=hour
        if minute != None:
            payload['minute']=minute
        if path != None:
            payload['path']= path
        if retention_count != None:
            payload['retention_count']=retention_count
        response = requests.put(server_details+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers=HEADERS)
	return response

    def apply(self):
        # Actions
        response=self.put()
        parse_state_response(response)

def parse_state_response(response):
    """ check the response body and take necessary state according to status code """
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

def main():
    """Apply backup-setting operations from playbook"""
    obj = NetAppNSLMBackupSettings()
    obj.apply()

if __name__ == '__main__':
    main()
