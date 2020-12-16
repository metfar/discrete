#!/bin/bash
python sequence.py -r -2147483648 2147483648|grep "#"|cut -f 2 -d\# |tr  '\n' ' '> data.dat
python sequence.py -r -65536 65536|grep "#"|cut -f 2 -d\# |tr  '\n' ' '> mindata.dat

