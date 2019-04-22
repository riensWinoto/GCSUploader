import sys
from google.cloud import storage

class Uploader:

    def getBucketName(self, bucketName):
        self.bucketName = bucketName

        if self.bucketName == "":
            self.bucketName = input("Please enter your bucket name:")
            if self.bucketName == "":
                print("Next time fill your bucket name")
                sys.exit()
            else:
                bucketNameGCS = clientBucket(self)
                return bucketNameGCS

        else:
            bucketNameGCS = clientBucket(self)
            return bucketNameGCS

    def enterDirNewContent(self, dirNewContent):
        self.dirNewContent = dirNewContent
        return self.dirNewContent

    def enterNewContentName(self, newContentName):
        self.newContentName = newContentName
        if self.newContentName == "":
            self.newContentName = str(input("Please enter your desired file name include extension: "))
            if self.newContentName == "":
                print("Next time fill your desired file name include extension")
                sys.exit()
            else:
                return self.newContentName

        else:
            return self.newContentName

    def enterLocalContentDir(self, localContentDir):
        self.localContentDir = localContentDir
        return self.localContentDir

def clientBucket(self):
    client = storage.Client()
    return client.get_bucket(self.bucketName)

# initial stage
gUploader = Uploader()
bucketIS = gUploader.getBucketName(input("Enter your bucket name:"))

# looping stage
countNum = 0
while countNum < 1:
    dirContentGCS = gUploader.enterDirNewContent(str(input("Enter directory for new content and end with /: ")))
    nameContentGCS = gUploader.enterNewContentName(str(input("Enter your desired file name include extension: ")))
    localDir = gUploader.enterLocalContentDir(str(input("Enter your content directory to upload: ")))
    dirImgOut = dirContentGCS + nameContentGCS
    blobGCS = bucketIS.blob(dirImgOut)
    blobGCS.upload_from_filename(filename=localDir)
    print("This is your content directory and name:" + dirImgOut)
    print("this is your content you upload to GCS:" + localDir + "\n")