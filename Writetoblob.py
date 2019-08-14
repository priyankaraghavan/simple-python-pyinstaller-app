from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import sys
def writetoAzure(accountname,accountkey,containername,blobname,filename):    
    block_blob_service = BlockBlobService(account_name=accountname, account_key=accountkey)
    print("Blob service")
    print(block_blob_service)
    block_blob_service.create_blob_from_path(containername,blobname,filename, content_settings=ContentSettings(content_type='json'))
   
        