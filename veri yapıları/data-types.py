#int
#float
#string
#bool

"""
x = int(input("x: "))
y = int(input("y: ")) #terminalde istediğimiz sayı veya değeri girebiliriz

print(type(x)) #<class 'int'>
print(type(x)) #<class 'int'>

toplam = x + y
print(toplam)
"""

age = 5
weight = 12.5
name = "Serdar"
isStudent = True

print(type(age)) #<class 'int'>
print(type(weight)) #<class 'float'>
print(type(name)) #<class 'str'>
print(type(isStudent)) #<class 'bool'>

# int to float (int'ten float'a çevirme)
result = float(age) 
print(result) #5.0
print(type(result)) #<class 'float'>

# float to int
result = int(weight)
print(result) #12 kendi ondalığına yuvarlar
print(type(result)) #<class 'int'>

# bool to str
result = str(isStudent)
print(type(result)) #<class 'str'>

isStudent = False
print(isStudent) #False ama bu str olan False

#bool to int
result = int(isStudent)
print(result) #0 False'ın karşılığı
print(type(result)) #<class 'int'>
#True == 1

'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)

'''
"""
pi = 3.14
r = float(input("yarıçap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r


result = "alan: " + str(alan) + " cevre: " + str(cevre) #cevre'den önce de boşluk bırakıyoruz
print(result)
"""
'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''
print("gidilen yol")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)

print(str(mesafeKm) + " km =" + str(mesafeMil) + " mil.")