###Run ansible playbook with hosts file

```bash
ironman@jarvis:~/workspace/gtproject/ansible/ansible_playbook$ ansible-playbook -i hosts main.yaml 

PLAY [jarvis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [192.168.0.106]

TASK [say] ***********************************************************************************************************************************************************************
ok: [192.168.0.106] => {
    "msg": "Hello World"
}

PLAY RECAP ***********************************************************************************************************************************************************************
192.168.0.106              : ok=2    changed=0    unreachable=0    failed=0   

ironman@jarvis:~/workspace/gtproject/ansible/ansible_playbook$ 
```

###Errors faced

```bash
ironman@jarvis:~/workspace/gtproject/ansible/ansible_playbook$ ansible-playbook -i hosts main.yaml 

PLAY [jarvis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
fatal: [192.168.0.106]: FAILED! => {"msg": "to use the 'ssh' connection type with passwords, you must install the sshpass program"}
        to retry, use: --limit @/home/ironman/workspace/gtproject/ansible/ansible_playbook/main.retry

PLAY RECAP ***********************************************************************************************************************************************************************
192.168.0.106              : ok=0    changed=0    unreachable=0    failed=1   ```

###Resolution

```bash

ironman@jarvis:~/workspace/gtproject/ansible/books$ sudo su
[sudo] password for ironman:          
root@jarvis:/home/ironman/workspace/gtproject/ansible/books# apt-get install sshpass
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  libido3-0.1-0
Use 'sudo apt autoremove' to remove it.
The following NEW packages will be installed:
  sshpass
0 upgraded, 1 newly installed, 0 to remove and 6 not upgraded.
Need to get 10.5 kB of archives.
After this operation, 30.7 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 sshpass amd64 1.06-1 [10.5 kB]
Fetched 10.5 kB in 0s (107 kB/s)   
Y
Selecting previously unselected package sshpass.
(Reading database ... 202161 files and directories currently installed.)
Preparing to unpack .../sshpass_1.06-1_amd64.deb ...
Unpacking sshpass (1.06-1) ...
Setting up sshpass (1.06-1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```