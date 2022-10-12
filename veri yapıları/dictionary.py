# 41 = Kocaeli
# 34 = İstanbul

sehirler = ["kocaeli", "istanbul"]
plakalar =[41, 34]

# print(plakalar[0], sehirler[0]) #41 kocaeli
# print(plakalar[1], sehirler[1]) #34 istanbul

# print(plakalar[sehirler.index("istanbul")]) #34
# print(plakalar[sehirler.index("kocaeli")]) #41


plakalar = {"kocaeli": 41, "istanbul": 34} #bu yolla da aynı sonuca daha kestirmeden ulaşabiliriz

# print(plakalar["kocaeli"]) #41
# print(plakalar["istanbul"]) #34

plakalar["rize"] = 53
# plakalar["izmir"] = 36 #hata yaparsak son değeri dikkate alacağından üstte yapılan hata görünmez

# plakalar["izmir"] = 35


# print(plakalar) #{'kocaeli': 41, 'istanbul': 34, 'rize': 53, 'izmir': 35}  üstteki listeye ekleme yaptık

# ogrenciler = {100: "hayat"} #hayat
# print(ogrenciler[100]) 

ogrenciler = {
    100: {
        "ad": "hayat",
        "soyad": "tohma",
        "yas": 9,
        "notlar":[70,80,70] 
    }, #{'ad': 'hayat', 'soyad': 'tohma', 'yas': 9}
    101: {
        "ad": "hilal",
        "soyad": "tohma",
        "yas": 4
    }
} 

# sonuc = ogrenciler[100] #{'ad': 'hayat', 'soyad': 'tohma', 'yas': 9}
# sonuc = ogrenciler[101] #{'ad': 'hilal', 'soyad': 'tohma', 'yas': 4}

sonuc = ogrenciler[100]["ad"] #hayat
sonuc = ogrenciler[101]["soyad"] #tohma
sonuc = ogrenciler[100]["notlar"] #[70, 80, 70]
sonuc = ogrenciler[100]["notlar"][0] #70 
sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) /3  #73.33333333333333


print(sonuc)
