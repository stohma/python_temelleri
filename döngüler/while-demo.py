# sayilar = [4, 6, 9, 10, 35, 57, 89, 125, 244]

# 1: sayilar listesini while ile ekrana yazdırın

# for i in sayilar:
#     print(i)
# for ile üstteki gibi yapabiliriz.

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# veya

# while sayilar:
#     print(sayilar.pop(0)) #bu da alternatif yol

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# i=0 veya
# baslangic = int(input('baslangıç: '))
# bitis = int(input('bitis: '))
#
# i= baslangic
# while i < bitis:
#     i+=1
#     if(i%2==1): # tek sayı
#         print(i)

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın

# i=100
#
# while(i>0):
#     print(i)
#     i-=1

# 4: kullanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazdırın

# sayilar=[]
#
# i=0
# while(i<5):
#     sayi=int(input("sayı: "))
#     sayilar.append(sayi)
#     i+=1
#
# sayilar.sort()
# print(sayilar)

# kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içerisine saklayınız.
# ** ürün sayısınız kullanıcıya sorun
# ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

i=0
adet=int(input('kaç adet ürün eklemek istiyorsunuz: '))
urunler=[]

while (i<adet):
    urunAdi=input('ürün adı: ')
    fiyat=input('ürün fiyatı: ')
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i+=1

print(urunler)

# kaç adet ürün eklemek istiyorsunuz: 7
# [{'urunAdi': 'serdar', 'fiyat': '1000'}, {'urunAdi': 'gamze', 'fiyat': '2000'}, {'urunAdi': 'ece', 'fiyat': '3000'}, {'urunAdi': 'hayat', 'fiyat': '4000'}, {'urunAdi': 'hilal', 'fiyat': '5000'}, {'urunAdi': 'bilge', 'fiyat': '6000'}, {'urunAdi': 'tohma', 'fiyat': '7000'}]

for urun in urunler:
    print(f"ürün adı: {urun['urunAdi']} ürün fiyatı: {urun['fiyat']}")
# [{'urunAdi': 'iphone x', 'fiyat': '2000'}]
# ürün adı: iphone x ürün fiyatı: 2000
