ad = "Hayat"
soyad = "Tohma"
yas = 9
#print("My name is {}".format(ad)) #My name is Hayat
print("My name is {} {}".format(ad,soyad)) #My name is Hayat Tohma
print("My name is {1} {0}".format(ad,soyad)) #My name is Tohma Hayat
print("My name is {n} {s}".format(n=ad,s=soyad)) #My name is Hayat Tohma
print("My name is {} {}. I'm {} years old.".format(ad,soyad,yas)) #My name is Hayat Tohma.  I'm 9 years old.

number = 200 / 700
print("the result is {}".format(number)) #the result is 0.2857142857142857
print("the result is {n:1.3}".format(n=number)) #the result is 0.2857142857142857 #the result is 0.286  noktadan sonra 3 basamak al
print("the result is {n:1.2}".format(n=number)) #the result is 0.29   1 ise soldan yer tutucu yani karakter aşağıdaki örnekte 10 boşluk olması gibi
print("the result is {n:10.2}".format(n=number)) #the result is       0.29

#f string
print(f"My name is {ad} {soyad} and I'm {yas} years old.") #My name is Hayat Tohma and I'm 9 years old
