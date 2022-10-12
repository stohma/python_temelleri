# x = 10
# y = 20
#
# if (x > y):
#     print(" x, y den büyük.")
# else:
#     print("y, x den büyüktür.") #y, x den büyüktür.

# x = 20
# y = 20
#
# if (x > y):
#     print(" x, y den büyük.")
# elif (x == y):
#     print("x, y ye eşit") #x, y ye eşit
# else:
#     print("y, x den büyüktür.") # y, x den büyüktür. her 2 sayı eşit olmasına rağmen bu çıktı veriyor. bunun için elif kullanırız

sayi = int(input("sayı: "))

if sayi > 0:
    print("sayı pozitif")
elif (sayi == 0):
    print("sayı sıfır")
else:
    print("sayı negatif")