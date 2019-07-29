#!/usr/bin/env python
import ssllabscanner
import json
def testssllabs(url):
    data = ssllabscanner.newScan(url)
    return data

dat=testssllabs("www.maersk.com")
with open('ssllabscans.json', 'w') as json_file:
    json.dump(dat, json_file)
