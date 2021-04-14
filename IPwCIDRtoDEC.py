##Use Example: python3 IPwCIDRtoDEC.py 192.169.0.0/28
##output.txt will list all IP addresses in cidr as integers 

#Imports
import sys
import ipaddress

#Argument grab
cidr = sys.argv[1]

#Create list of IP addresses from CIDR
ip = list(ipaddress.ip_network(cidr).hosts())

i = 0

#Get length of list 
length = len(ip)

##Debug tool
#print("list length is", length)

#Create/open output.txt
outfile = open('output.txt', 'w')

#Iterate through list making each IP an integer and output to file
while i < length :
    print(int(ipaddress.IPv4Address(ip[i])), file = outfile)
    i += 1

#Close/rewrite output.txt
outfile.close()
