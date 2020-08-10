#!/bin/python3

#a bootleg port scanner.

#for command line arguments, plus other cool stuff
import sys
#for the connections
import socket
#datetime for some cool pretty stuff!
from datetime import datetime

#Defining the target.
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
        print("Invalid Arguments.")
        print("Syntax: python3 scanner.py <ip>")
        sys.exit() #THIS IS IMPORTANT SO IT DOESNT KEEP RUNNING
        
#pretty banner :)
print("-" * 50)
print("""\
dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHb
HHP%%#%%%%%%%%%%%%%%%%#%%%%%%%#%%VHH
HH%%%%%%%%%%#%v~~~~~~\%%%#%%%%%%%%HH
HH%%%%%#%%%%v'        ~~~~\%%%%%#%HH
HH%%#%%%%%%v'dHHb      a%%%#%%%%%%HH
HH%%%%%#%%v'dHHHA     :%%%%%%#%%%%HH
HH%%%#%%%v' VHHHHaadHHb:%#%%%%%%%%HH
HH%%%%%#v'   `VHHHHHHHHb:%%%%%#%%%HH
HH%#%%%v'      `VHHHHHHH:%%%#%%#%%HH
HH%%%%%'        dHHHHHHH:%%#%%%%%%HH
HH%%#%%        dHHHHHHHH:%%%%%%#%%HH
HH%%%%%       dHHHHHHHHH:%%#%%%%%%HH
HH#%%%%       VHHHHHHHHH:%%%%%#%%%HH
HH%%%%#   b    HHHHHHHHV:%%%#%%%%#HH
HH%%%%%   Hb   HHHHHHHV'%%%%%%%%%%HH
HH%%#%%   HH  dHHHHHHV'%%%#%%%%%%%HH
HH%#%%%   VHbdHHHHHHV'#%%%%%%%%#%%HH
HHb%%#%    VHHHHHHHV'%%%%%#%%#%%%%HH
HHHHHHHb    VHHHHHHH:%odHHHHHHbo%dHH
HHHHHHHHboodboooooodHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
VHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHV""")
print("The Peng Scanner!")
print("Scanning target "+ target)
print("Time began scan:" + str(datetime.now()))
print("-" * 50)

try:
        for port in range(50,85):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1) #is a float could also be .5 seconds
                result = s.connect_ex((target,port)) #returns the connection error, no error = 0
                print("Scanning port {}".format(port))
                if result == 0:
                    print("[!!!] Port {} is open [!!!]".format(port))
                print("Finished Checking.")
                s.close()
                

except KeyboardInterrupt:
    print("\nExiting Scan. Bye bye.")
    sys.exit

except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

