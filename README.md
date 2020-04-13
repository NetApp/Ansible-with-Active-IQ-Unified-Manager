# Active IQ Unified Manager Ansible Integration Solution

The Active IQ Unified Manager Ansible Integration Solution pack contains Ansible modules and sample playbooks for Active IQ Unified Manager (AIQUM). These modules enable you to configure Service Level Objective (SLO) based storage management. The Ansible modules for AIQUM act as an orchestrator tool.

# Repository includes:

1.	Ansible modules for AIQUM
2.	Sample Playbooks
3.	README file
 
# Supported configurations:

1.	Active IQ Unified Manager version 9.7
2.	Ansible version 2.9.1
3.	Python versions 2.7.0, 3.5.0, and 3.6.0



# Overview

User can use Ansible modules for AIQUM to configure SLO-based storage management.
User can download the modules on their Ansible server by using the following configuration steps. After user has configured the modules, it can be used to write custom playbooks according to specific use cases or requirements. The modules function as an interface between Ansible and AIQUM. On using the modules, the commands provided at the Ansible server are translated into RESTful API calls to AIQUM. Responses are sent from AIQUM to the Ansible server.


# Configuration
## Prerequisites
1.	Ansible must be set up on your Red Hat Enterprise Linux 7.x system
2.	Active IQ Unified Manager version 9.7 must be installed and working

 ## Steps
1.	As a root user, log in to both the Ansible master machine and the Ansible managed servers.
2.	Edit the *ansible.cfg* file to modify the Ansible modules library folder:
```
vi /etc/ansible/ansible.cfg
```
3.	Search for the commented line with the default value for the library parameter and remove the # symbol at the beginning of the line:
```
library = /root/modules
```
4.	Log in as a root user to the Ansible server and create the modules directory at */root* level:
```
mkdir modules
```
5.	In */root/modules*, download all the modules from the *NetApp/Ansible-with-Active-IQ-Unified-Manager* directory.

**Note:** You can download these modules to either of the Master Ansible servers.

6.	Install the *requests* Python package using following command:
```
PIP install requests
```

7.	Refer to the available sample playbooks to get started.


# Module Documentation
You can access the documentation for each module by using the standard Ansible doc command:
```
ansible-doc aiqum_luns.py
```

# Support
Report any problems to: https://github.com/NetApp/Ansible-with-Active-IQ-Unified-Manager/issues
Or please report it to the following mail id: *ng-aiqum-solutions@netapp.com*

# Releases:
## 9.7
This release supports the Ansible modules compatible with Active IQ Unified Manager 9.7

## 9.7U1
This release provides a new Ansible module to manage clusters as a data source for Active IQ Unified Manager 9.7

