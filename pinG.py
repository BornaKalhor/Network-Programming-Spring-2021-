import array
import socket
import time
import struct
import select
import random
import asyncore
import select
import sys
import threading
import signal


NUMBER_OF_PACKETS = 1
TIMEOUT = 0.5

ICMP_ECHO_REQUEST = 8
ICMP_CODE = 1
    

table = []
hostZZ = []
#def sighand(sig, frame):



def create_packet(id):

    data = 192 * 'Q'
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0,
                         socket.htons(24449), id, 1) # I have already calculated the checksum for this packet and the result was 2449
    return header + data.encode('ascii')


def makeList():
    hosts = input("ENTER DESIRED HOSTS FOR PINGING... \n")
    hosts = hosts.split(' ')
    for eachHost in hosts:
        print("The host {} added for pinging.".format(eachHost))
        hostZZ.append(eachHost)
    return hosts

def pinger():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
    packet_id = 25 # random number

    packet = create_packet(packet_id)

    hostList = makeList()

    seg = 0

    try:
        for number in range(10):
            for eachHost in hostList:
                the_host = eachHost

                sock.sendto(packet, (the_host, 1))
                time_sent = time.time()

                sock.settimeout(TIMEOUT)
                try:
                    received, addr = sock.recvfrom(1024)
                    time_received = time.time()

                    RTT = int((time_received - time_sent)*1000)
                    print("\033[1;32;40m REPLY FROM: {} <{}> IN \033[1;31;40m {}ms \033[1;35;40m SEG={}".format(the_host, socket.gethostbyname(the_host), RTT, seg))
                    record = (the_host, RTT)
                    table.append(record)

                except socket.timeout:
                    print("reply from {} was timed out".format(the_host))
            
            print("     -------------------")
            seg += 1

        showstats()
    except Exception:
        showstats()
        sys.exit(0)
                

def threadRun(number_of_threads=5):
    try:
        threadlist = []
        for each in range(number_of_threads):
            thread = threading.Thread(target=pinger)
            threadlist.append(thread)

        for thread in threadlist:
            thread.start()

        for thread in threadlist:
            thread.join()
    except socket.timeout:
        print("reply from {} was timed out".format(the_host))        
    except KeyboardInterrupt:
        showstats()

    except Exception:
        showstats()


def showstats():
    print("     ======= STATS =======")
    for eachhost in hostZZ:
        try:
            list1 = []
            for record in table:
                if str(record[0])==str(eachhost):
                    list1.append(record[1])
            list1.sort()
            print("host:{} > MIN:{} MAX:{}".format(eachhost, list1[0], list1[-1]))
        except:
            continue

# run threadRun() or pinger()
pinger()



