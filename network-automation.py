import os
import time
import sys

def clean():
    if os.name == 'nt':
        os.system("cls")
        os.system("color b")
    else :
        os.system("clear")
try :
    import paramiko
    import colorama
except:
    clean()
    print("-----------------------------------------------")
    print("paramiko and colorama libraries Not Installed!! \n [x] Please Install These with : \n -pip3 install colorama \n -pip3 install paramiko ")
    print("-----------------------------------------------")
    sys.exit()
    colorama.init()
try :    
    clean()
    print("-----------------------------------------------")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target = input(colorama.Fore.GREEN+"--[!] IP Address :  ")
    user = input(colorama.Fore.GREEN+"--[!] Username : ")
    passwd = input(colorama.Fore.GREEN+"--[!] Password : ")
    client.connect(target , username = user , password = passwd)
    while True :
        cmd = input(colorama.Fore.CYAN+"Shell>>> ")
        stdin , stdout , stderr = client.exec_command(cmd)
        for line in stdout:
            print(line.strip('\n'))

    client.close()
except KeyboardInterrupt:
    clean()
    sys.exit()