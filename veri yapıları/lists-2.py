diller = ["Python","C#","Java","Javascript","React"]
sonuc = diller #['Python', 'C#', 'Java', 'Javascript', 'React']
sonuc = type(diller) #<class 'list'>
# sonuc = diller[:2] #['Python', 'C#']
sonuc = diller[2:] #['Java', 'Javascript', 'React']
sonuc = diller[-1] #React
sonuc = diller[-4:-1] #['C#', 'Java', 'Javascript']
# diller[0] = "Html"
# sonuc = diller #['Html', 'C#', 'Java', 'Javascript', 'React']
diller[-1] ="Html"
sonuc = len(diller) #5
sonuc = diller + ["Angular", "Vuejs"] #['Python', 'C#', 'Java', 'Javascript', 'Html', 'Angular', 'Vuejs']  ekleme yapma

# if bloğu => koşul ifadeleri
if "Python" in diller:
    # print("evet") #evet  dizin içerisinde arama yapma
    print("değer listenin bir elemanı") #değer listenin bir elemanı

# döngüler
# print(diller[0]) #Python
# print(diller[1]) #C#
# print(diller[2]) #Java
# print(diller[3]) #Javascript veya
for x in diller:
    print(x) #Python C# Java Javascript Html

del diller[0] # eleman silme. hangi numaradaki elemanı silmek istersek onu del ile silebiliriz.

sonuc = diller #['C#', 'Java', 'Javascript', 'Html']

print(sonuc)