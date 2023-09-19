############################# CORRECTION ###############################
from scapy.all import *

rep = sr1(IP(dst='10.100.1.135') / TCP(dport = [80], flags = 'S'), timeout = 1)
if rep != None:
  rep.show()