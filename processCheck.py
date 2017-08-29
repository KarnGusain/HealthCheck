#!/usr/bin/env python
##################################################################################################################
### Title: processCheck.py
### Version: 02
### Published : 30th March 2017
### Author : Karn Kumar (karn.itguy@gmail.com)
### This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
### without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
##################################################################################################################
import subprocess
import socket
hst_name = (socket.gethostname())
print "HostName:", hst_name
############### Function to Check the Different process & Service Status #########

def call_function(service):
   #return subprocess.call('ps -e | grep service> /dev/null 2>&1', shell=True)
   return subprocess.call('ps -e | grep %s > /dev/null 2>&1' % service, shell=True)
ps_ntp = call_function("ntp")
ps_nscd = call_function("nscd")
ps_mail = call_function("sendmail")
ps_postfix = call_function("qmgr")
ps_altris = call_function("aex-plug")
ps_automnt = call_function("automount")

if ps_ntp == 0:
    print "Service Status:  NTP is Running on the host", hst_name
else:
   print  "Service Status:  NTP is not Running on the host", hst_name

if ps_nscd == 0:
   print "Service Status:  NSCD is Running on the host", hst_name
else:
   print "Service Status:  NSCD is not Running on the host", hst_name

if ps_mail == 0:
   print "Service Status:  Sendmail is Running on the host", hst_name
elif ps_postfix == 0:
   print "Service Status:  Postfix  is Running on the host", hst_name
else:
   print "Service Status:  Sendmail is not Running on the host", hst_name

if ps_altris == 0:
   print "Service Status:  Altris is Running on the host", hst_name
else:
   print "Service Status:  Altris is not Running on the host" , hst_name

if ps_automnt == 0:
   print "Service Status:  Automount is Running on the host" , hst_name
else:
   print "Service Status:  Automont is not Running on the host" , hst_name

