###Ansible Galgaxy Init

``` bash
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy$ ansible-galaxy init automation
- automation was created successfully
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy$ ls -lrt 
total 4
drwxrwxr-x 10 ironman ironman 4096 Sep  9 11:37 automation
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy$ cd automation/
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy/automation$ ll
total 44
drwxrwxr-x 10 ironman ironman 4096 Sep  9 11:37 ./
drwxrwxr-x  3 ironman ironman 4096 Sep  9 11:37 ../
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 defaults/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 files/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 handlers/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 meta/
-rw-rw-r--  1 ironman ironman 1328 Sep  9 11:37 README.md
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 tasks/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 templates/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 tests/
drwxrwxr-x  2 ironman ironman 4096 Sep  9 11:37 vars/
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy/automation$ tree
.
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 8 files
ironman@jarvis:~/workspace/gtproject/ansible/ansible_galaxy/automation$ 
```