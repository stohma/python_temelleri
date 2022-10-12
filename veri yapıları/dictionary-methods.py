opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
} #{'marka': 'Opel', 'model': 'Corsa', 'yil': 2020}

# sonuc = opelObj["marka"] #Opel
# sonuc = opelObj.get("marka") ##Opel

# for x in opelObj:
#     print(x) #marka
# # model
# # yil

# for x in opelObj:
#     print(opelObj[x]) #Opel
# # Corsa
# # 2020

# for x in opelObj:
#     print(opelObj[x]) #marka
# # model
# # yil
# # Opel
# # Corsa
# # 2020
# # Opel
# # Corsa
# # 2020

# for x in opelObj.values():
#     print(x) #Opel
# # Corsa
# # 2020

# for x,y in opelObj.items():
#     print(x,y) #marka Opel
# # model Corsa
# # yil 2020

# sonuc ="marka" in opelObj #True
# sonuc = (len(opelObj)) #3
# opelObj["renk"] = "kırmızı" #{'marka': 'Opel', 'model': 'Corsa', 'yil': 2020, 'renk': 'kırmızı'} eleman ekleme
# opelObj.pop("renk") #{'marka': 'Opel', 'model': 'Corsa', 'yil': 2020} eleman silme
# opelObj.popitem() #sondaki veriyi siler.  {'marka': 'Opel', 'model': 'Corsa'}

# del opelObj["marka"] #{'model': 'Corsa', 'yil': 2020} listedeki istenilen elemanı siler
# del opelObj #NameError: name 'opelObj' is not defined
# opelObj.clear() #bütün listeyi siler {}

# obj = opelObj #{'marka': 'Opel', 'model': 'Corsa', 'yil': 2020} referans olarak kullanır
obj = opelObj.copy() # bu şekilde print(obj) ile print(opelObj) ayrı çıktılar verir

obj["marka"] = "Mazda" #{'marka': 'Mazda', 'model': 'Corsa', 'yil': 2020} hem de her iki print'te de marka değişimi oldu. aynı çıktı elde edildi

opelObj.update({
    "marka": "Bmw", #{'marka': 'Bmw', 'model': 'Corsa', 'yil': 2020}
    "renk": "kırmızı" #{'marka': 'Bmw', 'model': 'Corsa', 'yil': 2020, 'renk': 'kırmızı'}
})

# print(sonuc)
print(obj)
print(opelObj)