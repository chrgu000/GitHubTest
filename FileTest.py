#!/usr/bin/env python
# coding:utf-8

import sys
import binascii

def encrypt(testfile, password):
    result = ""
    for i in testfile:
        result += chr(ord(i) ^ password)
    return result



def main():
    if len(sys.argv) != 3:
        print "Usage : "
        print "        python FileTest.py [testfile_FILE] [PASSWORD]"
        print "TIPS : "
        print "        1. password must bigger than 0 and less than 255"
        print "CONTACT : "
        print "        If  you have any questions, please check the code by youself"
        exit(1)
    try:
        filename = sys.argv[1]
        testfile_file  = open(filename)
        testfile = testfile_file.read()
    except:
        print "Open [FILE] failed."
        exit(2)
    password = int(sys.argv[2], 10) % 255
    print "[PASSWORD] : " + str(password)
    encrypted_testfile = encrypt(testfile, password)
    result_file = open("test_" + filename, "w")
    result_file.write(encrypted_testfile)
    result_file.close()
    print "[%s] Saved!" % (filename)

if __name__ == "__main__":
    main()
