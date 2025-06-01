#/bin/bash/python

import os
import re

os.system("clear")
def banner():
    print(""" 
 ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║  ███╗██║   ██║██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
██║   ██║██║   ██║██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                    
    """)

def run_gobuster():
    os.system("clear")
    banner()
    print("Gobuster bilan ishlash")

    # Maqsadli URL manzilni tekshirish
    while True:
        target = input("\nMaqsadli URL manzilni kiriting (masalan: http://example.com): ")
        if target.startswith("http://") or target.startswith("https://"):
            break
        print("❌ Noto‘g‘ri URL manzil! Qaytadan urinib ko‘ring.")

    while True:
        print("\nTahlil turini tanlang:")
        print("1. Yashirin kataloglarni topish")
        print("2. Subdomainlarni aniqlash")
        print("3. Fayllarni bruteforce qilish")
        print("4. Virtual hostlarni tekshirish")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")

        # Wordlist faylini so'rash
        wordlist = input("\nWordlist fayl yo'lini kiriting (masalan: /usr/share/wordlists/dirb/common.txt): ")
        if not os.path.exists(wordlist):
            print("❌ Wordlist topilmadi! Qaytadan urinib ko‘ring.")
            return

        if choice == "1":
            command = f"gobuster dir -u {target} -w {wordlist}"
        elif choice == "2":
            domain = target.replace("http://", "").replace("https://", "").replace("/", "")
            command = f"gobuster dns -d {domain} -w {wordlist}"
        elif choice == "3":
            command = f"gobuster dir -u {target} -w {wordlist} -x php,html,txt"
        elif choice == "4":
            command = f"gobuster vhost -u {target} -w {wordlist}"
        elif choice == "0":
            print("Dasturdan chiqildi.")
            return
        else:
            print("❌ Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")
            return

        print("\nGobuster ishga tushirilmoqda...\n")
        os.system(command)

        again = input("\n🔁 Shu IP/domen uchun yana foydalanishni xohlaysizmi? (yes/no): ").lower()
        if again != "yes":
            break
        back = input("\n⬅️  Boshqa IP/domenni foydalanishni xohlaysizmi? (yes/no): ").lower()
        if back != "yes":
            print("🔚 Dastur tugatildi. Asosiy menyuga qaytilmoqda...\n")
            from main import main
            return main()

