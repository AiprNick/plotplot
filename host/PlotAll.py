#!/usr/bin/python
import os
import matplotlib.pyplot as plt
import numpy

list_all = []
list_y = []

count = 0

while True:
   with open('tmp','r') as fp:
      for line in fp:
         if 'complete' in line:
            a = line.find('[')
            b = line.find('<')
            c = line.find('>')
            list_y.append(float(line[b+1:c])*1000000)

         if 'str' in line:
            break

   fp.close()
   
   if len(list_y)>0 and count == 0:
      list_all = list_y
      list_y = []
      count += 1
      print list_all
   if len(list_y) > 0 and len(list_all) > 0:
      list_all.append(list_y[len(list_y)-1])
      list_y = []
      count += 1
      print list_all
   # count is able to adjust
   if count >= 15000:
      list_y = []
      list_x = range(len(list_all))
      break
   os.system("sleep 1")

plt.xlim(0,count)
plt.ylim(0,100)
plt.plot(list_x, list_all,'bo')
plt.show()

