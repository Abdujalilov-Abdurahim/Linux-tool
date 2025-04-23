#!/bin/bash/python

import os

os.system("clear")

def  banner():
    banner = r"""
                                         ^M@@@@@@@@@v                                    
                                      v@@@@@@@@@@@@@@@@@                                 
                                    _@@@@@@@}    ;a@@@@@@@                               
                                   M@@@@@            @@@@@@                              
                                  ;@@@@@              O@@@@@                             
                                  @@@@@v               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;                                                 
                                  @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O  """


    return banner

def john_tool():
    banner()

    print("John the Ripper bilan ishlash")

    print("\n1. Hash faylga asoslangan parolni crack qilish")
    print("2. Crack qilingan parollarni ko‘rish")
    print("0. Chiqish")

    choice = input("\nTanlovni kiriting: ")

    if choice == "1":
        hash_file = input("Hashlar saqlangan faylni yo‘lini kiriting: ")
        wordlist = input("Wordlist (masalan, /usr/share/wordlists/rockyou.txt): ")

        if not os.path.exists(hash_file):
            print("❌ Hash fayl topilmadi!")
            return
        if not os.path.exists(wordlist):
            print("❌ Wordlist fayli topilmadi!")
            return

        command = f"john --wordlist={wordlist} {hash_file}"
        print("\n🔐 Crack qilish boshlandi...\n")
        os.system(command)

    elif choice == "2":
        hash_file = input("Oldingi ishlatilgan hash fayl yo‘lini kiriting: ")
        if not os.path.exists(hash_file):
            print("❌ Fayl topilmadi!")
            return

        command = f"john --show {hash_file}"
        print("\n📜 Crack qilingan parollar:\n")
        os.system(command)

    elif choice == "0":
        print("Dasturdan chiqildi.")
        return

    else:
        print("❌ Noto‘g‘ri tanlov!")

