#/bin/bash/python

import os
import re

def banner():
    print("\n============= Enum4Linux Tool =============")

def run_enum4linux():
    banner()
    print("Enum4Linux bilan ishlash")

    # IP-manzilni tekshirish
    while True:
        target = input("\nMaqsadli IP-manzilni kiriting (masalan: 192.168.1.100): ")
        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if re.match(ip_pattern, target):
            break
        print("❌ Noto'g'ri IP-manzil formati! Qaytadan urinib ko'ring.")

    while True:
        print("\nTahlil turini tanlang:")
        print("1. Foydalanuvchilar va guruhlarni chiqarish")
        print("2. Ulashilgan papkalar (SMB shares) haqida ma'lumot olish")
        print("3. RPC xizmatlarini tekshirish")
        print("4. To'liq skanerlash (barcha ma'lumotlarni olish)")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")

        if choice == "1":
            command = f"enum4linux -U {target}"
        elif choice == "2":
            command = f"enum4linux -S {target}"
        elif choice == "3":
            command = f"enum4linux -R {target}"
        elif choice == "4":
            command = f"enum4linux -a {target}"
        elif choice == "0":
            print("Dasturdan chiqildi.")
            return
        else:
            print("❌ Noto'g'ri tanlov! Qaytadan urinib ko‘ring.")
            return

        print("\nEnum4Linux ishga tushirilmoqda...\n")
        os.system(command)

        a = input("Yana foydalanasizmi?: yes/no").lower()
        if a != "yes":
            break

# Test qilish
if __name__ == "__main__":
    run_enum4linux()
