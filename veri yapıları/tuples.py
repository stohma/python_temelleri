_list = [1,2,3]
_tuple = (1,2,3)

print(type(_list)) #<class 'list'>
print(type(_tuple)) #<class 'tuple'>

print(_list[1]) #2
print(_tuple[1]) #2

print(len(_list)) #3
print(len(_tuple)) #3

_list[0] = 5
# _tuple[0] = 5 #TypeError: 'tuple' object does not support item assignment değiştirilemez özelliğinden dolayı veri atamayı kabul etmez

_list.append(3) 
# _tuple.append(3) #AttributeError: 'tuple' object has no attribute 'append' tupple'a append özelliği gelmez
print(_tuple.count("iki")) #0

_t = tuple([3,4,5])
print(type(_t)) #<class 'tuple'>
print(_t) #(3, 4, 5)

print(_list)
print(_tuple)