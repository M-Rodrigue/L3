############################# CORRECTION ###############################
from scapy.all import *

rep = sr1(IP(dst = "8.8.8.8")/UDP()/DNS(rd = 1, qd = DNSQR(qname="acissi.net")))
print (rep[DNSRR].rdata)