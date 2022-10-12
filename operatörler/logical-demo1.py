# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

# sayi = int(input("sayı: "))
# sonuc = (50 < sayi < 100)
# print(sonuc)

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

# sayi = int(input("sayı: "))
# sonuc = ((sayi > 0) and (sayi % 2 != 0))
# print(sonuc)

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 

# _username = "serdartohma"
# _password = "12345"
#
# girilenUsername = input("username: ")
# girilenPassword = input("password: ")
#
# sonuc = (girilenUsername == _username) and (girilenPassword == _password)
# print("girilen username ve password doğru: " , sonuc)

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
#
# sonuc = (x > y) and (x > z) # x en büyü
# print("x en büyük sayı", sonuc)
#
# sonuc = (y > x) and (y > z)
# print("y en büyük sayı", sonuc)
#
# sonuc = (z > x) and (z > y)
# print("z en büyük sayı", sonuc)


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input("vize 1: "))
# vize2 = float(input("vize 2: "))
# final = float(input("final: "))
#
# ortalama = ((((vize1 + vize2) / 2) * 0.4) + (final * 0.6))

# sonuc1 >= 50
#a
# sonuc = (ortalama >= 50) and (final >= 50)
#b
# sonuc = (ortalama >= 50) or (final >= 70)

# print(f'öğrenci not ortalaması: {ortalama} ve geçme durumu: {sonuc}')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
#
ad = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

kiloIndex = kg / (hg ** 2)

zayif = (kiloIndex >= 0) and (kiloIndex <= 18.4)
normal = (kiloIndex > 18.4) and (kiloIndex <= 24.9)
kilolu = (kiloIndex > 24.9) and (kiloIndex <= 29.9)
obez = (kiloIndex >= 29.9) and (kiloIndex <= 34.9)

print(f'{ad} kilo indeksin: {kiloIndex} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{ad} kilo indeksin: {kiloIndex} ve kilo değerlendirmen normal: {normal}')
print(f'{ad} kilo indeksin: {kiloIndex} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{ad} kilo indeksin: {kiloIndex} ve kilo değerlendirmen obez: {obez}')