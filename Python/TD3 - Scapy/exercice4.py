############################# CORRECTION ###############################
from scapy.all import *
import time

t = time.time()
ipToTest = "10.0.100.101"

for i in range(0, 5):
  rep, nom_rep = sr(IP(dst = ipToTest) / ICMP(), timeout = 0.3)
  for r in rep:
    if r[1].type == 0
    duration = time.time() - t
    duration = str(duration).split(".")
    duration = duration[0] + "." + duration[1][:3]
    print("[UP] [%s] in %s ms" % (ipToTest, duration))