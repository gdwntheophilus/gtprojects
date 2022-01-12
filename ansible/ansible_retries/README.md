###Retries

```yaml

---
- hosts: my-hosts
    tasks:
    - action: uri url=http://{{ ansible_all_ipv4_addresses }}:8080/alive return_content=yes
      delegate_to: localhost
      register: result
      until: "'failed' not in result and result.content.find('OK') != -1"
      retries: 18
      delay: 10
```