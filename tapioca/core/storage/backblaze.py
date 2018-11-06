from tapioca.core.storage import BlockBucket

class BackblazeBucket(BlockBucket):

    def __init__(self, bucket, prefix=None):
        self.bucket = bucket.files
        self.prefix = prefix or ''

    def upload_file(self, path, data):
        self.bucket.upload(file_name=path, contents=data)
