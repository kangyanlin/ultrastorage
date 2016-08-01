import boto.s3.connection

# S3 access information
# access_key = 'JYEO98B3AZD1L1DWL33I'
# secret_key = 'M5Y5VOYHLyZidAHPmaGDFCHf9laeMw4gdJ0d7AIv'
# host = 'bk2s3-devel-1'
# port = 80

def s3_connection(access_key, secret_key, hostname, hostport):
    conn = boto.s3.connection.S3Connection(
    aws_access_key_id = access_key,
    aws_secret_access_key =  secret_key,
    host = hostname,
    port = hostport,
    is_secure = False,
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
    )
    return conn

def get_all_buckets_list(access_key, secret_key, hostname, hostport):
    conn = s3_connection(access_key, secret_key, hostname, hostport)
    buckets_list = conn.get_all_buckets()
    conn.close()
    return buckets_list

def get_bucket(bucket_name, access_key, secret_key, hostname, hostport):
    conn = s3_connection(access_key, secret_key, hostname, hostport)
    bucketnm = conn.get_bucket(bucket_name)
    conn.close()
    return bucketnm

def create_bucket(bucket_name, access_key, secret_key, hostname, hostport):
    conn = s3_connection(access_key, secret_key, hostname, hostport)
    bucket = conn.create_bucket(bucket_name)
    print 'creating a bucket: bucket_name = %s' % bucket
    conn.close()
    return bucket

def delete_bucket(bucket_name, access_key, secret_key, hostname, hostport):
    conn = s3_connection(access_key, secret_key, hostname, hostport)
    d = conn.delete_bucket(bucket_name)
    print 'deleteing a bucket ......'
    conn.close()
    return True

def upload_object_to_bucket(bucket_name, bucket_object, access_key, secret_key, hostname, hostport):
    # TODO: finish the exception
    try:
        bucket_list = get_bucket(bucket_name, access_key, secret_key, hostname, hostport)
        existed = True
    except:
        existed = False
    try:
        bucket = create_bucket(bucket_name, access_key, secret_key, hostname, hostport)
        key = boto.s3.key.Key(bucket, bucket_object)
        key.set_contents_from_filename(bucket_object)
        retr = True
    except Exception:
        retr = False
    return [existed, retr]

def download_object_from_bucket(bucket_name, bucket_object, access_key, secret_key, hostname, hostport):
    # TODO: finish the exception
    try:
        bucket_list = get_bucket(bucket_name, access_key, secret_key, hostname, hostport)
        existed = True
    except:
        existed = False
    try:
        key = boto.s3.key.Key(bucket_list, bucket_object)
        key.get_contents_to_filename(bucket_object)
        retr = True
    except Exception:
        retr = False
    return [existed, retr]