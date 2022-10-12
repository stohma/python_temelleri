ad = "Serdar"
soyad = "Tohma"
print(type(ad)) #<class 'str'>
yas = "36"
print(type(yas)) #<class 'str'>

msj = "benim adım " + ad + " ve soyadım " + soyad + ". Yaşım ise " + yas + "."
print(msj) #benim adım Serdar ve soyadım Tohma. Yaşım ise 36
#print(len(msj)) #karakter sayısı verir. çıktı: 49
karakterSayisi = len(msj)
print(msj[karakterSayisi - 1]) #. sondan başlar
print(msj[0:5]) #benim
print(msj[6:17]) #adım Serdar
print(msj[:10]) #benim adım
print(msj[11:]) #Serdar ve soyadım Tohma. Yaşım ise 36.
print(msj[-13:-1]) #Yaşım ise 36
print(msj[0:40:2]) #bnmaı edrv oaı om.Yş  2'şer artarak
print(msj[::1]) #benim adım Serdar ve soyadım Tohma. Yaşım ise 36.
print(msj[::-1]) #.63 esi mışaY .amhoT mıdayos ev radreS mıda mineb

#kizim = "Hayat"
#print(kizim[-1]) #tersten aldı. çıktı: t
#print(kizim[0]) #H
#print(len(kizim)) #karakter sayısı bulma. çıktı: 5
