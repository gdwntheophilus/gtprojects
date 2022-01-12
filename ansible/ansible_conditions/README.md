### Conditions

```yaml
task:
  - name: run if operating system is debian
    command: echo "I am a Debian Computer"
    when: ansible_os_family == "Debian"
```

###Common use
```yaml
when: ansible_os_family == "CentOS"
when: ansible_os_family == "Redhat"
when: ansible_os_family == "Darwin"
when: ansible_os_family == "Debian"
when: ansible_os_family == "Windows"
```

```yaml
### Conditions
when: ansible_os_family == "Debian"
when: myvariablename is defined
when: webservers in group_names
when: result|failed
when: ansible_os_family == "Debian" and ansible_pkg_mgr == "apt"

when:
    ansible_distribution in ['RedHat', 'CentOS', 'ScientificLinux'] and
    (ansible_distribution_version|version_compare('7', '<') or
    ansible_distribution_version|version_compare('8', '>='))
    or
    ansible_distribution == 'Fedora'
    or
    ansible_distribution == 'Ubuntu' and
    ansible_distribution_version|version_compare('15.04', '>=')
```