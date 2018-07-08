#! /bin/usr/python2
# FLOAT ASSEMBLER - FA

from struct import pack, unpack
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Usage: %s <argv1> <argv2> ... <agrvi>" % sys.argv[0]
        exit()

    for a in sys.argv[1:]:

        a = float(a)
        a_bytes = pack('>d', a)
        a_int64, = unpack('>Q',a_bytes)

        a_sign = (a_int64 >> 63) & 1
        a_exp  = (a_int64 >> 52) & ((1 << 11) - 1)
        a_mant = a_int64 & ((1 << 52) -1)

        print "Float: %s" % str(a)
        print "Bin: %s" % bin(a_int64)[2:].zfill(64)
        print "Hex: %.16x" % a_int64
        print "Sign: %s" % '+-'[a_sign]
        print "Exp: %s -> %s" % (hex(a_exp),bin(a_exp)[2:].rjust(11, "0"))
        print "Mant: %s -> %s" % (hex(a_mant),bin(a_mant)[2:].rjust(52, "0"))
        print "\n"
