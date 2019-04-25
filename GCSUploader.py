import sys
# import os #use this when using environ for automatic assign Google Application Credentials
from google.cloud import storage


class Uploader:

    def get_bucket_name(self, bucket_name):
        self.bucket_name = bucket_name
        if self.bucket_name == "":
            self.bucket_name = input("Please enter your bucket name: ")
            if self.bucket_name == "":
                print("Next time fill your bucket name")
                sys.exit()
            else:
                bucket_gcs = Uploader.client_bucket(self)
                return bucket_gcs
        else:
            bucket_gcs = Uploader.client_bucket(self)
            return bucket_gcs

    def client_bucket(self):
        client = storage.Client()
        return client.get_bucket(self.bucket_name)

    def new_content_directory(self, new_content_dir):
        self.new_content_dir = new_content_dir
        if self.new_content_dir == "":
            return self.new_content_dir
        else:
            self.new_content_dir = self.new_content_dir + "/"
            return self.new_content_dir

    def new_content_name(self, content_new_name):
        self.content_new_name = content_new_name
        if self.content_new_name == "":
            self.content_new_name = str(input("Please enter your desired file name include extension: "))
            if self.content_new_name == "":
                print("Next time fill your desired file name include extension")
                sys.exit()
            else:
                return self.content_new_name
        else:
            return self.content_new_name

    def local_content_directory(self, content_directory):
        self.content_directory = content_directory
        if self.content_directory == "":
            self.content_directory = str(input("Please enter your content directory to upload: "))
            if self.content_directory == "":
                print("Next time fill your content directory to upload")
            else:
                return self.content_directory
        else:
            return self.content_directory

# initial stage
if __name__ == "__main__":
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "yourServiceAccount.json" # or "path/to/serviceAccount.json
    gcsUploader = Uploader()
    gcsBucket = gcsUploader.get_bucket_name(input("Enter your bucket name: "))

# looping stage
    countNum = 0
    while countNum < 1:
        newDirGCS = gcsUploader.new_content_directory(str(input("Enter directory for new content: ")))
        newNameGCS = gcsUploader.new_content_name(str(input("Enter your desired file name include extension: ")))
        localDir = gcsUploader.local_content_directory(str(input("Enter your content directory to upload: ")))
        pathOnGCS = newDirGCS + newNameGCS
        blobGCS = gcsBucket.blob(pathOnGCS)
        blobGCS.upload_from_filename(filename=localDir)
        print("This is your content directory and name: " + pathOnGCS)
        print("this is your content you upload to GCS: " + localDir + "\n")