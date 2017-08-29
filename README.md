# HealthCheck
HealthCheck repo consists few python written modules for UNIX Systems health status

There are three main modules :

1) fsusaage.py  -> This module Checks the Filesystem usage on the host and reports the usage like "/root" & "/var"
2) processCheck.py -> This module checks the Diffrent Service process and returns the status like sendmail, ntp etc.
3) getSpeedInfo.py -> This module fetches the Current NIC Speed the NIC running with and reports the Speed Status.
4) healthCheck_Parsing.py -> This module parses the report file generated by the above all modules checks the report for
   not running Services and then sends the e-mail to the desired recepients.
   
5) mainRun.py  --> This is just import all the above modules and runs as a master module to collect all the output from all these scripts.
