#!/usr/bin/env python3

import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# get nearby ap status on osx, change cmd according to your os
os.system('/System/Library/PrivateFrameworks/'
'Apple80211.framework/Versions/Current/Resources/airport -s '
'> aplist.raw')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('aplist.raw', 'r') as f:
        aplist_raw = f.read()
        s.sendall(aplist_raw.encode())
        data = s.recv(1024)

print(data.decode())
