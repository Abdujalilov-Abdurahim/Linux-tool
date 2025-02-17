#/bin/bash/python

import os

from pycparser.c_ast import While


def banner():
    banner = f"""
    ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
    ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
    ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
    ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
    ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                         
"""


def run_hydra():
    banner()
    print("Hydra bilan ishlash")

    # Maqsadli IP yoki domenni kiritish
    while True:
        target = input("\nMaqsadli IP yoki domenni kiriting: ")
        if target.replace(".", "").isdigit() or "." in target:
            break
        print("❌ Noto'g'ri format! Iltimos, to'g'ri IP yoki domen kiriting.")

    while True:
        print("\nXizmatni tanlang:")
        print("1. SSH")
        print("2. FTP")
        print("3. HTTP (Basic auth)")
        print("4. MySQL")
        print("5. Telnet")
        print("6. RDP (Windows)")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")
        service = ""

        if choice == "1":
            service = "ssh"
        elif choice == "2":
            service = "ftp"
        elif choice == "3":
            service = "http"
        elif choice == "4":
            service = "mysql"
        elif choice == "5":
            service = "telnet"
        elif choice == "6":
            service = "rdp"
        elif choice == "0":
            print("Dasturdan chiqildi.")
            return
        else:
            print("❌ Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
            return

        # Loginni kiritish
        username = input("Foydalanuvchi nomini kiriting yoki fayl (user.txt) tanlang: ")

        # Parolni kiritish
        password_option = input("Bitta parolni sinash (1) yoki fayldan (2) yuklash: ")

        if password_option == "1":
            password = input("Parolni kiriting: ")
            command = f"hydra -l {username} -p {password} {target} {service}"
        elif password_option == "2":
            password_file = input("Parol faylini kiriting (masalan, passwords.txt): ")
            command = f"hydra -l {username} -P {password_file} {target} {service}"
        else:
            print("❌ Noto'g'ri tanlov. Dasturdan chiqildi.")
            return

        # Hydra buyrug‘ini ishga tushirish
        print("\nHydra ishga tushirilmoqda...\n")
        os.system(command)

        a = input("Yana foydalanasizmi?: yes/no").lower()
        if a != "yes":
            break


# Test qilish
if __name__ == "__main__":
    run_hydra()
