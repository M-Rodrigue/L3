############################# CORRECTION ###############################
from scapy.all import *

def filtre(pkt):
  if pkt[ARP].op == 0x2:
    return True
  else:
    return False

def arp_display(pkt):
  print(pkt[ARP].psrc + " => " + pkt[ARP].hwsrc)

sniff(iface = "en0", prn = arp_display, filter = "arp", lfilter = filtre, count = 100)