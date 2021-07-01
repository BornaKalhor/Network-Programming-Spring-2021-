#       Port Sniffer by Borna Kalhor
#       Ferdowsi University of Mashhad





    ###########################|  IMPORT  |###########################

import socket
import threading
import string
from queue import Queue

    ###########################|  DECLARATION  |###########################

queue = Queue()
open_ports = []

targetAddress = input("Please enter the address of your target host > \n")


    ###########################|  FUNCTIONS  |###########################

def connect(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        answer = str(waitTime).upper()
        if answer != "PASS":
            sock.settimeout(float(waitTime))

        try:
            sock.connect((targetAddress, port))
            return True
        except:
            return False
    except:
        print("Program failed to establish connection")


def insert_ports_in_Q(mode):
    try:
        if mode =="1":
            for port in range(1, 65536):
                queue.put(port)

        elif mode =="2":
            ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 137, 138, 139, 143, 161, 443, 445]
            for p in ports: queue.put(p)

        elif mode =="3":
            service = input("Enter your desired service... \n")
            service = service.upper()

            if service =="HTTP":
                queue.put(80)
            elif service =="TLS":
                queue.put(443)
            elif service =="SMTP":
                queue.put(25)
            elif service =="FTP":
                queue.put(20)
                queue.put(21)
            elif service =="TELNET":
                queue.put(23)
            elif service =="SSH":
                queue.put(22)

        elif mode =="4":
            ports = input("Enter your custom ports range (seperated by comma) ... \n")
            ports = ports.split(',', 3)
            print("Scanning between port range", ports)
            ports = list(map(int, ports))
            for eachPort in range(ports[0], ports[1]):
                queue.put(eachPort)

    except:
        print("Failed to insert ports into the queue.")




def actualThing():
    try:
        while not queue.empty():
            port = queue.get()
            if connect(port):
                print("port {} is open".format(port))
                open_ports.append(port)
    except:
        print("wow...")

    ###############################



def runSniffer(xthreads):
    try:
       # get_ports(mode)
        thread_list = []

        for eachThread in range(xthreads): #thread numbers
            thread = threading.Thread(target=actualThing)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()


        if not open_ports:
            print("Couldn't find anything :(")
        else:
            print("Process finished, Found these open ports: ", open_ports)
    except:
        print("Failed on running the program.")



    ###########################|  MAIN  |###########################
    ################################################################

print("avaliable modes are:")
print("1. Scan all ports of the host.")
print("2. Only scan reserved & well known ports.")
print("3. [type your desired service]")
print("4. Enter custom port range...")

themode = input("Choose the mode \n")
thethreads = int(input("Choose the number of threads \n"))
waitTime = input("Specify waiting time on each port or just type 'PASS' to ignore. \n")

insert_ports_in_Q(str(themode))
runSniffer(thethreads)