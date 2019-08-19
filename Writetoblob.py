#!/usr/bin/env python
import sys
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import time

def Writetoblob(accountname,accountkey,containername,blobname,filename):    
    block_blob_service = BlockBlobService(account_name=accountname, account_key=accountkey)
    print("Blob service")
    print(block_blob_service)
    block_blob_service.create_blob_from_path(containername,blobname,filename, content_settings=ContentSettings(content_type='json'))
    time.sleep(10)
    print("Done creating blob")

   
