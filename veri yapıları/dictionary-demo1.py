# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

# urunler = {}

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }


# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }


# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat
# }

# {'100': {'ad': 'iphone 8', 'fiyat': '5000'}, '101': {'ad': 'iphone x', 'fiyat': '6000'}, '102': {'ad': 'iphone xr', 'fiyat': '7000'}} örnek giriş

# print(urunler)

urunler = {
    '100': {'ad': 'iphone 8', 'fiyat': '5000'}, 
    '101': {'ad': 'iphone x', 'fiyat': '6000'}, 
    '102': {'ad': 'iphone xr', 'fiyat': '7000'}
}

# print(urunler)

id = input("aramak istediğiniz ürün id: ") #input'a yukarıda tanımlı hangi veri girilirse onun karşılığındaki değerler çıktı olur. 
#101, 102 veya 103
urun = urunler[id]

# print(urun) veya
print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyatı: {urun["fiyat"]}') #dışta ve içte "" kullanıldığından SyntaxError: f-string: unmatched '[' hatası aldık. içteki "" ise dıştaki '' olmalı
#üstteki gibi input'a tanımlı değer girildiğinde çıktıyı yandaki verir: id: 101 ürün adı: iphone x ürün fiyatı: 6000
# print(urunler)