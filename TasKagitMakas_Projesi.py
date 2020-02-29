import random
import time as zaman
#TAS=1 - KAGIT=2 - MAKAS=3
while 1:
    pc_secimi=random.choice(["1","2","3"])
    user_secim=input("************  TAS(1)   KAGIT(2)   MAKAS(3)    ************\nSECİMİNİZİ YAPINIZ:")
    zaman.sleep(2)
    print("BILGISAYARIN SECIMI:{}".format(random.choice(pc_secimi)))
    if ((pc_secimi=='1' and user_secim=='2') or (pc_secimi=='2' and user_secim=='3')or (pc_secimi=='3'and user_secim=='1')):
        zaman.sleep(2)
        print("************KAZANAN USER************")
        zaman.sleep(1)
    elif ((pc_secimi=='2' and user_secim=='1') or (pc_secimi=='3' and user_secim=='2')or (pc_secimi=='1'and user_secim=='3')):
        zaman.sleep(2)
        print("************KAZANAN BILGISAYAR************")
        zaman.sleep(1)
    elif (pc_secimi==user_secim):
        zaman.sleep(2)
        print("************SONUC ESİTTİR************\nOYUN TEKRAR BASLIYOR")
        zaman.sleep(1)
    if (user_secim=="q"):
        zaman.sleep(2)
        break


