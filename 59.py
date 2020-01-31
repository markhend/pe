import string
from itertools import product
lowers = string.ascii_lowercase

##with open('words.txt', 'r') as f1: #uppercase
##    words = []
##    for line in f1:
##        words.append(line.rstrip())

with open('cipher1.txt', 'r') as f2:
    cipher = f2.readline()
    cipher = cipher[:-1].split(',')
    cipher = [int(s) for s in cipher]
    # print cipher

def find_msg():
    for a, b, c in product(lowers, repeat=3):
        msg = ""
        i = 2
        while i < len(cipher):
            msg += chr(ord(a) ^ cipher[i-2])
            msg += chr(ord(b) ^ cipher[i-1])
            msg += chr(ord(c) ^ cipher[i])
            i += 3
        # len(cipher) 1201 (not mult of 3)
        msg += chr(ord(a) ^ cipher[-1])
        # checking if there are enough spaces for 'valid' msg
        if msg.count(' ') > 200:
            print "key is", a+b+c
            return msg

msg = find_msg()
ans = sum([ord(c) for c in msg])
print "msg len is", len(msg)
print "ans is", ans
print msg

