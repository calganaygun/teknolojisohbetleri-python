# print("Merhaba\nDünya")
# print("Selam")
"""
ogrenciler = ['Ahmet','Mehmet','Ali']
print(ogrenciler)
ogrenciler[0]="Çalgan"
print(ogrenciler)
"""

# liste = [1,5,7,9,15]
# print(liste)
# print(liste[1:4])
# kucukliste = liste[1:4]
# print(kucukliste)
# print(liste[len(liste)-1])
# print(liste[-1])
"""
liste = [1,5,7,9,15]
print(liste)
liste2 = list(liste) list.copy()
liste2[0]=9
print(liste)
print(liste2)
"""
"""
liste = [1,2,3,4,5,6,7,8,9]
print(liste[::-1])
"""
"""
yazi = "Merhaba YouTube!"
print(yazi[::-1])
"""

# iller = ["Ankara","İstanbul","İzmir","Aydın"]
# iller2 = ['Yozgat',"Sivas"]
# print(iller)
# iller = iller + iller2
# iller.extend(iller2)
# iller.insert(1,"Konya")
# iller.remove("İzmir")
# iller.reverse()
# print(list(reversed(iller)))
# print(iller.pop(0))
# iller.sort()
# iller.clear()
# print(iller)
"""
a = 0
while a<3:
    print(a)
    a += 1
"""
"""
while True:
    cevap = input("Yapmak istediğiniz işlem?\n")
    if cevap == "q":
        break
    elif cevap == "Topla":
        ilksayi = int(input("Birinci sayı: "))
        ikincisayi = int(input("İkinci sayı: "))
        print(ilksayi + ikincisayi)
"""
"""
x=1
while x<=10:
    print(x)
    x += 1
x==5
x=="q"
x>5
"""

# liste = ["a","b","c","d"]
# yazi = "Merhaba"
"""
for i in range(1,20):
    if i%2==1:
        print(i)
"""
ogrenciler = []
while True:
    islem = input("""1-Ogrenci Ekle
2-Ogrenci Listele
3-Çıkış
    """)
    if islem == "1":
        ogrenci = input("Ogrenci ismi: ")
        ogrenciler.append(ogrenci)
    elif islem == "2":
        """for ogrenci in ogrenciler:
            print(ogrenci)"""
        print(*ogrenciler,sep="\n")
    elif islem == "3":
        break
    else:
        print("Hatalı işlem yaptınız.")

















