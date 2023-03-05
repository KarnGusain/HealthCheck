# HealthCheck Module
HealthCheck repo consists few python written modules for UNIX Systems health status..

There are three main modules :

```
1) fsusaage.py  -> This module Checks the Filesystem usage on the host and reports the usage for them, example "/root" & "/var"
2) processCheck.py -> This module checks the Diffrent Service process and returns the status feed, example like sendmail, ntp etc.
3) getSpeedInfo.py -> This module fetches the Current NIC Speed of the active primary NIC running and reports the Speed Status.
4) healthCheck_Parsing.py -> This module parses the report file generated by the above all modules and further checks the report for
   not running Services and then sends the e-mail to the desired recepients.
5) mainRun.py  --> This module just imports all the above modules and runs as a master module to collect all the output from all these scripts.
```

Note: Just put all these scripts into the same Directoy path along with "mainRun.py" and then run it as below ....

```
$ ./mainRun.py or

$ python mainRun.py
```
There is one more Python Fabric Script "Fabfile.py" has been added if you wish you Run this Script via Fabric to multiple UNIX hosts ata time.

