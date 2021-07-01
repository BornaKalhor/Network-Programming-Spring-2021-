# Borna Kalhor
# Ferdowsi University of Mashhad

import socket, struct, time


def tracert(target):

    ttl = 1
    timeout = 5
    max_hops = 30
    port = 33500
    node_addr = None


    while ttl < max_hops and node_addr is not socket.gethostbyname(target):

        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, 1)
        # snd_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.settimeout(timeout)

        data = 192 * 'Q'
        header = struct.pack('bbHHh', 8, 0, socket.htons(24449), 25, 1)
        packet = header + data.encode('ascii')

        sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl);

        

        finished = False
        tries = 3
        tries_left = tries

        while not finished and tries_left != 0:
            try:
                sock.sendto(packet, (target, port)) ; time_sent = time.time()
                node_addr = sock.recvfrom(1024)[1]  ; time_rcvd = time.time()
                ping = int((time_rcvd - time_sent) * 1000)
                print("Hop: {}  Node Address: {}     ping: {}    Try: {}".format(ttl, node_addr[0], ping, tries-tries_left+1))
                # finished = True
                tries_left -= 1

            except Exception:
               print("Hop: {}  Node Address: {}     ping: {}    Try: {}".format(ttl, "* * * *", " - ", tries-tries_left+1))
               tries_left -= 1
               

        sock.close()
        ttl += 1

    print("Tracing finished.", ttl, target)

if __name__ == '__main__':
    tracert("bing.com")