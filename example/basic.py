#!/usr/bin/env python
#
# Aware TI, 2011, http://www.aware.com.br
# Thiago Rondon <thiago@aware.com.br>
#

from nsms_web_api import NSMS

foo = NSMS('username', 'password')
print foo.auth()

print foo.send('1183320022', 'teste')

