#!/usr/bin/python3
"""
Quick script for testing serial communication to a
gq EMF detector on ttyUSB0
"""

import serial
import binascii

TEST_STRING = b'<GETVER>>'

#data records come as a date row + some number of data rows
# until the first date record, then it is 180 data rows after
#180 rows at 14 bytes each + date row of 8 bytes
#180*14 + 8 = 2528 DEC = 9E0 HEX
# call <SPIR 00 00 00 09 E0>>
# to get at least one time record
# max data per request = 65535 DEC = FFFF HEX (unless there's 
# another undocumented change)


port = serial.Serial('/dev/ttyUSB0', 115200 )

port.timeout = 6

port.write( TEST_STRING )

port.flush()

response = port.read( 1024 )

print(response)

TEST_STRING = bytearray(b'<SPIR\x00\x00\x00\x10\x20>>')
TEST_STRING = b'<SPIR\x00\x00\x00\x09\xe0>>'
TEST_STRING = b'<SPIR\x00\x00\x00\x12\x20>>'
TEST_STRING = b'<SPIR\x00\x00\x00\xff\xff>>'

port.write( TEST_STRING )

port.flush()

response = port.read( 65535 )

# Uncomment for raw data
#print(response)
#print("-----------------")
# print as ascii-expanded hex
print(binascii.b2a_hex(response))

port.close()
