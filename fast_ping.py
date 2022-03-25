
import asyncio
import aioping
import logging
import os
from os.path import exists
import socket
from numpy import index_exp
import pandas as pd
hostlist = ''
file = open(hostlist).read().splitlines()
iplist = []
index=1
# path = os.getcwd()
# os.mkdir("Archive")
# if (exists(file)): #Checks if excel exists. If it does, it sends it to an Archive folder.
#     file.remove()
for host in file:
    
    try:
        ipaddr = socket.gethostbyname(host)
        iplist.append(ipaddr)
        print(f"Working on {index} of {len(file)} - {ipaddr}")
        index += 1
    except Exception:
        iplist.append("No resolution")
        print(f"Working on {index} of {len(file)}")
        index += 1
df = pd.DataFrame()
df["URL"] = file
df["IP_Address"] = iplist
df.to_csv('C:\\Users\\jujohnson\\OneDrive - InComm Payments\\Desktop\\Scripts\\Ping\\PingedHosts.csv', index=False)
