#!/usr/bin/env python
###################################################################################################################
##### last modified 4/20/2017.
##### Version: 02
##### Published : 30th March 2017
##### Author : Karn Kumar (karn.itguy@gmail.com)
##### This Scripts checks the threshold Value and returns the Status of its  Well being.
##### This Script can be extended to check the number of Filesystem and can be added under the "fs_main" function.
##### This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
##### without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
####################################################################################################################
import subprocess
import socket
threshold = 92
hst_name = (socket.gethostname())

def fs_function(usage):
   return_val = None
   try:
      return_val = subprocess.Popen(['df', '-Ph', usage], stdout=subprocess.PIPE)
   except IndexError:
      print "Mount point not found."
   return return_val


def show_result(output, mount_name):
   if len(output) > 0:
      for x in output[1:]:
          perc = int(x.split()[-2][:-1])
          if perc >= threshold:
            print "Service Status:  Filesystem For " + mount_name + " is not normal and " + str(perc) + "% used on the host",hst_name 
          else:
            print "Service Status:  Filesystem For " + mount_name + " is normal on the host",hst_name 

def fs_main():
   rootfs = fs_function("/")
   varfs  = fs_function("/var")
   tmPfs = fs_function("/tmp") 

   output = rootfs.communicate()[0].strip().split("\n")
   show_result(output, "root (/)")

   output = varfs.communicate()[0].strip().split("\n")
   show_result(output, "Var (/var)")
   
   output = tmPfs.communicate()[0].strip().split("\n")
   show_result(output, "tmp (/tmp)")
fs_main()
