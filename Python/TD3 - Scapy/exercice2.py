############################# CORRECTION ###############################
from scapy.all import *

def monFiltre(pkt):
  if pkt.hasLayer(Raw):
    return True
  else:
    return False

def maFonction(pkt):
  if pkt[Raw].load[:4] == 'POST' or pkt[Raw].load[:3] == 'GET':
    print("Nom : ", pkt[Raw].load)

sniff(iface = "en0", prn = maFonction, filter = "tcp dst port 80", lfilter = monFilte, count = 10)