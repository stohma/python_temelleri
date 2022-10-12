# identity operator: is

# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x == y) #True
# print(x == z) #True
# print(( x is y)) #True
# print(x is z) #False

# x = [1, 2, 3]
# y = [2, 4]
# del x[2]
# y[1] = 1
# y.reverse()

# print(x == y) #True elemanlar aynı olduğundan True çıktısını verdi
# print(x is y) #False elemanlar aynı olsa da aynı sırada olmadığından False verdi
# print(x is not y) #True soru tersten sorulduğu için True çıktısını verdi. tıpkı != mantığındaki gibi


# membership operator: in
# x = ["apple", "banana"]
# print("banana" in x) #True
#
# name = "Ece"
# print("e" in name) #True e harfi Ece'de var mı sorusuna cevap
# print("a" not in name) #True :) a Ece'de yok değil mi