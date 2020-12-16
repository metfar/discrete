#!/bin/bash

time python sequence.py -r -65536 65536|grep "#"|cut -f 2 -d\# |tr  '\n' ' '> mindata.dat
time python plotting.py mindata.dat
python sequence.py -r -4194304 4194304|grep "#"|cut -f 2 -d\# |tr  '\n' ' '> data.dat
python plotting.py data.dat

