def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3():
    client.upload_fileobj(infile, bucket, name)
