Ansible-string-split-filter
===========================

A simple Ansible Jinja2 filter to split a string into a list.

Setup
-----

See the [http://docs.ansible.com/developing_plugins.html#distributing-plugins](plugin documentation).

Usage
-----

    split(delimiter)

    split_regex(pattern) (regex syntax is identical to Pythons) 

Examples
--------

In a Jinja 2 template:
    # hostname = dev.example.com
    ldap_server = "dc={{ hostname | split('.') | join(',dc=') }}"
Output:
    ldap_server = dc=dev,dc=example,dc=com

The same example, using split_regex:
    ldap_server = "dc={{ hostname | split_regex('\.') | join(',dc=') }}"

Contributing
------------

Any improvements are welcome. This is actually my first time publishing reusable code, so any feedback on making open-source code more useful is also appreciated!
