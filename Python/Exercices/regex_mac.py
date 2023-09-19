############################# CORRECTION ###############################
import re

f=open("texte_mac.txt",'r')
data=f.read()
f.close()
regex=re.compile(r'[0-9a-f]{2}(?::[0-9a-f]{2}){5}')#(r'(?:[0-9a-fA-F]:?){12}')
l=[]
l=regex.findall(data)
print(l)