#/bin/bash/python

import pyfiglet
from termcolor import colored
import shutil
import os
from tools.nmap_tool import run_nmap
from tools.sqlmap_tool import run_sqlmap
from tools.nikto_tool import run_nikto
from tools.hydra_tool import run_hydra

os.system("clear")
columns, rows = shutil.get_terminal_size()
banner = pyfiglet.figlet_format("Xush kelisiz! Bu dastur sizga qanday yordam bera oladi  ? !")
banner_lines = banner.split("\n") 

for line in banner_lines:
	print (line.center(columns))

Main = "Menyu:"
option_01 = colored("[+] 1. Nmap	", 'light_blue', attrs=['reverse', 'bold'])
option_02 = colored("[+] 2. Sqlmap	", 'white', attrs=['reverse', 'bold'])
option_03 = colored("[+] 3. Nikto	", 'yellow', attrs=['reverse', 'bold'])
option_04 = colored("[+] 4. Hydra	", 'green', attrs=['reverse', 'bold'])
option_05 = colored("[+] 5. Dnsenum	", 'magenta', attrs=['reverse', 'bold'])
option_06 = colored("[+] 6. John	", 'red', attrs=['reverse', 'bold'])
option_07 = colored("[+] 7. Wpscan	", 'cyan', attrs=['reverse', 'bold'])
option_08 = colored("[+] 8. Netcat	", 'light_green', attrs=['reverse', 'bold'])
option_09 = colored("[+] 9. Gobuster	", 'light_yellow', attrs=['reverse', 'bold'])
option_10 = colored("[+] 10. Enum4linux	", 'light_cyan', attrs=['reverse', 'bold'])
Chiqish =  colored("[+] 0. Chiqish", 'red', 'on_white', attrs=['reverse', 'bold', 'blink'])


menu1 = f"""
   
		 └─┬─────────┤     {Main}      ├─────────────────┬───────────────────┤
		   │         └─────────────────┘        	 │
		   ├─ {option_01	                        }├─ {option_06                   }
		   ├─ {option_02	                        }├─ {option_07                   }
		   ├─ {option_03	                        }├─ {option_08                   }
		   ├─ {option_04	                        }├─ {option_09                   }
		   ├─ {option_05	                        }├─ {option_10                   }

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
		elif choice == "0":
			print("Dasturdan chiqildi. Xayr!")
			break
		else:
			print("Noto‘g‘ri tanlov!")

if __name__ == "__main__":
	main()

