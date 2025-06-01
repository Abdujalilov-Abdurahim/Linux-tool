#!/bin/bash/python

import os
import re

def banner():
    os.system("clear")
    print(r"""
 ______                 _  _   _            _             
|  ____|               | || | (_)          | |            
| |__  __  _____  ___  | || |_ _  ___ _ __ | |_ ___  _ __ 
|  __| \ \/ / _ \/ _ \ |__   _| |/ _ \ '_ \| __/ _ \| '__|
| |____ >  <  __/  __/    | | | |  __/ | | | || (_) | |   
|______/_/\_\___|\___|    |_| |_|\___|_| |_|\__\___/|_|   

🔎 Enum4Linux - Samba (SMB) tarmoqlarini aniqlovchi vosita
""")

def is_valid_ip(ip):
    return re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip)

def run_enum4linux():
    banner()

    while True:
        target = input("🎯 Maqsadli IP-manzilni kiriting (masalan: 192.168.1.100): ").strip()
        if is_valid_ip(target):
            break
        print("❌ Noto'g'ri IP-manzil! Qaytadan urinib ko‘ring.")

    while True:
        print("\n📋 Tanlov menyusi:")
        print("1. 👥 Foydalanuvchilar va guruhlarni aniqlash")
        print("2. 📁 Ulashilgan papkalarni ko‘rish (SMB shares)")
        print("3. ⚙  RPC xizmatlarini tekshirish")
        print("4. 🧪 To‘liq skanerlash (barcha ma'lumotlarni olish)")
        print("0. 🚪 Chiqish")

        choice = input("\n🔢 Tanlovni kiriting: ").strip()

        if choice == "1":
            command = f"enum4linux -U {target}"
        elif choice == "2":
            command = f"enum4linux -S {target}"
        elif choice == "3":
            command = f"enum4linux -R {target}"
        elif choice == "4":
            command = f"enum4linux -a {target}"
        elif choice == "0":
            print("🚪 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")
            continue

        print("\n🔍 Enum4Linux ishlamoqda...\n")
        os.system(command)

        again = input("\n🔁 Yana foydalanasizmi? (yes/no): ").lower()
        if again != "yes":
            print("🔙 Asosiy menyuga qaytilmoqda...")
            os.system("python3 main.py")
            break
                                       
