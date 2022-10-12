sayilar = [1,5,8,9,3,45,77,5]
harfler = ["a","b","e","s","a","y"]

sonuc = min(sayilar) #1
sonuc = max(sayilar) #77
sonuc = min(harfler) #a
sonuc = max(harfler) #y

#ekleme
sayilar.append(10) #sona değer ekler
sonuc= sayilar #[1, 5, 8, 9, 3, 45, 77, 10]

sayilar.insert(3,5) #[1, 5, 8, 5, 9, 3, 45, 77, 10]  istenilen yere değer ekler
sayilar.insert(-1,50) #[1, 5, 8, 5, 9, 3, 45, 77, 50, 10]
sayilar.insert(len(sayilar),150) #[1, 5, 8, 5, 9, 3, 45, 77, 50, 10, 150] insert ile sona değer ekleme

#silme
sayilar.pop() #[1, 5, 8, 5, 9, 3, 45, 77, 50, 10] sondaki değeri siler
sayilar.pop() #[1, 5, 8, 5, 9, 3, 45, 77, 50]
sayilar.pop(0) #[5, 8, 5, 9, 3, 45, 77, 50] aynı zamanda istediğimiz konumdaki değeri de silebiliriz

sayilar.remove(45) #[5, 8, 5, 9, 3, 77, 50] doğrudan ilgili değeri de silebiliriz 
harfler.remove("y") #['a', 'b', 'e', 's', 'a']

# sonuc = sayilar
sonuc = harfler

# sıralama
sayilar.sort() #[3, 5, 5, 8, 9, 50, 77]
harfler.sort() #['a', 'a', 'b', 'e', 's']
sayilar.reverse() #[77, 50, 9, 8, 5, 5, 3]

print(sayilar.count(5)) #3
print(harfler.count("a")) #2

print(sayilar.index(77)) #0

sonuc = sayilar
# sonuc = harfler

# sayilar.clear() #[]

print(sonuc)