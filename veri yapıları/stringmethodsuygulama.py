website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
sonuc = " Hello World ".strip()
sonuc = " Hello World ".lstrip() #soldan boşluk siler
sonuc = " Hello World ".rstrip() #sağdan boşluk siler
sonuc = "http://www.sadikturan.com".lstrip("/:htpw.") #sadikturan.com

print(sonuc) #Hello World

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
sonuc = "www.sadikturan.com".strip("w.com")
print(sonuc) #sadikturan

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc = kursAdi.lower()
print(sonuc) #python dersleri: sıfırdan i̇leri seviye python programlama.

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
sonuc = website.count("a")
print(sonuc) #2

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
sonuc = website.startswith("www")  #False
sonuc = website.startswith("http") #True
print(sonuc)

# 6- 'website' içinde '.com' ifadesi var mı?
sonuc = website.find(".com") #21
sonuc = website.find("Python") # -1
sonuc = kursAdi.find("Python") # 0
sonuc = kursAdi.rfind("Python") # 39 /saymaya sağdan başla
print(sonuc) 

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
sonuc = "abc1".isalpha() #False
sonuc = "123".isdigit() #True
print(sonuc) 

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
sonuc = "Contents".center(50,"*") #*********************Contents*********************
sonuc = "Contents".ljust(50,"*") #Contents******************************************
sonuc = "Contents".rjust(50,"*") #******************************************Contents
print(sonuc)

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
sonuc = kursAdi.replace(":","").replace(" ","-").replace(".","") #Python-Dersleri-Sıfırdan-İleri-Seviye-Python-Programlama
print(sonuc)

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
msg = "Hello World"
sonuc = msg.replace("World","There")
print(sonuc) #Hello There

# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
sonuc = kursAdi.split()
print(sonuc) #['Python', 'Dersleri:', 'Sıfırdan', 'İleri', 'Seviye', 'Python', 'Programlama.']

a = "Hello, World".split(",")
print(a)

ad = "Ahmet"
soyad = "Yılmaz"
yas = 35
 
print("My name is {0} {0} and I am {2} years old.".format(ad,soyad,yas))

print("Sadık".isalpha())