# a = 5
# b = 10
# c = 20 veya

a, b, c = 5, 10, 20 #5 10 20

# a, b = b, a #10 5 20

a += 5 # veya a = a + 5 #çıktı 10 10 20
a -= 5 #a = a - 5
a *= 5 #a = a * 5
a /= 5
a %= 5
a **= 5
a //= 5

# print(a,b,c) 

# values = 1, 2, 3 #(1, 2, 3)
# values = (1, 2, 3)
# a, b, c = values
# print(a, b, c) #1 2 3

# values = (1, 2, 3, 4, 5, 6)
# a, b, *c = values #1 2 [3, 4, 5, 6]
values = (1, 2, 3, 4, 5, 6)
a, *b, c = values #1 [2, 3, 4, 5] 6

print(a, b, c)


# sonuc = values

# print(sonuc)

