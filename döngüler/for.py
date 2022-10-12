# sayilar = [1, 2, 3, 6, 8, 9, 15]
# for i in sayilar:
#     print(i)
#
# for i in  sayilar:
#     print("merhaba")


# isimler = ["ali", "ece", "gamze"]
# for isim in  isimler:
#     print(isim)


# isim = "serdar tohma"
# for a in isim:
#   print(a)

# _tuple = [(1, 2), (4, 5), (6,7)]
# for a in _tuple:
#     print(a)
#
# _tuple = [(1, 2), (4, 5), (6,7)]
# for a,b in _tuple:
#     print(a,b)

_dict ={"k1": 1, "k2": 2, "k3": 3}
for a in _dict:
    print(a)
for a in _dict:
    print(_dict [a])

for a in _dict.values():
    print(a)

for key,value in _dict.items():
    print(key,value)