# 5000tl'ye %18 kdv ekleme
print(5000 + (5000 * 0.18))
#sayılar sürekli değiştiğinde veriyi kontrol etmek zorlaşabilir. bunun yerine;
urunA = 5000
urunB = 6000 
urunC = 7000 
kdv = 0.18 #böylece sayılar değiştiğinde tek seferde düzenleme sağlanabilir.
print(urunA + (urunA * kdv))
print(urunB + (urunB * kdv))
print(urunC + (urunC * kdv))

sayi1 = 10
sayi2 = 20
a, b, c = 20, 30, 40
print(a, b, c)
"""
Ürün 1 => 50 TL
Ürün 2 => 60.5 TL
Ürün 3 => 356.45 TL ürünlerin toplamını bulalım
"""
urun1 = 50
urun2 = 60.5
urun3 = 356.45

toplam = urun1 + urun2 + urun3
print("Ürün Toplamı: ", toplam)