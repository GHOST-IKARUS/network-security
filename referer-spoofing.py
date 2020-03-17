#!/usr/bin/python

import sys
import httplib2

if len(sys.argv) < 2:
    print sys.argv[0] + ": <url>"
    sys.exit(1)

headers = {'Referer': 'http://www.peter-lustig.com'}
webclient = httplib2.Http()
response, content = webclient.request(sys.argv[1],
                                      'GET',
                                      headers=headers)
print content
