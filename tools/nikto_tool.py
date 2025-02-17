#/bin/bash/python

import os

def banner():
    banner = f"""
    ███▄    █     ██▓    ██ ▄█▀   ▄▄▄█████▓    ▒█████  
     ██ ▀█   █    ▓██▒    ██▄█▒    ▓  ██▒ ▓▒   ▒██▒  ██▒
    ▓██  ▀█ ██▒   ▒██▒   ▓███▄░    ▒ ▓██░ ▒░   ▒██░  ██▒
    ▓██▒  ▐▌██▒   ░██░   ▓██ █▄    ░ ▓██▓ ░    ▒██   ██░
    ▒██░   ▓██░   ░██░   ▒██▒ █▄     ▒██▒ ░    ░ ████▓▒░
    ░ ▒░   ▒ ▒    ░▓     ▒ ▒▒ ▓▒     ▒ ░░      ░ ▒░▒░▒░ 
    ░ ░░   ░ ▒░    ▒ ░   ░ ░▒ ▒░       ░         ░ ▒ ▒░ 
       ░   ░ ░     ▒ ░   ░ ░░ ░      ░         ░ ░ ░ ▒  
             ░     ░     ░  ░                      ░ ░  
                                                        
"""


def run_nikto():
    banner()
    print("Nikto bilan ishlash")

    # Maqsadli URL yoki IP-ni kiritish
    while True:
        target = input("\nMaqsadli URL yoki IP-ni kiriting (masalan, http://example.com yoki 192.168.1.1): ")
        if target.startswith("http://") or target.startswith("https://") or target.replace(".", "").isdigit():
            break
        print("❌ Noto'g'ri format! Iltimos, to'g'ri URL yoki IP kiriting.")

    print("\nQo'shimcha parametrlarni tanlang:")
    print("1. Oddiy skanerlash")
    print("2. HTTPS orqali skanerlash")
    print("3. Maxsus portni tekshirish")
    print("4. Veb-server haqida ma’lumot olish")
    print("5. Xatolarni logga yozish")
    print("6. Maksimal xavfsizlik skaneri")
    print("0. Chiqish")

    choice = input("\nTanlovni kiriting: ")
    command = ""

    while True:
        if choice == "1":
            command = f"nikto -h {target}"
        elif choice == "2":
            command = f"nikto -h {target} -ssl"
        elif choice == "3":
            port = input("Portni kiriting (masalan, 8080): ")
            command = f"nikto -h {target} -p {port}"
        elif choice == "4":
            command = f"nikto -h {target} -id"
        elif choice == "5":
            log_file = input("Log fayl nomini kiriting (masalan, nikto_log.txt): ")
            command = f"nikto -h {target} -output {log_file}"
        elif choice == "6":
            command = f"nikto -h {target} -Tuning 123bde"
        elif choice == "0":
            print("Dasturdan chiqib ketildi.")
            return
        else:
            print("❌ Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")
            return

    # Nikto buyrug'ini ishga tushirish
        os.system(command)

        a = input("Yana foydalanasizmi?: yes/no").lower()
        if a != "yes":
            break

# Test qilish
if __name__ == "__main__":
    run_nikto()


