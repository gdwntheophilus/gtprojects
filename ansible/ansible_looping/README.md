###Ansible: Looping
```yaml
- name: Add lines to this file
  lineinfile: dest=/etc/file line={{ item }} state=present
  with_items:
   - Line 1
   - Line 2
   - Line 3
```

### from group vars or host vars
```yaml
###From vars:
favorite_snacks:
  - hotdog
  - ice cream
  - chips
###and then the loop:
- name: create directories for storing my snacks
  file: path=/etc/snacks/{{ item }} state=directory
  with_items: '{{ favorite_snacks }}'
```


###with_items - predefined dictionary
```yaml
###From vars:
packages:
- present: tree
- present: nmap
- absent: apache2
###then the loop:
- name: manage packages
  package: name={{ item.value }} state={{ item.key }}
  with_items: '{{ packages }}'
###Or, if you don't like to use the key value:
###vars:
  packages:
- name: tree
  state: present
- name: nmap
  state: present
- name: apache2
  state: absent
  then the loop:
- name: manage packages
  package: name={{ item.name }} state={{ item.state }}
  with_items: '{{ packages }}'
```

###with_items - dictionary

```yaml
- name: manage packages
  package: name={{ item.name }} state={{ item.state }}
  with_items:
    - { name: tree, state: present }
    - { name: nmap, state: present }
    - { name: apache2, state: absent }
```


###Actual Execution

```yaml
ironman@jarvis:~/workspace/gtproject/ansible/ansible_looping$ ansible-playbook -i hosts main.yaml 

PLAY [jarvis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [loop items] ****************************************************************************************************************************************************************
ok: [localhost] => (item=None) => {
    "msg": "Godwin Theophilus"
}

PLAY RECAP ***********************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0   

ironman@jarvis:~/workspace/gtproject/ansible/ansible_looping$ 
```