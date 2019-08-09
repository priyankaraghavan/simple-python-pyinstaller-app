#!/usr/bin/env python
import sys
import ssllabscanner
import json
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

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
        block_blob_service = BlockBlobService(account_name=accountname, account_key=accountkey)
        print("Blob service")
        print(block_blob_service)
        block_blob_service.create_blob_from_path(containername,blobname,jsonname, content_settings=ContentSettings(content_type='json'))
        print("Rating is:",r1)
        if(r1!='A'):
           print("Failure!Rating is"+r1)
           exit(1)
        else:    
            print("Success!Rating is"+r1)
main()
