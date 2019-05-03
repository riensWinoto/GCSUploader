import sys
import time
#import os #use this when using environ for automatic assign Google Application Credentials
from datetime import datetime
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
                return bucket_gcs, bucket_gcs.name
        else:
            bucket_gcs = Uploader.client_bucket(self)
            return bucket_gcs, bucket_gcs.name

    def client_bucket(self):
        client = storage.Client()
        return client.get_bucket(self.bucket_name)

    def get_all_requirements (self):
        new_dir_gcs = Uploader.new_content_directory(self, str(input("Enter directory for new content: ")))
        new_name_gcs = Uploader.new_content_name(self, str(input("Enter your desired file name include extension: ")))
        local_dir = Uploader.local_content_directory(self, str(input("Enter your content directory to upload: ")))
        return new_dir_gcs, new_name_gcs, local_dir

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

    def get_date_time(self):
        date_and_time = datetime.now()
        str_date_time = date_and_time.strftime('%Y/%m/%d %I:%M:%S%p')
        return str_date_time

# initial stage
if __name__ == "__main__":
    try:
        #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "yourServiceAccount.json" # or "path/to/serviceAccount.json"
        gcsUploader = Uploader()
        gcsBucket, gcsBucketName = gcsUploader.get_bucket_name(input("Enter your bucket name: "))

# looping stage
        countNum = 0
        while countNum < 1:
            newDirGCS, newNameGCS, localDir = gcsUploader.get_all_requirements()
            pathOnGCS = newDirGCS + newNameGCS
            blobGCS = gcsBucket.blob(pathOnGCS)
            blobGCS.upload_from_filename(filename=localDir)
            dateAndTime = gcsUploader.get_date_time()
            print("In your {} bucket, your uploaded content located at {} path".format(gcsBucketName, pathOnGCS))
            print("{} is your content you just upload to GCS".format(localDir))
            print("{} is your upload date and time".format(dateAndTime) + "\n")
    except KeyboardInterrupt:
        time.sleep(1.0)
        sys.exit()