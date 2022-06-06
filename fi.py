from Crypto.Cipher import DES
import codecs

plain1 = b'Python is the Best Language!'
cipher2 = b'\x01\x08\xb5\xb1\xccu\t\x873/\xc0\x04$\x8f\r\x89\xf6\x80kv\x8aj\xe8\xe8\xd8\x9a{\x16\x1dz\xee\xc7'
key1 = b'm33t1n'
key2 = b'0Fr34k'
plains2 = dict()
ciphers1 = dict()
i = 0
while i <= 0xff:
    j = 0
    while j <= 0xff:
        tmp_key = key1 + bytes ([i, j])
        des1 = DES.new(tmp_key, DES.MODE_ECB)
        ciphers1[tmp_key] = des1.encrypt(plain1)
        j += 1
    i += 1
i = 0
while i <= 0xff:
    j = 0
    while j <= 0xff:
        tmp_key = key2 + bytes ([i, j])
        des2 = DES.new(tmp_key, DES.MODE_ECB)
        plains2[tmp_key] = des2.encrypt(cipher2)
        j += 1
    i += 1

set1 = set(ciphers1.values())
set2 = set(plains2.values())
int_set = set1.intersection(set2)
final_msg = int_set.pop()
print("intersection:", final_msg)
for k in ciphers1:
    if ciphers1[k] == final_msg:
        print('key1:', k)


for k in plains2:
    if plains2[k] == final_msg:
        print('key1:', k)
