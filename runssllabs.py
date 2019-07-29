#!/usr/bin/env python
import ssllabscanner
import json
def testssllabs(url):
    data = ssllabscanner.newScan(url)
    return data

dat=testssllabs("www.maersk.com")
if(dat is None):
    print("NO RESULT")
    exit(1)
else:    
    print(dat['endpoints'][0]['grade'])
    with open('ssllabscans.json', 'w') as json_file:
        json.dump(dat, json_file)
