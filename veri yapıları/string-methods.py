msg = "Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma"
#sonuc = msg.upper() #PYTHON KURSUMUZA HOŞ GELDINIZ. BEN SERDAR TOHMA
# sonuc = msg.lower() #python kursumuza hoş geldiniz. ben serdar tohma
# sonuc = msg.title() #Python Kursumuza Hoş Geldiniz. Ben Serdar Tohma
# sonuc = msg.capitalize() #Python kursumuza hoş geldiniz. ben serdar tohma
# sonuc = "abc".islower() #True
# sonuc = "    abc ".strip() #önden ve arkadan boşluğu kırpar  abc
# sonuc = msg.split() #['Python', 'Kursumuza', 'Hoş', 'Geldiniz.', 'Ben', 'Serdar', 'Tohma']
# print(sonuc[3]) #Geldiniz.
# sonuc = msg.split(".") #['Python Kursumuza Hoş Geldiniz', ' Ben Serdar Tohma']  noktadan itibaren ayırır
# sonuc = msg.split(".") 
# sonuc = "-".join(sonuc) #Python Kursumuza Hoş Geldiniz- Ben Serdar Tohma  birleştirme yapar
# print(sonuc)
# index = msg.index("Hoş") # print(index) #17. index'e denk geldiğini buluruz
# sonuc = msg.startswith("P") #True
# sonuc = msg.startswith("A") #False
# sonuc = msg.endswith("a") #True
# sonuc = msg.replace("Serdar","Hayat") #Python Kursumuza Hoş Geldiniz. Ben Hayat Tohma
# sonuc = msg.replace(" ","-").replace("ş","s").replace(".","") #Python-Kursumuza-Hos-Geldiniz-Ben-Serdar-Tohma
sonuc = msg.lower().replace(" ","-").replace("ş","s").replace(".","") #python-kursumuza-hos-geldiniz-ben-serdar-tohma

print(sonuc)