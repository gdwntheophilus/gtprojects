### using group vars and host vars

```yaml

ironman@jarvis:~/workspace/gtproject/ansible/ansible_group_variables$ ansible-playbook -i hosts main.yaml 

PLAY [home] **********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 8081
}

PLAY [jarvis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 8080
}

PLAY [all] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 80
}

PLAY RECAP ***********************************************************************************************************************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0   

ironman@jarvis:~/workspace/gtproject/ansible/ansible_group_variables$ ansible-playbook -i hosts main.yaml 

PLAY [home] **********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 8111
}

PLAY [jarvis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 8111
}

PLAY [all] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [localhost]

TASK [say] ***********************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 8111
}

PLAY RECAP ***********************************************************************************************************************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0   

ironman@jarvis:~/workspace/gtproject/ansible/ansible_group_variables$ 
```
