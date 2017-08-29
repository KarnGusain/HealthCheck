#!/usr/bin/python
import sys
import re
var1 = ''
var2 = ''
Html_file= open("/var/healthCheck_result.html","w")
html_str = """
<table border=1>
     <tr>
       <th bgcolor=fe9a2e>Hostname</th>
       <th bgcolor=fe9a2e>Service</th>
     </tr>
"""
Html_file.write(html_str)
fh=open(sys.argv[1],"r")
for line in fh:
	pat_match=re.match("^\s+\"HostName:\s+(.*?)\".*", line)
	pat_match1=re.match("^\s+(.*?\")Service Status:\s+(.*Not.*?)\".*", line)
	if pat_match:
		Html_file.write("""<TR><TD bgcolor=fe9a2e>""" + pat_match.group(1) + """</TD>\n""")
	elif pat_match1:
		Html_file.write("""<TR><TD><TD>""" + pat_match1.group(2) + """</TD></TD></TR>\n""")
