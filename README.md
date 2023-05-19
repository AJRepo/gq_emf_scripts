# gq_emf_scripts
Program to test communications with the gq emf detector

Debugging the Portable GQ EMF-390 tool led to the need to test
via raw serial commands and to get back the raw data. 

Simple scripts for testing that device


TEST_STRING = b'<GETVER>>'

Results in
b'GQ-EMF390v2Re 3.72\r\n'

---
```
Data records come as 
date row + N data rows (where N <= 180)
date row + 180 data rows

Dumping the first two timestamped data records

55aa1705100e3737
aa550013404f8042c43119485a02
aa550013404f8042c43119485a02
aa550013404f8042c43119485a02
aa550013404f8042c43119485a02
aa550013ce1f8142ab9c0b485a02
aa5500148d567e42947efc475a08
aa55001362cc8042947efc475a08
aa55001365fd7e4280b721485a02
aa55001321037e420e021e485a02
... 82 more records ...
55aa1705100e391a
aa550013c1677b42f03f47485a08
aa550013c1677b424fb745485a02
aa550014eac07a42e60237485a02
aa55001471b57c42545a4a485a08
aa550014b5af7d429acb48485a08
aa550014121a7a42652f41485a08
aa550014990e7c4218194f485a08
aa550014dd087d42545a4a485a08
aa550013c1677b420e814d485a08
... 170 more records ...
55aa1705100f0019
aa550013e3e47b42289a35485a02
... etc ... 
```
