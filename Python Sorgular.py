

def k_kucuk(k, liste):
    if k > 0 and k <= len(liste):  
        sirali_liste = sorted(liste)   #Listeyi sıralıyoruz ki elemanları seçerken kolaylık saglasın
        k_kucuk_eleman = sirali_liste[k - 1]  
        return k_kucuk_eleman
    else:
        return "K değerini liste uzunluğuna göre giriniz."  #girilen k degeri ile liste uzunlugu uyusmuyor ise alacagımız cıktı




def en_yakin_cift(hedef_sayi, liste):
    liste.sort()  #Liste içindeki elemanları küçükten büyüğe veya büyükten küçüğe doğrudan sıralar.

    en_yakin = float('inf') #matematiksel anlamda en büyük değeri temsil eder. Genellikle algoritmalar veya programlar içinde bir maksimum değeri temsil etmek için kullandık
    en_yakin_cift = [] #liste 2 elemanlı oldugundan cıktıyı liste olarak alacagız

    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]

            
            if abs(hedef_sayi - toplam) < en_yakin:
                en_yakin = abs(hedef_sayi - toplam) #absyi mutlak değer olarak kullandık
                en_yakin_cift = (liste[i], liste[j])

    print(en_yakin_cift)
    return en_yakin_cift

def tekrar_eden_elemanlar(liste):
    tekrar_edenler = list({x for x in liste if liste.count(x) > 1})
    print(tekrar_edenler)
    return tekrar_edenler

def matris_carpimi(matris1, matris2):
    matris1 = list(map(int, matris1))
    matris2 = list(map(int, matris2))

    if any(isinstance(eleman, str) for eleman in matris1) or any(isinstance(eleman, str) for eleman in matris2):
        return "Hatalı giriş"

    satir_sayisi1 = len(matris1) // len(matris2)
    sutun_sayisi2 = len(matris2) // len(matris1)

    if satir_sayisi1 * len(matris2) != len(matris1) or sutun_sayisi2 * len(matris1) != len(matris2):
        return "Hatalı giriş"

    matris1 = [matris1[i:i + len(matris2)] for i in range(0, len(matris1), len(matris2))]
    matris2 = [matris2[i:i + len(matris1)] for i in range(0, len(matris2), len(matris1))]

    sonuc = [[0 for _ in range(sutun_sayisi2)] for _ in range(satir_sayisi1)]

    for (matris1_satir, matris2_satir) in zip(matris1, matris2):
        for (matris1_eleman, matris2_eleman) in zip(matris1_satir, matris2_satir):
            sonuc[matris1_satir.index(matris1_eleman)][matris2_satir.index(matris2_eleman)] += matris1_eleman * matris2_eleman

    return sonuc

def hizlandirici(n, k, fib_k, fib_k1):
    print(f"{n} {k} {fib_k} {fib_k1}")

    if k == n: #if k == n: ifadesi, belirtilen Fibonacci sayısına ulaşıldığında fonksiyonu durdurur.
        return

    next_fib = fib_k + fib_k1 #bir sonraki Fibonacci sayısını hesaplar. Bu adımda bulunan Fibonacci sayısını hesaplamak için k. adımdaki değer ile (k-1). adımdaki değeri toplar.

    hizlandirici(n, k + 1, next_fib, fib_k)




def en_kucuk_deger(liste):
    en_kucuk = liste[0] 
    for eleman in liste:
        if eleman < en_kucuk: #listedeki elemamanları dolasıyor sort ile de yapılabilirdi ama farklı bir yöntem olarak bunu kullandık
            en_kucuk = eleman #eğer eleman daha kucukse değişkeni değiştiriyoruz
    print('Listedeki en küçük eleman' , en_kucuk)
    return en_kucuk    

def ebobbul(x,y):
  if (x > y):  
    kucuksayi = y 
  else:
    kucuksayi = x
  for i in range(1, kucuksayi + 1):
    if (x % i == 0) and (y % i == 0): #temel ebob kuralını uyguladık
     ebob = i
  print("İki saynın en büyük ortak böleni:", ebob)

def asalsayitesti(x):
 if x > 1: 

     for i in range(2, x):
         if (x % i) == 0: #eger herhangi bir sayıya bolunuyorsa asal sayı olmadıgından once bolunup bolunmedigini anlamak için kontrol ediyoruz
             print(x, " Asal Sayı Değildir.")
             break
     else: #
         print(x, " Asal Sayıdır.")

def karekok(N, x0=1, tol=1e-10, maxiter=10):
    """Babıl döneminden beri kullanılan tekrarlamalı karekök bulma yöntemi."""
    for i in range(maxiter):
        x = (x0 + N / x0) / 2
        if abs(x - x0) < tol: #tol "tolerans" kelimesinin kısaltması olarak kullanılır. Matematiksel veya hesaplamalı bir bağlamda, "tolerans" bir hesaplama veya karşılaştırma sırasında kabul edilebilir bir hata düzeyini ifade eder
            return x
        x0 = x
    raise ValueError("Gerekli doğrulukta karekök bulunamadı")
# -*- coding:utf-8 -*-
def kelime_frekansi(dosya_yolu):

    frekanslar = {}

    with open(dosya_yolu, 'r', encoding="utf-8") as dosya:
        for satir in dosya:
            kelimeler = satir.split() # Her satırdaki kelimeleri ayır

            for kelime in kelimeler:
                kelime = kelime.strip(",.!?;:'") #özel harfleri kaldırıyouz yoksa . , gibi sonuc alabiliriz.
                kelime = kelime.lower() # Kelimelerin tamamını küçük harfe çeviriyorizki kelimiler caps yüzünden farklılaşmasın

                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1

    return frekanslar

import os

def menus():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \033[91m1- K'nıncı küçük eleman\033[0m
    \033[92m2- En yakın çift sayı\033[0m
    \033[93m3- Tekrar eden elemanlar\033[0m
    \033[94m4- Matris çarpımı\033[0m
    \033[95m5- En küçük değer\033[0m
    \033[91m6- EBOB bulma\033[0m
    \033[92m7- Asal sayı testi\033[0m
    \033[93m8- Kelime Frekansı\033[0m
    \033[94m9- Fibonacci Hızlandırıcı\033[0m
    \033[95m10- Karekök Fonksiyonu\033[0m
    \033[91m11- Programdan Çıkış\033[0m
    """)
    return input("\033[94mSeçiminiz: \033[0m")

while True:
    secim = menus()
    if secim == '1':
        k = int(input("Liste için K değerini giriniz: "))
        liste = list(map(int, input("Liste elemanlarını boşlukla ayrılmış şekilde giriniz: ").split()))
        print(k_kucuk(k, liste))
    elif secim == '2':
        hedef_sayi = int(input("Hedef sayıyı giriniz: "))
        liste = list(map(int, input("Liste elemanlarını boşlukla ayrılmış şekilde giriniz: ").split()))
        en_yakin_cift(hedef_sayi, liste)
    elif secim == '3':
        liste = list(map(int, input("Liste elemanlarını boşlukla ayrılmış şekilde giriniz: ").split()))
        tekrar_eden_elemanlar(liste)
    elif secim == '4':
        matris1 = list(map(int, input("Matris A'nın elemanlarını virgülle ayrılmış şekilde giriniz: ").split(',')))
        matris2 = list(map(int, input("Matris B'nın elemanlarını virgülle ayrılmış şekilde giriniz: ").split(',')))
        sonuc = matris_carpimi(matris1, matris2)
        print(sonuc)
    elif secim == '5':
        liste = list(map(int, input("Liste elemanlarını boşlukla ayrılmış şekilde giriniz: ").split()))
        en_kucuk_deger(liste)
    elif secim == '6':
        ebobbul(int(input("Birinci sayıyı giriniz: ")), int(input("İkinci sayıyı giriniz: ")))
    elif secim == '7':
        asalsayitesti(int(input("Sayıyı giriniz: ")))
    elif secim == '8':
        dosya_yolu = 'giris_metni.txt'
        kelime_sonuclari = kelime_frekansi(dosya_yolu)
        print(kelime_sonuclari)
    elif secim == '9':
        n = int(input("Fibonacci sayısı giriniz: "))
        hizlandirici(n, 1, 0, 1)
    elif secim == '10':
            N = int(input("Karekök alınacak sayı: "))
            try:
                result = karekok(N)
                print(f"{N}'nin karekökü: {result}")
            except ValueError as e:
                print(e)
    elif secim == '11':
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
    input("Devam etmek için herhangi bir tuşa basınız...")

    