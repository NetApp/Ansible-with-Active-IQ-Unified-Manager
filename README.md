# NetApp Service Level Manager Ansible Integration Solution

This pack contains Ansible modules and sample playbooks for NetApp® Service Level Manager (SLM) that enable you to configure service-level-based NetApp storage management. The Ansible modules for SLM act as the orchestrator tool.

# Disclaimer
This document contains best practices for Ansible modules and sample playbooks, it provides no warranties or SLAs, expressed or implied.

# Repository includes:
1.	Ansible modules for SLM 
2.	Sample playbooks (part of module documentation)
3.	README file
 
# Supported configurations:
1.	NetApp Service Level Manager version 1.2 general availability (GA) 
2.	Ansible version 2.7.0


# Overview
You can use Ansible modules for SLM to configure service-level-based NetApp storage management.

You can download the modules on your Ansible server using the following configuration steps. After you configure the modules, you can use them to write custom playbooks according to specific use cases or requirements. The modules function as an interface between Ansible and NetApp Service Level Manager. Using the modules, the commands provided at the Ansible server are translated into RESTful API calls to SLM. Responses are sent from SLM to the Ansible server.


# Configuration
## Prerequisites
1.	Ansible must be setup (RHEL-7)     
2.	NetApp Service Level Manager version 1.2 GA must be installed and working

 ## Steps
1.	Log in as root at both the Ansible Master machine and the Ansible Slave servers.
2.	To modify the Ansible modules library folder, edit the ansible.cfg file using the command:
```vi /etc/ansible/ansible.cfg```
3.	Find the commented line for the library default value; remove the # sign from start of the line and change it to:
```library = /root/modules```
4.	Log in as root at the Ansible server.
5.	Create a directory using the command:
```mkdir modules```
6.	Run the command:
```cd modules```
7.	Run the command:
```pwd```
8.	Verify that the output is:
```/root/modules```
9.	In "/root/modules”, download all modules from “modules/NetApp Service Level Manager”. 
**Note:** You can download these modules to either of the Master Ansible servers.
10.	Install the “requests” Python package PIP install requests.
11.	Use the sample playbooks provided to get started.


# Module Documentation
You can access documentation for each module using the Ansible standard doc command.
```ansible-doc nslm_luns.py```

# Support
Report any problems to: https://github.com/NetApp/Ansible-with-NetApp-Service-Level-Manager/issues
