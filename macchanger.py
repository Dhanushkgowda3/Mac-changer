#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():	 
     parser = optparse.OptionParser()
     parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC adress")
     parser.add_option("-m", "--mac", dest="new_mac", help="Interface to change MAC adress")
     (options, arguments) = parser.parse_args()
     if not options.interface:
        parser.error(" [-]Please specify an interface, use --help for more info")
     elif not options.new_mac:
        parser.error(" [-]Please specify an mac, use --help for more info")
     return options
     
     

def mac_change(interface, new_mac):
    print("[+] Changing MAC adress from " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", interface])
    mac_address_search_result= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
 
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not read a MAC address.")

#icon and author


print("""      
.88b  d88.  .d8b.   .o88b.    .o88b. db   db  .d8b.  d8b   db  d888b  d88888b d8888b. 
88'YbdP`88 d8' `8b d8P  Y8   d8P  Y8 88   88 d8' `8b 888o  88 88' Y8b 88'     88  `8D 
88  88  88 88ooo88 8P        8P      88ooo88 88ooo88 88V8o 88 88      88ooooo 88oobY' 
88  88  88 88~~~88 8b        8b      88~~~88 88~~~88 88 V8o88 88  ooo 88~~~~~ 88`8b   
88  88  88 88   88 Y8b  d8   Y8b  d8 88   88 88   88 88  V888 88. ~8~ 88.     88 `88. 
YP  YP  YP YP   YP  `Y88P'    `Y88P' YP   YP YP   YP VP   V8P  Y888P  Y88888P 88   YD  v1.1   
""")
print("--------------{+} Coded By h4ck3rdhanush{+}--------------")
print("--------------{+} Github & IG :h4ck3rdhanush{+}--------------")
   

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Curernt MAC = " + str(current_mac))

mac_change(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac :
    print("[+]MAC address was successfully changed to" , current_mac)
else:
    print("[-]MAC address did not changed.")

