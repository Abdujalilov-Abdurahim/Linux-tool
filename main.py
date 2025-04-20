#/bin/bash/python

import pyfiglet
from termcolor import colored
import shutil
import os
from tools.nmap_tool import run_nmap
from tools.sqlmap_tool import run_sqlmap
from tools.nikto_tool import run_nikto
from tools.hydra_tool import run_hydra
from tools.gobuster_tool import run_gobuster

os.system("clear")
columns, rows = shutil.get_terminal_size()
banner = """
██████╗ ███████╗██████╗     ████████╗███████╗ █████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝█████╗  ██║  ██║       ██║   █████╗  ███████║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     
██╔══██╗██╔══╝  ██║  ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     
██║  ██║███████╗██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                       
                                                                                                       
"""
banner_lines = banner.split("\n")

for line in banner_lines:
	ban = line.center(columns)
	print(colored(f"{ban}", 'red', attrs=["bold"]))


Main = colored("🛡️  Offensive Security Toolkit  🧠", "red", attrs=["bold"])
option_01 = colored("[+] 1. Tizim portlarini scanner qilish	", 'light_blue', attrs=[ 'bold'])
option_02 = colored("[+] 2. Ma'lumotlar bazasidagi zaifliklarni aniqlash	", 'white', attrs=[ 'bold'])
option_03 = colored("[+] 3. Veb-serverni zaifliklarga tekshirish	", 'yellow', attrs=['bold'])
option_04 = colored("[+] 4. Login parollarni bruteforce qilish	", 'green', attrs=['bold'])
option_05 = colored("[+] 5. DNS ma'lumotlarini tahlil qilish	", 'magenta', attrs=['bold'])
option_06 = colored("[+] 6. Hash parollarni ochish	", 'red', attrs=[ 'bold'])
option_07 = colored("[+] 7. WordPress saytini tahlil qilish	", 'cyan', attrs=['bold'])
option_08 = colored("[+] 8. Port orqali aloqa va monitoring qilish ", 'light_green', attrs=['bold'])
option_09 = colored("[+] 9. Veb-serverdagi yashirin papkalarni aniqlash (Active Directory)	", 'light_yellow', attrs=['bold'])
option_10 = colored("[+] 10. Tarmoqdagi Windows qurilmalarini tahlil qilish	", 'light_cyan', attrs=['bold'])
Chiqish =  colored("[+] 0. Chiqish", 'red', 'on_white', attrs=['bold', 'blink'])


menu1 = f"""
   
		 └─┬─────────┤{Main}├
		   │         └─────────────────────────────────┘        	 
		   ├─ {option_01}
		   ├─ {option_02}
		   ├─ {option_03}
		   ├─ {option_04}
		   ├─ {option_05}
		   ├─ {option_06}
		   ├─ {option_07}
		   ├─ {option_08}
		   ├─ {option_09}
		   ├─ {option_10}
													{Chiqish}
"""



def main():
	print (menu1)
	while True:
		choice = input("\nTanlovni kiriting: ")
		if choice == "1":
			run_nmap()
		elif choice == "2":
			run_sqlmap()
		elif choice == "3":
			run_nikto()
		elif choice == "4":
			run_hydra()
		elif choice == "5":
			run_gobuster()
		elif choice == "0":
			print("Dasturdan chiqildi. Xayr!")
			break
		else:
			print("Noto‘g‘ri tanlov!")

if __name__ == "__main__":
	main()

