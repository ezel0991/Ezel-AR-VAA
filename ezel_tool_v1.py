
import os
import random
import string
import time
import requests

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def animasyonlu_yazi(metin):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(0.1)
    print()

def banner():
    temizle()
    print("""
[96m███████╗███████╗███████╗██╗     
[96m██╔════╝██╔════╝██╔════╝██║     
[96m███████╗█████╗  █████╗  ██║     
[96m╚════██║██╔══╝  ██╔══╝  ██║     
[96m███████║███████╗██║     ███████╗
[96m╚══════╝╚══════╝╚═╝     ╚══════╝
[92mEZEL V1 - Çok Amaçlı Araç
>> ezel [91m#ariva [92m<<
[95mig=ezel.501a[0m
""")

def ana_menu():
    temizle()
    animasyonlu_yazi("\n\033[91mE Z E L . 5 0 1 A   A R İ V A\033[0m")
    animasyonlu_yazi("\033[95m#  A  R  İ  V  A\033[0m\n")
    while True:
        banner()
        print("""
[93m[1][0m Tool'u Çalıştır
[93m[2][0m Admin Yönlendirme
[93m[3][0m Tool Hakkında Bilgi
[93m[4][0m Sosyal Medya Hesaplarımız
[93m[5][0m Tool'u Kapat
        """)
        secim = input("Seçiminizi yapınız >>> ")

        if secim == "1":
            tool_menu()
        elif secim == "2":
            input("Instagram: @ezel.501a (Enter ile devam)")
        elif secim == "3":
            input("EZEL V1: Çok Amaçlı bir siber güvenlik aracıdır. Enter ile devam.")
        elif secim == "4":
            input("Instagram: @ezel.501a  |  Telegram: @ezeltools  (Enter ile devam)")
        elif secim == "5":
            print("Çıkılıyor...")
            time.sleep(1)
            break
        else:
            input("Geçersiz seçim. Enter ile tekrar dene.")

def tool_menu():
    temizle()
    animasyonlu_yazi("\n\033[91m#  A  R  İ  V  A  !\033[0m\n")
    while True:
        banner()
        print("""
[94m[1][0m IP Analizi (Gerçek)
[94m[2][0m Sahte Kimlik Oluştur
[94m[3][0m Parola Oluştur
[94m[4][0m Geçici E-posta Oluştur
[94m[5][0m Web Sitesi Flood (dummy)
[94m[6][0m USB Killer Bilgilendirme
[94m[7][0m ÖGE Şablonları
[94m[0][0m Geri Dön
        """)
        sec = input("Seçiminizi yapınız >>> ")

        if sec == "1":
            ip = input("Sorgulamak istediğin IP (boş bırak kendi IP): ")
            hedef = ip if ip else ""
            try:
                data = requests.get(f"http://ipwho.is/{hedef}").json()
                for key in ['ip', 'city', 'region', 'country', 'org', 'timezone']:
                    print(f"{key.capitalize()}: {data.get(key, 'Yok')}")
            except:
                print("IP bilgisi alınamadı.")
            input("Devam etmek için Enter...")
        elif sec == "2":
            try:
                fake = requests.get("https://randomuser.me/api/").json()
                kisi = fake['results'][0]
                print("İsim:", kisi['name']['first'], kisi['name']['last'])
                print("E-posta:", kisi['email'])
                print("Adres:", kisi['location']['city'], "-", kisi['location']['country'])
                print("Telefon:", kisi['phone'])
            except:
                print("Sahte kimlik alınamadı.")
            input("Devam etmek için Enter...")
        elif sec == "3":
            chars = string.ascii_letters + string.digits
            pwd = ''.join(random.choice(chars) for _ in range(12))
            print("Oluşturulan Parola:", pwd)
            input("Devam etmek için Enter...")
        elif sec == "4":
            try:
                mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()
                print("Geçici E-posta:", mail[0])
            except:
                print("Mail oluşturulamadı.")
            input("Devam etmek için Enter...")
        elif sec == "5":
            input("Flood sistemi gelecekte eklenecek. Enter ile geri dön.")
        elif sec == "6":
            input("USB Killer fiziksel bir cihazdır. Bu sadece bilgi içindir.")
        elif sec == "7":
            print("OGE Şablonları: Türkçe, Matematik, Fizik. (Bu sadece görseldir.)")
            input("Devam etmek için Enter...")
        elif sec == "0":
            break
        else:
            input("Geçersiz seçim. Enter ile tekrar dene.")

ana_menu()
