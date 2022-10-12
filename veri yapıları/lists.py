# msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma".split()
# print(msg[0]) #Python
# msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma"
# print(msg[0]) #P
# msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma".split()
# print(msg) #['Python', 'Kursumuza', 'Hoş', 'Geldiniz.', 'Ben', 'Serdar', 'Tohma']
# msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma".split()
# print(msg[0][0]) #P
# msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma".split()
sayilar = [1,3,5,7,9]
# sonuc = sayilar #[1, 3, 5, 7, 9]
# sonuc = sayilar[0] #1
# sonuc = sayilar[5] # IndexError: list index out of range olmayan değer karşılığı

isimler = ["gamze","ece","bilge","serdar"]
sonuc = isimler[0]
# print(type(isimler)) #<class 'list'>
# print(type(sayilar[0])) #<class 'int'>
# print(type(isimler[0])) #<class 'str'>

listeHayat = ["hayat",20]
listeHilal = ["hilal",4]

sonuc = listeHayat[0] #hayat
sonuc = listeHilal[1] #4
# ogrenciler = [["hayat",20],["hilal",4]] #veya
ogrenciler = [listeHayat,listeHilal]
# sonuc = ogrenciler[0] #['hayat', 20]
# sonuc= ogrenciler[1] #['hilal', 4]
sonuc = ogrenciler[0][0] #hayat isimleri buluruz
sonuc= ogrenciler[1][0] #hilal yaş için ise;
sonuc= ogrenciler[1][1] #4


print(sonuc) 