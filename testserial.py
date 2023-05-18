#!/usr/bin/python3
"""
Quick script for testing serial communication to a
gq EMF detector on ttyUSB0
"""

import serial

TEST_STRING = b'<GETVER>>'


port = serial.Serial('/dev/ttyUSB0', 115200 )

port.timeout = 1.5

port.write( TEST_STRING )

port.flush()

response = port.read( 4098 )

print(response)

TEST_STRING = bytearray(b'<SPIR\x00\x00\x00\x10\x00>>')
TEST_STRING = b'<SPIR\x00\x00\x00\x10\x00>>'

port.write( TEST_STRING )

port.flush()

response = port.read( 4098 )

print(response)

port.close()
