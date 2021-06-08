from scapy.all import *

f=rdpcap('1.pcap')
b=''

for i in f:
	if IP not in i:
		continue
	if i.haslayer(DNS):
		if i[IP].src == '192.168.42.129':
			b+=str(i)[224:]

f=open('1.png','w')
f.write(b)
f.close()



