#/bin/bash/python

import os

os.system("clear")

def banner():
    print("\n=========== WPScan Tool ===========")

def run_wpscan():
    banner()
    print("WPScan bilan ishlash (WordPress zaifliklarni aniqlash vositasi)")

    print("\n1. WordPress saytni umumiy skan qilish")
    print("2. Foydalanuvchi nomlarini aniqlash (User Enumeration)")
    print("3. Zaifliklar (vulnerabilities) ni aniqlash")
    print("0. Chiqish")

    choice = input("\nTanlovni kiriting: ")

    if choice == "1":
        url = input("WordPress sayt manzilini kiriting (https:// bilan): ")
        command = f"wpscan --url {url}"
        print("\n🔍 Skaner ishlamoqda...\n")
        os.system(command)

    elif choice == "2":
        url = input("Sayt manzilini kiriting: ")
        command = f"wpscan --url {url} --enumerate u"
        print("\n👥 Foydalanuvchilar aniqlanmoqda...\n")
        os.system(command)

    elif choice == "3":
        url = input("Sayt manzilini kiriting: ")
        api_token = input("WPScan API tokeningizni kiriting: ")
        command = f"wpscan --url {url} --api-token {api_token} --enumerate vp,vt,cb,dbe,u,m"
        print("\n⚠️ Zaifliklar tahlil qilinmoqda...\n")
        os.system(command)

    elif choice == "0":
        print("Dasturdan chiqildi.")
        return

    else:
        print("❌ Noto‘g‘ri tanlov!")


