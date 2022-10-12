isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk") #['Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']


# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena") #['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
# isimler.insert(len(isimler),"Sena") #['Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk', 'Sena']

# 3-  "Yiğit" ismini listeden siliniz.
# isimler.remove("Yiğit") #['Sena', 'Ada', 'Hasan', 'Beril', 'Cenk'] veya
# isimler.pop()

# 4-  "Yiğit" isminin indeksi nedir ?
print(isimler.index("Yiğit")) #2

# 5-  "Beril" listenin bir elemanı mıdır ?
# if "Beril" in isimler:
#     print("evet") #evet   veya
sonuc = "Beril" in isimler
print(sonuc) #True

# 6-  Liste elemanlarını ters çevirin.
isimler.reverse() #['Cenk', 'Beril', 'Hasan', 'Yiğit', 'Ada', 'Sena']

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# isimler.sort() #['Ada', 'Beril', 'Cenk', 'Hasan', 'Sena', 'Yiğit']

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort() #[1987, 1998, 1998, 2000]

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
# s = "IPhone X,IPhone XR"
# sonuc = type(s)
# print(type(s)) #<class 'str'>
# s = ["IPhone X,IPhone XR"]
# print(type(s)) #<class 'list'>

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
sonuc = max(yaslar) #2000
sonuc = min(yaslar) #1987
print(sonuc)

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998)) #2


# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear() #[]

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar) #marka: iphone 8
# marka: iphone 9
# marka: iphone x
# ['iphone 8', 'iphone 9', 'iphone x']


# print(isimler)
print(yaslar)
