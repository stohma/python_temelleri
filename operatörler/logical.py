# yaş >= 18 ve (mezuniyet == "lise" ya da mezuniyet == "üniversite")

x = 10

#1- And Operatörü (ve)
# sonuc = 5  < x < 15 #True
sonuc = (x > 5) and (x < 15) 
#True ve True => True bütün koşullar True olmalı ki sonuç True olsun
#False ve True => False
#False ve False => False

hak = 3
devam = "e"
# devam = "h" #"e" değerinden başka değerler için False sonucunu verir. veya hak 0 olsa False

sonuc = (hak > 0) and (devam == "e") #True
# sonuc = (hak > 0) and (devam == "e") #False

#2 Or Operatörü

(x > 0) #sayı pozitif
(x % 2 == 0) #sayı çift
sonuc = (x > 0) or (x % 2 == 0) #koşullardan birinin doğru olması sonucu True olarak yazdırır

#3- not operatörü

sonuc = x > 0 #True
sonuc = not(x > 0) #False

# x, 5-10 arasında bir çift sayı mı?
sonuc = ((x > 5) and (x < 10)) and (x % 2 == 0) #10 değeri veya tek değerler için False. 

print(sonuc) 