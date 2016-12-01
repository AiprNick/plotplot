#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy

list_y = []
list_y_old = []

#total=zone[0]
#under_twenty=zone[1]
#twenty_thirty=zone[2]
#thirty_fourty=zone[3]
#fourty_fifty=zone[4]
#above_fifty=zone[5]
zone = numpy.zeros(6)
zone_lebal = ['total','<20','20 ~ 30','30 ~ 40','40 ~ 50','>50']
def cal(val):
   if val <= 20:
      zone[1] += 1
   if val > 20 and val <= 30:
      zone[2] += 1
   if val > 30 and val <= 40:
      zone[3] += 1
   if val > 40 and val <= 50:
      zone[4] += 1
   if val > 50:
      zone[5] += 1
   
   zone[0] += 1

   return

def showResult():
   for i in range(0,6,1):
      print zone_lebal[i] + " : " + str(float(zone[i])/float(zone[i-i])*100) + "%"
   return

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
   
   if len(list_y) == 0:
      list_y=list_y_old

   list_x=range(len(list_y))

   fp.close()

   plt.ion()
   line, = plt.plot(list_x, list_y, 'r-')

   plt.axis([0, 20, 0, 100])
   
   cal(list_y[0])
   print list_y

   showResult()

   if len(list_x) == len(list_y):
      plt.plot(list_x, list_y, 'bo')
      plt.draw()

   list_y_old = list_y
   list_y = []
   plt.pause(1)
   plt.gcf().clear()
