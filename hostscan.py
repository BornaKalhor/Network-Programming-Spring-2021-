import socket
import struct as st
from uuid import getnode
import re



start = "11.12.13.14"
finish = "22.22.22.22"

c = start.split('.')
d = '.'.join(c[0:3])

print(d)

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
mymac = re.findall('..', '%012x' % getnode())
myname = socket.gethostname()
myip = socket.gethostbyname(myname)
print(myip)
print(mymac)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("eth0", 0))

''''
frame = [
    st.pack('!H', 0x0001), # HRD
    st.pack('!H', 0x0800), # PRO
    st.pack('!B', 0x06), # HLN
    st.pack('!B', 0x04), # PLN 
    st.pack('!H', 0x0001), # OP
    st.pack('!B', mymac), # SHA
    st.pack('!B', myip), # SPA
    st.pack('!B', (0x00,)*6), # THA
    st.pack('!B', destip), # TPA
]
print(frame)

while True:
    for i in range(c, 256):
        for j in range(d, 256):



recvsock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
recvsock.bind
'''''