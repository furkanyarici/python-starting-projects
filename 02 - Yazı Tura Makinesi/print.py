import random

liste1 = ["Yazı","Tura"]
print("****************************************************"
    
    "\n- Yazı-Tura makinesine hoşgeldin!"
    "\n- Başlangıçta 'y' veya 'n' değerlerini girmen şart."
    "\n- Ardından atılacak para sayısını girmelisin."
    "\n- Devamında geri kalan işi ben yapacağım."
    "\n****************************************************")
secim = int(input("Yazı ve Tura değerlerinin ekranda görünmesi için '1' görünmemesi için '2' yazın : "))
yazi = liste1[0]
sayi = int(input("Kaç para atılsın? : "))
liste2 = []

for i in range(sayi) :
    if secim == 1 :
        print(random.choice(liste1), end = " ")
        liste2.append(random.choice(liste1))
        yazi_sayisi = liste2.count("Yazı")
        tura_sayisi = liste2.count("Tura")
        toplam = yazi_sayisi + tura_sayisi
        yazi_yuzde = (yazi_sayisi / toplam) * 100
        tura_yuzde = (tura_sayisi / toplam) * 100
    elif secim == 2 :
        random.choice(liste1)
        liste2.append(random.choice(liste1))
        yazi_sayisi = liste2.count("Yazı")
        tura_sayisi = liste2.count("Tura")
        toplam = yazi_sayisi + tura_sayisi
        yazi_yuzde = (yazi_sayisi / toplam) * 100
        tura_yuzde = (tura_sayisi / toplam) * 100
print("\n\nParalar atıldı. {} tane yazı, {} tane tura geldi.\nAtılan zar sayısı : {} \nYazı gelme yüzdesi : %{}\nTura gelme yüzdesi : %{}".format(yazi_sayisi,tura_sayisi,sayi,yazi_yuzde,tura_yuzde))