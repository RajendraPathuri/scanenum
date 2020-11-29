#!/usr/bin/env

from os import *
from getpass imporrt getpass

def nmap():
	system(pass1 + 'nmap -T4 -p- -A ' + ipaddr)  #perform nmap scan
	#system.exit(0)


def nikto():
	system(pass1 + 'nikto -h http://' + ipaddr)  #perform nikto scan
	#system.exit(0)
#prg for opening terminals individually

ipaddr = raw_input("Enter the target IP Address: ") #get ip from user

sudopassw = getpass("Enter root Password: ") #pass as argument for nmap,nikto,

pass1 = ('echo '+str(sudopassw)+' | sudo -S echo && sudo -s ') #passes this password directly to sudo with out involvement

nmap()
nikto()
