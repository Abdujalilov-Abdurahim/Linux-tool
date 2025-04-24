#!/bin/bash/python

import os
from termcolor import colored

def run_netcat():
    os.system("clear")
    print(colored(r"""
 _   _      _   _              _   
| \ | | ___| |_| |__   ___  __| |_ 
|  \| |/ _ \ __| '_ \ / _ \/ _` (_)
| |\  |  __/ |_| | | |  __/ (_| |_ 
|_| \_|\___|\__|_| |_|\___|\__,_(_)

         --- Netcat Tool ---
""", "cyan"))

    while True:
        print(colored("\nNetcat funksiyalarini tanlang:", "yellow"))
        print("1. Server (listener) rejimida tinglash")
        print("2. Klient (bog'lanish) rejimi")
        print("3. Fayl yuborish/qabul qilish (file transfer)")
        print("4. Port skanerlash")
        print("0. Ortga qaytish")

        choice = input("\nTanlovni kiriting: ")

        if choice == "1":
            port = input("📡 Tinglash uchun port raqamini kiriting: ")
            os.system(f"nc -lvp {port}")
        
        elif choice == "2":
            target = input("🎯 Maqsadli IP yoki domen: ")
            port = input("🔌 Port raqami: ")
            os.system(f"nc {target} {port}")

        elif choice == "3":
            mode = input("Fayl yuborish (send) yoki qabul qilish (recv)? ").lower()
            if mode == "send":
                target = input("🎯 Qabul qiluvchi IP: ")
                port = input("🔌 Port: ")
                filepath = input("📄 Yuboriladigan fayl yo‘li: ")
                os.system(f"cat {filepath} | nc {target} {port}")
            elif mode == "recv":
                port = input("📡 Tinglash porti: ")
                output = input("📥 Saqlash uchun fayl nomi: ")
                os.system(f"nc -lvp {port} > {output}")
            else:
                print(colored("❌ Noto'g'ri tanlov.", "red"))

        elif choice == "4":
            target = input("🎯 Maqsadli IP: ")
            ports = input("🔍 Qaysi portlar oraliqda? (masalan: 20-80): ")
            os.system(f"nc -zv {target} {ports}")

        elif choice == "0":
            print(colored("\n🔙 Asosiy menyuga qaytilmoqda...", "green"))
            break

        else:
            print(colored("❌ Noto‘g‘ri tanlov. Iltimos, 0–4 oralig‘idagi raqamni tanlang.", "red"))

        input(colored("\n⏎ Davom etish uchun Enter tugmasini bosing...", "magenta"))
        os.system("clear")
