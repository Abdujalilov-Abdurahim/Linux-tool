#/bin/bash/python
import os
import re

def banner():
    banner = f""""""

    return banner

def run_dnsenum():
    banner()
    print("DNSEnum bilan ishlash")

    # Maqsadli domenni tekshirish
    while True:
        target = input("\nMaqsadli domenni kiriting (masalan: example.com): ")
        if re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", target):
            break
        print("❌ Noto'g'ri domen formati! Iltimos, to'g'ri domen kiriting.")

    while True:
        print("\nTahlil turini tanlang:")
        print("1. DNS yozuvlarini olish (A, MX, NS, TXT)")
        print("2. Subdomainlarni topish")
        print("3. Zone Transfer (AXFR) hujumi")
        print("4. Reverse DNS lookup (IP orqali domen topish)")
        print("0. Chiqish")

        choice = input("\nTanlovni kiriting: ")

        if choice == "1":
            command = f"dnsenum --enum {target}"
        elif choice == "2":
            command = f"dnsenum --enum -f subdomains-top1mil-5000.txt {target}"
        elif choice == "3":
            command = f"dnsenum --enum --axfr {target}"
        elif choice == "4":
            ip = input("Reverse lookup uchun IP-manzilni kiriting: ")
            command = f"dnsenum --reverse {ip}"
        elif choice == "0":
            print("Dasturdan chiqildi.")
            return
        else:
            print("❌ Noto'g'ri tanlov! Qaytadan urinib ko‘ring.")
            return

        print("\nDNSEnum ishga tushirilmoqda...\n")
        os.system(command)

        a = input("Yana foydalanasizmi?: yes/no").lower()
        if a != "yes":
            break

# Test qilish
if __name__ == "__main__":
    run_dnsenum()