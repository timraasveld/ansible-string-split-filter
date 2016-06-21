**! Ansible 2.0 has split functionality built in, see [this example](https://github.com/timraasveld/ansible-string-split-filter/issues/2#issuecomment-227422158) !**

Ansible-string-split-filter
===========================

A simple Ansible Jinja2 filter to split a string into a list.

Setup
-----

See the [plugin documentation](http://docs.ansible.com/developing_plugins.html#distributing-plugins).

Usage
-----

```python
split(delimiter)

split_regex(pattern) # regex syntax is identical to Pythons
```

Examples
--------

In a Jinja 2 template:
```python
# hostname = dev.example.com
ldap_server = "dc={{ hostname | split('.') | join(',dc=') }}"
```

Output:

```
ldap_server = dc=dev,dc=example,dc=com
```

The same example, using split_regex:

```python
ldap_server = "dc={{ hostname | split_regex('\.') | join(',dc=') }}"
```

Contributing
------------

Any improvements are welcome. This is actually my first time publishing reusable code, so any feedback on making open-source code more useful is also appreciated!
