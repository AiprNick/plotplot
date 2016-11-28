#!/usr/bin/python
import os
n = 0
while True:
    os.system("sshpass -p 12433 scp nicklin@192.168.1.3:~/tmp ./")
    os.system("sleep 1")

