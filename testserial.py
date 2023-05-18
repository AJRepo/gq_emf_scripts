#!/usr/bin/python3
"""
Quick script for testing serial communication to a
gq EMF detector on ttyUSB0
"""

import serial
import binascii

TEST_STRING = b'<GETVER>>'

#data records come as a date row + 91 data rows 
#91 rows at 14 bytes each + date row of 8 bytes
#91*14 + 8 = 1274 + 8 = 502  (508 HEX)
# Double = 2564 = 0A04 HEX
# so we'll call <SPIR 00 00 00 0a 04>>
# to get a two uninterrupted records


port = serial.Serial('/dev/ttyUSB0', 115200 )

port.timeout = 1.5

port.write( TEST_STRING )

port.flush()

response = port.read( 2564 )

print(response)

TEST_STRING = bytearray(b'<SPIR\x00\x00\x00\x10\x20>>')
TEST_STRING = b'<SPIR\x00\x00\x00\x10\x20>>'
TEST_STRING = b'<SPIR\x00\x00\x00\x0a\x04>>'

port.write( TEST_STRING )

port.flush()

response = port.read( 2564 )

#print(response)
#print("-----------------")
print(binascii.b2a_hex(response))

port.close()
