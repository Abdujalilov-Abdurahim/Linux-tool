#!/bin/bash/python

from termcolor import colored
import re
import os


def banner(): 
        os.system("clear")


        banner = colored(r"""
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              }@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       }@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      }0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  }@@@@@@@@@@@@@| 00v  j00000}                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000}                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
        """, 'red')


        print (banner)

def validate_target(target):
        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        domain_pattern = r"^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return re.match(ip_pattern, target) or re.match(domain_pattern, target)

def show_menu():
        print("\n⚙  Qo'shimcha parametrlarni tanlang:")
        print("1. Portlarni skanerlash")
        print("2. To'liq skanerlash")
        print("3. Xizmatlar va versiyalarni aniqlash")
        print("4. Maqsadli tarmoqni tahlil qilish (ping bypass)")
        print("5. Xavfsizlik zaifliklarini aniqlash (NSE skriptlari)")
        print("6. Tarmoq diapazonini skan qilish")
        print("7. Yashirin skan (Stealth scan)")

def run_nmap():
        banner()
        print("🛰  Nmap bilan ishlash")

        while True:
                target = input("🎯 Maqsadli IP yoki domenni kiriting: ")
                if validate_target(target):
                        break
        print("❌ Noto‘g‘ri IP yoki domen formati. Qayta urinib ko‘ring.")

        while True:
                show_menu()
                choice = input("\n🧭 Tanlovni kiriting: ")

                if choice == "1":
                        ports = input("📍 Portlarni kiriting (masalan: 80,443): ")
                        command = f"nmap -p {ports} {target} --script=default"
                elif choice == "2":
                        command = f"nmap -A {target}"
                elif choice == "3":
                        if os.geteuid() != 0:
                                print("❌ Xizmatlar va versiyalarni aniqlash uchun root huquqlari talab qilinadi.")
                                return
                        command = f"nmap -sV -O {target} --script=default"
                elif choice == "4":
                        command = f"nmap -Pn {target}"
                elif choice == "5":
                        command = f"nmap --script vuln {target}"
                elif choice == "6":
                        range_target = input("🌐 Tarmoq diapazonini kiriting (masalan: 192.168.1.0/24): ")
                        command = f"nmap {range_target}"
                elif choice == "7":
                        command = f"nmap -sS {target}"
                else:
                        print("❌ Noto'g'ri tanlov. Qayta urinib ko'ring.")
                        continue

                print(f"\n🚀 Buyruq bajarilmoqda:\n{command}\n")
                os.system(command)

                again = input("\n🔁 Shu IP/domen uchun yana skanerlashni xohlaysizmi? (yes/no): ").lower()
                if again != "yes":
                        break
        back = input("\n⬅  Boshqa IP/domenni skanerlashni xohlaysizmi? (yes/no): ").lower()
        if back != "yes":
                print("🔚 Nmap skanerlash tugatildi. Asosiy menyuga qaytilmoqda...\n")
                from main import main
                return main()                                                                                                                                                                                                                
