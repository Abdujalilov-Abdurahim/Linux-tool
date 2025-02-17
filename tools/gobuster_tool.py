#/bin/bash/python

import os
import re

def banner():
    print("\n============= Gobuster Tool =============")

def run_gobuster():
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

        a = input("Yana foydalanasizmi?: yes/no").lower()
        if a != "yes":
            break

# Test qilish
if __name__ == "__main__":
    run_gobuster()
