import hashlib


def md5_hash(filename):
    with open(filename,'rb')as f:
        bytes=f.read()
        md5hash=hashlib.md5(bytes).hexdigest()
        f.close()
    return md5hash
print(md5_hash('1452003.jpg'))
#malware detection hash
def malware_identifier(pathoffile):
     hash_malware_identify = md5_hash(pathoffile)
     malware_hashes=open('virushash.txt','r')
     malware_hashes_read=list(malware_hashes.read().splitlines())
     for check in malware_hashes_read:
         if check== hash_malware_identify:
             return 'red'
         else:
             return 'green'
print(malware_identifier('1452003.jpg'))
