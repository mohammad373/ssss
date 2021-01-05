# ssss

import os
import requests
import socket
import time
import sys
from colorama import Fore

def __target__():
    os.system("clear")
    time.sleep(1)
    print(Fore.RED + "Hello , I`m Bobot ;))")
    time.sleep(1)
    target = input(Fore.BLUE + "[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + "Pleass Enter Domain ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "[-] ~ Error : Your Domain Is None ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    if not "http://" in target or not "https://" in target:
        target = "http://" + target
    s1 = requests.get(target)
    if s1.status_code == 200:
        print(Forre.GREEN + "[+] ~ Your Domain Is Found ;))")
    else:
            try:
              time.sleep(1)
              print(Fore.RED + "[-] ~ Error : Your Domain Is Not Found ;(")
              time.sleep(1)
              sys.exit()
            except:
                sys.exit()
    s2 = requests.get( "https://api.hackertarget.com/whatweb/?q="  +  target).text
    print(Fore.GREEN + s2)
    time.sleep(1)
    sys.exit()
__target__()
