#!/usr/bin/env python

### This is Fabric python script which runs the main.py , main.py has some couple of script which getting imported by
# this and and executed on the run and yeilds the output ###
## ==============================================================================================###
import sys
from fabric.api import *
env.skip_bad_hosts=True
env.command_timeout=120
env.user = 'karn'
env.shell = "/bin/sh -c"
env.warn_only = True
env.password = 'pass123'
def read_hosts():
    env.hosts = [line.strip() for line in sys.stdin.readlines()]

def system_Health():
  with settings(warn_only=True):
         output=sudo("/home/karn/mainRun.py", shell=False)
