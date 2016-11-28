#!/usr/bin/python
import os
n = 0
while True:
   os.system("dmesg -d | tail -40 > tmp")
   #n += 0
   #tmp = os.popen('dmesg -d > tmp')
   #output = tmp.read()
   os.system("sleep 1.5")
