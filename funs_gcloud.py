from google.cloud import storage
import os
import json


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def upload_to_gcloud(_list):
    aux = 0  
    try:
        for airp in _list:
            client = storage.Client()
            bucket = client.bucket('imf-bucket-example')
            blob = bucket.blob('airports/' + airp['detailedName'].replace('/','_').replace(' ','_').replace("'",'' )+'.json')
            blob.upload_from_string(json.dumps(airp))
            aux+=1
            print('File {} uploaded successfully'.format(airp['detailedName']))
    except Exception as e:
            print(f"Error: {e}")
    print('{} files out of a total {} have been successfully uploaded'.format(aux,len(_list)))




def getFilesList(_carpeta):
    
    client = storage.Client()
    blobs = client.list_blobs('imf-bucket-example', prefix=_carpeta)
    
    lista = []
    for blob in blobs:
        lista.append(blob.name)
    
    return lista

def getFile(_blob):
    client = storage.Client()
    bucket = client.bucket('imf-bucket-example')
    
    blob = bucket.blob(_blob)
    content = blob.download_as_string()
    
    return content

def txt_2_json(_content):
    return json.loads(_content)

