#!/bin/bash/python

import os
import re

def banner():
    os.system("clear")
    print(r"""
    __        ______  ____   _____ _____            _   _  _____ 
    \ \      / / __ \|  _ \ / ____|  __ \     /\   | \ | |/ ____|
     \ \ /\ / / |  | | |_) | (___ | |__) |   /  \  |  \| | (___  
      \ V  V /| |  | |  _ < \___ \|  _  /   / /\ \ | . ` |\___ \ 
       \_/\_/ | |__| | |_) |____) | | \ \  / ____ \| |\  |____) |
               \____/|____/|_____/|_|  \_\/_/    \_\_| \_|_____/ 

    🔍 WPScan: WordPress zaifliklarini aniqlovchi vosita
    """)

def is_valid_url(url):
    return re.match(r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$", url)

def run_wpscan():
    banner()

    while True:
        print("\n📋 Tanlov menyusi:")
        print("1. WordPress saytni umumiy skan qilish")
        print("2. Foydalanuvchi nomlarini aniqlash (User Enumeration)")
        print("3. Zaifliklarni aniqlash (API token talab qiladi)")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")

        if choice == "1":
            url = input("🌐 WordPress sayt manzilini kiriting (https:// bilan): ").strip()
            if not is_valid_url(url):
                print("❌ Noto‘g‘ri URL! Masalan: https://example.com")
                continue
            command = f"wpscan --url {url}"
            print("\n🔍 Umumiy skaner ishlamoqda...\n")
            os.system(command)

        elif choice == "2":
            url = input("🌐 Sayt manzilini kiriting (https:// bilan): ").strip()
            if not is_valid_url(url):
                print("❌ Noto‘g‘ri URL! Masalan: https://example.com")
                continue
            command = f"wpscan --url {url} --enumerate u"
            print("\n👥 Foydalanuvchilar aniqlanmoqda...\n")
            os.system(command)

        elif choice == "3":
            url = input("🌐 Sayt manzilini kiriting (https:// bilan): ").strip()
            if not is_valid_url(url):
                print("❌ Noto‘g‘ri URL! Masalan: https://example.com")
                continue

            api_token = input("🔑 WPScan API tokeningizni kiriting: ").strip()
            if not api_token:
                print("❌ API token kiritilmadi!")
                continue

            command = f"wpscan --url {url} --api-token {api_token} --enumerate vp,vt,cb,dbe,u,m"
            print("\n⚠ Zaifliklar tahlil qilinmoqda...\n")
            os.system(command)

        elif choice == "0":
            print("🚪 Dasturdan chiqildi.")
            break

        else:
            print("❌ Noto‘g‘ri tanlov!")

        again = input("\n🔁 Shu IP/domen uchun yana foydalanishni xohlaysizmi? (yes/no): ").lower()
        if again != "yes":
            break
        back = input("\n⬅  Boshqa IP/domenni foydalanishni xohlaysizmi? (yes/no): ").lower()
        if back != "yes":
            print("🔚 Dastur tugatildi. Asosiy menyuga qaytilmoqda...\n")
            from main import main
            return main()   
