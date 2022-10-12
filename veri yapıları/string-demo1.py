website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(kursAdi)) #58
print(len(website)) #25

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10]) #www

# 3- 'website' içinden com karakterlerini alın.
print(website[-3:]) #com

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
print(kursAdi[:15]) #Python Dersleri
print(kursAdi[-15:]) #on Programlama.

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1]) #.amalmargorP nohtyP eyiveS irelİ nadrıfıS :irelsreD nohtyP

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = "Hello world"
s = s[:6] + "W" + s[-4:]
print(s) #Hello World

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
n= "abc"
print("{}, {}, {}.".format(n,n,n)) #abc, abc, abc. veya
print("abc" * 3) #abcabcabc
print("abc " * 3) #abc abc abc

name, surname, age, job = 'Sadık','Turan', 37, 'öğretmen' 

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.'
name = "Sadık"
surname = "Turan"
age = 37
job = "öğretmen"
print("Benim adım {} {}, Yaşın {} ve mesleğim {}.".format(name, surname, age, job)) #veya
print(f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}.")
#Benim adım Sadık Turan, Yaşın 37 ve mesleğim öğretmen.
