#!/usr/bin/env python

import sys
import ldap
import pprint

try:
	server, dn, password = sys.argv[1:4]
except:
	print 'Usage: %s <server> <username> <password>' % sys.argv[0]
	sys.exit(0)

l = ldap.initialize('ldap://' + server)
l.set_option(ldap.OPT_REFERRALS, False)
l.protocol_version = 3
try:
    l.simple_bind_s(dn, password)
    print 'Authentication successful'
except ldap.INVALID_CREDENTIALS:
    print 'ZUT ALORS! The password she is wrong.'
    sys.exit(0)


if 'search' in sys.argv[1:]:
    # Once the bind has succeeded, we can do a search.
    # But a successful bind should be sufficient for user authentication.

    # base = "dc=qa,dc=ruelala,dc=lan"
    base = ','.join(map(lambda x: 'dc=' + x, server.split('.')))
    scope = ldap.SCOPE_SUBTREE
    Filter = "(objectClass=user)"
    attrs = ["displayName"]

    r = l.search(base, scope, Filter, attrs)
    Type, user = l.result(r, True, 10)
    pprint.pprint(user)
    for name, attrs in user:
        if Type is not None and 'displayName' in attrs:
            displayName = attrs['displayName'][0]
            print displayName
