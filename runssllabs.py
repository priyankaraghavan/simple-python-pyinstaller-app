#!/usr/bin/env python
import sys
import ssllabscanner
import json
import Writetoblob
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import time

def testssllabs(url):
    data = ssllabscanner.newScan(url)
    return data

def main():
    print("Hello")
    accountname= sys.argv[1]
    accountkey= sys.argv[2]
    containername=sys.argv[3]
    blobname=sys.argv[4]
    jsonname= sys.argv[5]
    urlname= sys.argv[6]
    dat=testssllabs(urlname)
    if(dat is None):
        print("NO RESULT")
        exit(1)
    else:    
        r1=dat['endpoints'][0]['grade']
        with open(jsonname, 'w') as json_file:
            json.dump(dat, json_file)  
        time.sleep(30)          
        Writetoblob.Writetoblob(accountname,accountkey,containername,blobname,jsonname)
        print("Rating is:",r1)
        if(r1!='A' or r1!='A+'):
           print("Failure!Rating is"+r1)
           exit(1)
        else:    
            print("Success!Rating is"+r1)
main()
