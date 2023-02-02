import socket 
import sys
from queue import Queue 
import threading

print(r""" ███╗░░░███╗██╗██████╗░░█████╗░██╗░░██╗██╗░░░░░███████╗░██████╗░█████╗░
████╗░████║██║██╔══██╗██╔══██╗██║░██╔╝██║░░░░░██╔════╝██╔════╝██╔══██╗
██╔████╔██║██║██████╔╝███████║█████═╝░██║░░░░░█████╗░░╚█████╗░███████║
██║╚██╔╝██║██║██╔══██╗██╔══██║██╔═██╗░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║
██║░╚═╝░██║██║██║░░██║██║░░██║██║░╚██╗███████╗███████╗██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝

░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║""")

print("\n****************************************************************")
print("\n* https://github.com/MiraklesA                                 *")
print("\n****************************************************************")

q = Queue()
open_ports = []
print_lock = threading.Lock()
socket.timeout(5)

#Input 
target_ip = input("\nEnter an Ip Address to scan for open Ports : ")
try:
    targetdetails = socket.gethostbyname(target_ip)
except socket.gaierror:
    print("Invalid target IP/hostname")
    sys.exit()


print ("_"* 60)
print ("\nScanning, this might take some time")
print ("_"* 60)

def main(port):
    try:      
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        result = sock.connect((targetdetails,port)) 
              

        return True
    except:
        return False
            
def worker():
    while not q.empty():
        port = q.get()
        if main(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))    

def get_ports():
    print("\n Port Detection In Between 1 - 1024 [1] \n Port Detection In Between 1, 65535 [2] \n Popular Port Detection [3] \n Custom Port Detection [4]")
    mode = int(input("\n Select An Option: "))
    if mode == 1:
        for port in range(1, 1024):
            q.put(port)
    elif mode == 2:
        for port in range(1, 65535):
            q.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            q.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            q.put(port)
    else: 
        print("Unrecognised input please try again")            

def main_thread(threads):


    thread_list = []
    get_ports()

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)


main_thread(300)



