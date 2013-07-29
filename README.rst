LDAP Fun with Django
====================

Where I work, we are building a Django website which will use django-auth-ldap to connect to a legacy
ActiveDirectory server for authentication. I started out knowing nothing at all about LDAP or ActiveDirectory.
This is part of my effort to stumble through it and figure it out. My strategy is to build a working
reference implementation client script, and then make sure that LDAPBackend does the same stuff, using
Wireshark to compare the network traffic.

Here's what you need to know, encapsulated into a very small working example.
The most useful references I've found so far have been

* https://blogs.oracle.com/marginNotes/entry/ldap_basics_with_python
* http://stackoverflow.com/questions/140439/authenticating-against-active-directory-using-python-ldap
* http://www.grotan.com/ldap/python-ldap-samples.html
* http://stackoverflow.com/questions/10725891/authenticating-to-active-directory-with-python-ldap-always-returns-97
* http://www.python-ldap.org/doc/html/ldap.html

As far as I can determine, the steps to authentication are to initialize, bind, and do a search,
and if the search succeeds then you had the correct credentials for the initial bind.

For purposes of authentication, it should suffice to just bind without raising an exception, I think.
