#!/usr/bin/env python
##################################################################################################################
### Title: getSpeedInfo.py
### Version: 02
### Published : 30th March 2017
### Author : Karn Kumar (karn.itguy@gmail.com)
### Please Don't edit this file with Consulting karn is this Critical to helath check ###
### This module is Just captures the running speed of NIC from ethtool & speed file #####
### This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
### without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
### 
''' Global function has been added to detect and read the speed from the file for bond Interfaces if exists '''
##################################################################################################################
import subprocess
import netifaces
import socket
import re

hst_name = (socket.gethostname())

def get_Inf():
    global Current_inf    
    Current_inf = netifaces.gateways()['default'][netifaces.AF_INET][1]
    return Current_inf

def get_bondSpeed():
    spd1 = open('/sys/class/net/{}/speed' .format(Current_inf)).read().strip()
    return spd1

def get_intSpeed():
    spd = subprocess.Popen(['/sbin/ethtool', get_Inf()], stdout=subprocess.PIPE).communicate()[0]
    pat_match=re.search(".*Speed:\s+(\d+)+.*", spd)       # "d" means any number of digit following the "Mb/s".
    speed = pat_match.group(1)
    return speed

if get_intSpeed() == str(1000):
  print "Service Status:  System is running with 1Gbit Speed on the host",hst_name

elif get_intSpeed() == str(10000):
  print "Service Status:  System is running with 10Gbit Speed on the host",hst_name

elif get_bondSpeed() == str(10000):
  print "Service Status:  System is running with 10Gbit Speed on the host",hst_name, "with bond setup!"

elif get_bondSpeed() == str(1000):
  print "Service Status:  System is running with 1Gbit Speed on the host",hst_name, "with bond setup!"

elif get_bondSpeed() == str(2000):
  print "Service Status:  System is running with 2Gbit Speed on the host",hst_name, "with bond setup!"

else:
  print "Service Status:  System is not running with Gig Speed, Please check manually on the host",hst_name

get_Inf()
