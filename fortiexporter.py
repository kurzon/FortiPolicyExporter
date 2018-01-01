# Fortigate 5.2.x Policy Exporter v1.0
# Put the output of the "show firewall policy" command into the same directory of this script.
# It will create a file called output.csv in the same directory.

from __future__ import print_function
import re
import sys

with open('fw.txt', 'r') as testfile:
    data=testfile.read().replace('\n', '')

output0  = re.compile('edit(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)
output1  = re.compile('srcintf(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)
output2  = re.compile('dstintf(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)
output3  = re.compile('srcaddr(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)
output4  = re.compile('dstaddr(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)
output5  = re.compile('service(.*?)set', re.DOTALL |  re.IGNORECASE).findall(data)

rows=len(output1)


csv=open('output.csv', 'w')

print ("PoliycID,Source Interface,Destination Interface,Source IP,Destination IP,Services", file = csv)

for k in range(0,rows):
   print (output0[k],",",output1[k],",",output2[k],",",output3[k],",",output4[k],",",output5[k], file = csv)
print ("DONE")

