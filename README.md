# plotplot
simple plot script for showing duration of transmit complete interrupt

![fordemo](https://cloud.githubusercontent.com/assets/4496011/20654447/5b1a2f1e-b554-11e6-984b-0687a1b49687.png)

# Prerequisite


-python-


https://wiki.python.org/moin/BeginnersGuide


-Matplotlib-


Debian / Ubuntu : sudo apt-get install python-matplotlib


more details : http://matplotlib.org/users/installing.html


-Screen-


Debian / Ubuntu : sudo apt-get install screen



# Installation


@VM(guest)


$git clone https://github.com/AiprNick/plotplot.git


$mv plotplot/guest/ ~/


$cd ~/guest/ixgbevf-2.16.1/src/


$make



-reload vf driver-


$sudo rmmod ixgbevf


$cd ~/guest/ixgbevf-2.16.1/src/


$sudo insmod ixgbevf.ko



@host


$git clone https://github.com/AiprNick/plotplot.git


$mv plotplot/host/ ~/


# Execution


1.Start the VM


2.Record logs in VM


[guest]$./record.py &


3.Keep VM running


[guest]$./loop &


4.Background traffic in VM


[guest]$screen


[guest]$ping -i 1 (IP)


5.Fetch logs form VM


[host]$./pull.py &


6.Execute plot scripts


-Dynamic plot-


[host]$./TokenPlot.py &



-Static plot-


[host]$./Plotall.py


# Troublestooting


1.VF driver compile error


-VM's kernel is 3.16-


@VM(guest)


$cd ~/guest/ixgbevf-2.16.1/src/


$cp patch/kernel-3.16/ixgbevf_main.c ./


$make



-VM's kernel is 4.4-


@VM(guest)


$cd ~/guest/ixgbevf-2.16.1/src/


$cp patch/kernel-4.4/ixgbevf_main.c ./


$make
