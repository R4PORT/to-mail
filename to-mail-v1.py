# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import smtplib

os.system("clear")
print ("")
print ("")
print ("████████╗ ██████╗ ███╗   ███╗ █████╗ ██╗██╗   ")
print ("╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗██║██║   ")
print ("   ██║   ██║   ██║██╔████╔██║███████║██║██║   ")
print ("   ██║   ██║   ██║██║╚██╔╝██║██╔══██║██║██║   ")
print ("   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗")
print ("   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝")
print ("  TO MAIL SCRİPT V1.0 | CODED BY R4POR-T")
print ("  contact: www.instagram.com/onurcan.r00t")
print ("  mail: root@teknoalerji.com")
print ("")
print ("Lütfen Yapmak istediniz secenegi secin.")
print ("1- SMTP Mail Gönderme")
print ("2- SMTP Mail Alma: ")
print ("3- imza")
print ("4- Çıkış")

smtp = int(input("yapmak istediğiniz işlemi seçin."))


if smtp == 1:
   print ("")
   print ("")
   print("https://myaccount.google.com/u/1/lesssecureapps?pageId=none")
   print("Yukarıda bıraktığım linkten güvenlik ayarlarını kapatın.")
   print ("")
   smtp_adresi= "smtp.gmail.com"
   smtp_port= "587"
   mail_adresi = input("Mail Adresinizi girin: ")
   mail_sifresi = input("şifrenizi girin: ")
   alici = input("Gönderilicek Mail Adresi <to@gmail.com>: ")
   konu = input("Konu Giriniz: ")
   mesaj = input("Göndermek istediniz masajı yazınız : ")
   mesaj1 = mesaj,"gönderen", mail_adresi
   server = smtplib.SMTP(smtp_adresi, smtp_port)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login(mail_adresi, mail_sifresi)

   try:
       server.sendmail(mail_adresi, alici, mesaj)
       print ("Mail Gonderildi")
   except:
       print ("Mail Gonderilemedi")


if smtp == 2:
    print("Çok yakında güncelleme ile yayınlancak")


if smtp == 3:
    print("")
    print("████████╗ ██████╗ ███╗   ███╗ █████╗ ██╗██╗   ")
    print("╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗██║██║   ")
    print("   ██║   ██║   ██║██╔████╔██║███████║██║██║   ")
    print("   ██║   ██║   ██║██║╚██╔╝██║██╔══██║██║██║   ")
    print("   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗")
    print("   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝")
    print("  TO MAIL SCRİPT V1.0 | CODED BY R4POR-T")
    print("  contact: www.instagram.com/onurcan.r00t")
    print("  mail: root@teknoalerji.com")


if smtp == 4:
    exit()