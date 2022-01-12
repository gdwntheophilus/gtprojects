###Commands

```bash
$ ansible localhost -m setup
$ ansible localhost -a "ls -lrt"
```

###Listing files in remote servers

```bash
ironman@jarvis:~/workspace/gtproject/ansible$ ansible localhost  -a "ls -lrt"
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

localhost | SUCCESS | rc=0 >>
total 80
-rw-rw-r-- 1 ironman ironman 46520 Sep  4 18:28 ansible_works.png
-rw-rw-r-- 1 ironman ironman 25620 Sep  4 19:09 readme.md
-rw-rw-r-- 1 ironman ironman    53 Sep  4 19:11 ansible.md
```

#####$ ansible all -m ping -k

```bash
ironman@jarvis:~/workspace/gtproject/ansible/ansible_adhoc_commands$ ansible localhost -m ping -k
SSH password: 
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

localhost | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```

#####Test sudo access with
#####$ ansible all -m ping -k -b 

```bash
ironman@jarvis:~/workspace/gtproject/ansible/ansible_adhoc_commands$ ansible localhost -m ping -k -b
SSH password: 
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

localhost | FAILED! => {
    "changed": false, 
    "module_stderr": "sudo: a password is required\n", 
    "module_stdout": "", 
    "msg": "MODULE FAILURE", 
    "rc": 1
}
```