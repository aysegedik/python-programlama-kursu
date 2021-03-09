
def giris_ekrani():
    print("Hangi işlem?")
    print("""1- Toplama
    2- Çıkarma

    Çıkmak için Ç harfine basınız.
    
    Seçim için sıra nosunu yazınız : 
    """)

def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Sayıyı girin (Çıkmak için Ç'ye basın):")
        
        if sayi == "Ç":
            break

        sayi = int(sayi)

        sayilar.append(sayi)
    
    return sayilar

def cikarma(b):
    fark = sayilar[0]
        # 1, 2, 3, 4 .....
    for index in range(1,len(sayilar)):
        fark = fark - sayilar[index] 

def toplama(a):
    # toplam = sayilar[0] + sayilar[1]
        toplam = 0
        # [30, 40, 60]
        for sayi in a:
            toplam = toplam + sayi

        print(f"Toplama sonucu : {toplam}")
while True:
    
    giris_ekrani()

    secim = input()

    if secim == "Ç":
        break

    if not (secim == "1" or secim == "2"):
        print("Yanlış giriş yaptın.")
        continue 
    

    sayilar = veri_girisi()

    print(sayilar)

    if secim == "1":
        toplama(sayilar)

    elif secim == "2":

        cikarma(sayilar)

    else:
        print("Yanlış seçim yaptınız.")

