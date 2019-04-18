import sys
from google.cloud import storage

#Function for Initial Stage
def clientBucket():
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    return bucket

#Function for Looping Stage
def contentDirectory():
    bucket = clientBucket()
    contentDir = str(input("Enter your content directory to upload: "))
    dirImgOut= directoryIn + imageIn
    blob = bucket.blob(dirImgOut)
    blob.upload_from_filename(filename=contentDir)
    print("This is your content directory and name:" + dirImgOut)
    print("this is your content you upload to GCS:" + contentDir +"\n")

#Initial Stage
bucketName = input("Enter your bucket name:")
if bucketName == "":
    bucketName = input("Please enter your bucket name:")
    if bucketName == "":
        print ("Next time fill your bucket name")
        sys.exit()
    else:
        clientBucket()
else:
    clientBucket()

#Looping Stage
countNum=0
while countNum < 1:
    directoryIn = str(input("Enter directory for new content and end with /: "))
    imageIn= str(input("Enter your desired file name include extension: "))

    if imageIn == "":
        imageIn = str(input("Please enter your desired file name include extension: "))
        if imageIn == "":
            print ("Next time fill your desired file name include extension")
            sys.exit()
        else:
            contentDirectory()
    else:
        contentDirectory()