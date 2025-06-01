#!/bin/bash/python

import os

def banner():
    os.system("clear")
    print(r"""
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
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O  """)

def run_john():
    banner()
    print("John the Ripper bilan ishlash")

    print("\n1. Hash faylga asoslangan parolni crack qilish")
    print("2. Crack qilingan parollarni ko‘rish")
    print("0. Chiqish")

    choice = input("\nTanlovni kiriting: ")

    if choice == "1":
        while True:
            hash_file = input("Shifrlangan faylni kiriting: ")
            if os.path.exists(hash_file):
                break
            print("❌ Fayl topilmadi! Iltimos, to'g'ri fayl yo'lini kiriting.")

        wordlist = input("Wordlist (masalan, /usr/share/wordlists/rockyou.txt): ")

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

    back = input("\n⬅️ Dasturdan yana foydalanasizmi? (yes/no): ").lower()
    if back == "yes":
        run_john()
    else:
        print("\n🔚 John Ripper yakunlandi. Asosiy menyuga qaytmoqda...\n")
        try:
            from main import main
            return main()
        except ImportError:
            print("⚠️ main.py topilmadi.")

