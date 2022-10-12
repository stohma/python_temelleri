#sıralama önemli değilse, index önemli değilse, tekrarlanan elemanı 1 defa girmek istediğimizde kullanabiliriz

meyveler = {"elma", "kiraz", "kavun", "üzüm"} #{'kiraz', 'üzüm', 'kavun', 'elma'} rasgele sıraladı. index'leme yapılamaz
sebzeler = {"bezelye", "soğan"}

#ekleme yapabiliriz
meyveler.add("karpuz") #{'üzüm', 'kavun', 'kiraz', 'karpuz', 'elma'}
#var olan aynı eleman tekrar yazılmaz, listeye dahil olmaz
meyveler.update(["vişne", "kavun"]) #{'vişne', 'kiraz', 'elma', 'kavun', 'üzüm', 'karpuz'}
sonuc = len(meyveler) #6

#eleman kaldırmak için
# meyveler.remove("karpuz") #{'vişne', 'kiraz', 'kavun', 'üzüm', 'elma'}
# meyveler.remove("karpuzz") #KeyError: 'karpuzz'

#
# meyveler.discard("karpuz") #{'üzüm', 'vişne', 'kiraz', 'kavun', 'elma'}
# meyveler.discard("karpuzz") #{'kiraz', 'kavun', 'vişne', 'üzüm', 'elma', 'karpuz'}

# sonuc = meyveler.pop() #{'kiraz', 'üzüm', 'karpuz', 'elma', 'kavun'}
#rasgele ürün silindi

# meyveler.clear() #set()

#farklı listeleri birleştirme
sonuc = meyveler.union(sebzeler) #{'elma', 'soğan', 'üzüm', 'karpuz', 'bezelye', 'kavun', 'kiraz', 'vişne'}

# sonuc = meyveler
# sonuc = meyveler[0] #'set' object is not subscriptable index yapılamadı
# sonuc = "elma" in meyveler #True

# for x in meyveler:
#     print(x) #kiraz
# # kavun
# # üzüm
# # elma

print(sonuc)