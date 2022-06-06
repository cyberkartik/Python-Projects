from Crypto.Cipher import AES
import binascii
import sys
import time
#from flag import flag

key = b"3N7g309d6Y7enT**"
#IV = flag
IV = b"cyberhack{test_}"

ciphertext = b"54**************************36d43a**************************1658e7**************************bb2cdabc02a058f8c3936a5fd6ddd3c50491"

message = b'Security is not a joke, mind it. But complete security is a myth'

'''
The following data is given:
        p0: b'Security is not '
        p1: b'a joke, mind it.'
        p2: b' But complete se'
        p3: b'curity is a myth'
        c0: 54**************************36d4
        c1: b'3a**************************1658'
        c2: b'e7**************************bb2c'
        c3: b'\xda\xbc\x02\xa0X\xf8\xc3\x93j_\xd6\xdd\xd3\xc5\x04\x91'

'''



def encrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.encrypt(message)


key = b"3N7g309d6Y7enT"
p0 = message[:16]
p1 = message[16:32]
p2 = message[32:48]
p3 = message[48:64]

c0 = b'\x54\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x36\xd4'
c1 = b'\x3a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x58'
c2 = b'\xe7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\x2c'
c3 = b'\xda\xbc\x02\xa0X\xf8\xc3\x93j_\xd6\xdd\xd3\xc5\x04\x91'

print("""The following data is given:
        p0: {}
        p1: {}
        p2: {}
        p3: {}
        c0: {}
        c1: {}
        c2: {}
        c3: {}""".format(p0, p1, p2, p3, c0, c1, c2, c3))


def get_key():
    end = False
    # We bruteforce the last 2 bytes
    for k in range(0xff):
        if end == True:
            break
        for j in range(0xff):
            b1 = bytes([k])
            b2 = bytes([j])
            key_fmt = key + b1 + b2

            # We use the `last - 1 ` block as a IV vector of decryption
            # Since its just an xor, and we know the first and last 2 bytes of the 'last - 1' ciphertext, we can get those correct values.
            aes = AES.new(key_fmt, AES.MODE_CBC, c2)
            cx = aes.decrypt(c3)

            c2_1 = c2[:1]
            c2_2 = c2[-2:-1]
            c2_3 = c2[-1:]
            print(cx, end='\r')
            # If the
            if cx.startswith(b'c') and cx.endswith(b'th'):
                print("Got it!")
                print("The key is: {}".format(key_fmt))
                return key_fmt
    #        if c2[2:] ==


if __name__ == "__main__":
    key = get_key()
