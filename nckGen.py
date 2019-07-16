#!/usr/bin/env python3

import sys
import hashlib

offsets = [(0,8,16,24),
           (2,10,18,26),
           (4,12,20,28),
           (6,14,22,30)]
           

#5e8dd316726b0335 - Hash suffix for NCK code
#97b7bc6be525ab44 - Hash suffix for SPCK code

def getMD5Hash(imei):    
    return hashlib.md5(f"{imei}5e8dd316726b0335".encode()).hexdigest()
    
def get_bytes(offsets):
    bytes = [imei_hash[i:i+2] for i in offsets]    
    return bytes
    
def do_XOR(arr):
    tmp = [int(i,16) for i in arr]
    return hex(tmp[0] ^ tmp[1] ^ tmp[2] ^ tmp[3])[2:]  

def check_hex(bytes):
    tmp = ""
    for i in bytes:
        if len(i) == 1:
            i = '0' + i
        tmp += i
    return int(tmp,16)    
    
if __name__ == "__main__":
    imei_hash = getMD5Hash(sys.argv[1])
    imei_bytes = [get_bytes(i) for i in offsets]
    XORed_bytes = [do_XOR(i) for i in imei_bytes]
    checked = check_hex(XORed_bytes)
    nck_code = (checked & 0x1FFFFFF) | 0x2000000
    print(nck_code)
