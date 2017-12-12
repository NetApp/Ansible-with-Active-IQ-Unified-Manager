# Ansible with NetApp Service Level Manager

This pack contains Ansible modules and sample playbooks which enables you to configure service level based NetApp storage management using NetApp Service Level Manager. Ansible behaves as the orchestrator tool.

# Disclaimer
These Ansible modules and sample playbooks are written as best effort and provide no warranties or SLAs, expressed or implied.

# Repository includes:
1.	Ansible NetApp Service Level Manager Modules
2.	Sample Playbooks
3.	README
 
# Supported configurations:
1. Control server distros: RHEL 7.x CentOS 7.x
2. NetApp Service Level Manager - 1.0RC3
3. Minimum ONTAP version - ONTAP 9.x

# Overview
These Ansible Modules will help you configure service level based NetApp storage management using NetApp Service Level Manager.

These modules can be downloaded on your ansible server using the configuration steps below. Once these modules are configured, they can be used in custom written playbook according to specific use cases or requirements.
The functionality of these modules is to act as an interface between Ansible and NetApp Service Level Manager. With these modules the commands given at the Ansible server will be translated to RESTful api calls to NetApp Service Level Manager and communicated back.


# Configuration
1. Get a working Ansible Setup (rhel-7 or centos-7)
3. Get a working NetApp Service Level Manager Setup
2. Sign-in as root at the Ansible Master machine and the Ansible Slave servers
3. Edit the ansible.cfg file to edit the ansible modules library folder. Run command:
vi /etc/ansible/ansible.cfg
4. Find the commented line for library default value. Remove the # sign from start of the line. Edit it to
library = /root/modules
5. At the Ansible server, sign-in with root privileges
6. Create a new directory. Command:
mkdir modules
7. Run Command:
cd modules
8. Run Command:
pwd
9. Verify that the output is "/root/modules"
10. Now download all the modules from ‘modules/NetApp Service Level Manager’ inside "/root/modules"(download these modules to either Master Ansible server or the Slave Ansible servers)
11. Install 'requests' python package
pip install requests
12. Make use of sample playbooks provided to get started


# Related Project
Ansible with OnCommand API Services for Element based NetApp storage management. Look https://github.com/NetApp/Ansible-with-OnCommand-API-Services/

# Support
Please enter an issue if you would like to report a defect
