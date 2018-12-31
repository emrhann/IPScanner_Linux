# IP SCANNER #


import os
import time
from subprocess import Popen

from pip._vendor.distlib.compat import raw_input

devnull = open(os.devnull, 'wb')

ipscanner_yazi: str = '''
*********************************************************
*               LOCAL NETWORK IP SCANNER                *
*********************************************************
*              DEVELOPER :EMİRHAN IŞIK                  *                       
*        Mail Address : isikemirhan@outlook.com         *
*********************************************************
'''

print(ipscanner_yazi)

star = "**********************************************************************"

print(star)

ip_araligi_deger = raw_input("IP Aralığını giriniz ( example: 192.168.0.0 ) ---> ")

print(star)


print("Taranan ip aralığı ",ip_araligi_deger)

print(star)

if ip_araligi_deger == "":
     print (star)
     print ("Geçerli bir ip alığını deneyiniz...")
     print (star)

import sys

p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(0,255):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s Aktif' % ip)
                aktif = aktif + 1
            elif proc.returncode == 2:
                print('%s Yanıt yok' % ip)
                aktif = yanit_yok + 1
            else:
                print('%s Pasif' % ip)
                pasif = pasif + 1
    time.sleep(.04)

devnull.close()

print(star)

import os

print ("Geçerli işletim sistemi",os.name)
print ("Ağ Durumu")
print ("Aktif Ipler  [ ",aktif," ]")
print ("Pasif IPler [ ",pasif," ]")
print ("Yanıt Yok  [ ",yanit_yok," ]")

print(star)

bitis_mesaj = "Tarama tamamlandı.."

print(bitis_mesaj)

print(star)
