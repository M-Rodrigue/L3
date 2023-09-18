############################# CORRECTION ###############################
from scapy.all import *

def monFilte(pkt):
  if DNSQR:
    return True
  else:
    return False

def maFonction(pkt):
  print("Nom : ", pkt(DNSQR).qname)

sniff(iface = "en0", prn = maFonction, filter = "udp dst port 53", lfilter = monFiltre, count = 10)