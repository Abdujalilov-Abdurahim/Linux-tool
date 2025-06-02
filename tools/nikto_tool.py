#!/usr/bin/python

import os
import re

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    clear()
    print(r"""
    ███▄    █     ██▓    ██ ▄█▀   ▄▄▄█████▓    ▒█████  
     ██ ▀█   █    ▓██▒    ██▄█▒    ▓  ██▒ ▓▒   ▒██▒  ██▒
    ▓██  ▀█ ██▒   ▒██▒   ▓███▄░    ▒ ▓██░ ▒░   ▒██░  ██▒
    ▓██▒  ▐▌██▒   ░██░   ▓██ █▄    ░ ▓██▓ ░    ▒██   ██░
    ▒██░   ▓██░   ░██░   ▒██▒ █▄     ▒██▒ ░    ░ ████▓▒░
    ░ ▒░   ▒ ▒    ░▓     ▒ ▒▒ ▓▒     ▒ ░░      ░ ▒░▒░▒░ 
    ░ ░░   ░ ▒░    ▒ ░   ░ ░▒ ▒░       ░         ░ ▒ ▒░ 
       ░   ░ ░     ▒ ░   ░ ░░ ░      ░         ░ ░ ░ ▒  
             ░     ░     ░  ░                      ░ ░  
    """)

def is_valid_target(target):
    # IP adres yoki URL'ni tekshirish
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    url_pattern = r'^(http://|https://).+'
    return re.match(ip_pattern, target) or re.match(url_pattern, target)

def run_nikto():
    banner()
    print("🔍 Nikto bilan ishlash\n")

    while True:
        target = input("🎯 Maqsadli URL yoki IP-ni kiriting: ").strip()
        if is_valid_target(target):
            break
        print("❌ Noto'g'ri format! Masalan: http://example.com yoki 192.168.1.1")

    while True:
        print("\n📋 Tanlang:")
        print("1. Oddiy skanerlash")
        print("2. HTTPS orqali skanerlash")
        print("3. Maxsus portni tekshirish")
        print("4. Veb-server haqida ma’lumot")
        print("5. Natijani log faylga yozish")
        print("6. Maksimal xavfsizlik skaneri (tuning)")
        print("0. Chiqish va bosh menyuga qaytish")

        choice = input("\n🔢 Tanlovingiz: ").strip()
        command = ""

        if choice == "1":
            command = f"nikto -h {target}"
        elif choice == "2":
            command = f"nikto -h {target} -ssl"
        elif choice == "3":
            port = input("🛠 Port raqamini kiriting (masalan, 8080): ").strip()
            if port.isdigit():
                command = f"nikto -h {target} -p {port}"
            else:
                print("❌ Port faqat raqamlardan iborat bo'lishi kerak.")
                continue
        elif choice == "4":
            command = f"nikto -h {target} -Display V"
        elif choice == "5":
            log_file = input("📁 Log fayl nomini kiriting (masalan, nikto_log.txt): ").strip()
            command = f"nikto -h {target} -output {log_file}"
        elif choice == "6":
            command = f"nikto -h {target} -Tuning 123bde"
        elif choice == "0":
            print("\n↩ Asosiy menyuga qaytildi.")
            import main  # main.py fayliga qaytish
            main.main()
            return
        else:
            print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")
            continue

        os.system(command)

        repeat = input("\n🔁 Yana skanerlaysizmi? (yes/no): ").lower()
        if repeat != "yes":
            print("\n↩ Asosiy menyuga qaytildi.")
            import main
            main.main()
            return
