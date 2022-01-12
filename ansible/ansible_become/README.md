###Become User

```yaml

- name: Run script as foo user
  command: bash.sh
  become: true
  become_user: foo
  become_method: su