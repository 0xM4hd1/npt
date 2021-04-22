import socket
import os
import sys

def clean():
	if os.name == 'nt':
		os.system("cls")
		os.system("color 4")
	else:
		os.system("clear")
clean()
try :
	import colorama
except :
	clean()
	print("colorama Library is not installed \n -Install this with command line : pip3 install colorama")
	sys.exit()
colorama.init()
print(colorama.Fore.GREEN + " __")
print(colorama.Fore.GREEN + "|__|___")
print(colorama.Fore.GREEN + "|__|___|__")
print(colorama.Fore.GREEN + "|___|_____|___")
print(colorama.Fore.GREEN + "|_____|___|___|__")
print(colorama.Fore.GREEN + "|_________|___|__|___________")
ip = input(colorama.Fore.GREEN + "|[!] IP Address : ")
first_port = int(input(colorama.Fore.GREEN + "|[!] First Port Number : "))
end_port = int(input(colorama.Fore.GREEN + "|[!] End Port Number :")) + 1
#tcount = int(input("[!] Thread Count : "))
print(" ______________________________________")
print(colorama.Fore.GREEN + "[!] Target : ", socket.gethostbyname(ip))
print(colorama.Fore.GREEN + "[!] Your Computer Name : ", socket.gethostname())
print(colorama.Fore.GREEN + " ______________________________________")
print(colorama.Fore.GREEN + "Scanning...")


def pscan():
    for port in range(first_port, end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(colorama.Fore.GREEN + f"[+] Port {port} : Open!!!")
        else:
            print(colorama.Fore.RED + f"[-] Port {port} : Close :( ")
        s.close()
        if port == 21:
            print("    L[ Service : FTP")
        if port == 22:
            print("    L[ Service : SSH")
        if port == 23:
            print("    L[ Service : Telnet")
        if port == 80:
            print("    L[ Service : HTTP")
        if port == 443:
            print("    L[ Service : HTTPS")
        if port == 445:
            print("    L[ Service : SMB // AD")
        if port == 53:
            print("    L[ Service : DNS")
        if port == 3389:
            print("    L[ Service : RDP")
        if port == 3306:
            print("    L[ Service : MySQL")
        if port == 110:
            print("    L[ Service : POP3")
        if port == 26:
            print("    L[ Service : SMTP")
        if port == 43:
            print("    L[ Service : Whois")
        if port == 115:
            print("    L[ Service : SFTP")
        if port == 69:
            print("    L[ Service : TFTP")
        if port == 67:
            print('    L[ Service : DHCPS')
        if port == 68:
            print('    L[ Service : DHCPC')
        if port == 167:
            print("    L[ Service : Nmap")
        if port == 1900:
            print("    L[ Service : UPNP")
        if port == 123:
            print("    L[ Service : NTP")
        if port == 25:
            print("    L[ Service : SMTP")
        if port == 118:
            print("    L[ Service : SQL")
        if port == 135:
            print("    L[ Service : EPMAP")
        if port == 137:
            print("    L[ Service : NETBIOS Name Service")
        if port == 138:
            print("    L[ Service : NETBIOS DataGram Service")
        if port == 139:
            print("    L[ Service : NETBIOS Session Service")
        if port == 143:
            print("    L[ Service : IMAP")
        if port == 153:
            print("    L[ Service : SGMP")
        if port == 161:
            print("    L[ Service : SNMP")
        if port == 179:
            print("    L[ Service : BGP")
        if port == 8291:
            print("    L[ Service : WinBox")
        if port == 1723:
            print("    L[ Service : PPTP")
        if port == 143:
            print("    L[ Service : VPN Connection")
        if port == 520:
            print("    L[ Service : Rip Protocol ")
        if port == 465:
            print("    L[ Service : Cisco SMP // SMTPS")
        if port == 444:
            print("    L[ Service : SNPP")

pscan()

print(colorama.Fore.BLUE + " ________________________")
print(colorama.Fore.BLUE + "|[♥] Scan Finished...    |")
print(colorama.Fore.BLUE + "|________________________|")
print(colorama.Fore.GREEN + " ______________________")
print(colorama.Fore.GREEN + "|_____________|____|")
print(colorama.Fore.GREEN + "|________|____|")
print(colorama.Fore.GREEN + "|___|____|")
print(colorama.Fore.GREEN + "|___|")
sys.exit()
