# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

benzinFiyat = 21.46
dizelFiyat = 23.14
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input("100km de ortalama yakıt tüketimi: "))
gidilecekYol = float(input("gidilecek yol kaç km: "))
yakitTipi = input("yakıt tipiniz nedir: ")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if (yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi

elif (yakitTipi== "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else:
    print("hatalı yakıt tipi girdiniz.")

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)
