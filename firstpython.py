"""
Ekrana teknoloji sohbetleri yazdırıyorum.
print("Teknoloji Sohbetleri!")
"""
"""
a = 5
b = 5.3
c = "Python"

print(type(a))
print(type(b))
print(type(c))
"""

"""
a = "5"

print(type(a))
"""

"""
    + 
    -
    *  -> çarpma
    ** -> üs alma
    /  -> bölme
    // -> tam bölme
    %  -> bölümünde kalan(mod)
"""
"""
print(4*3)
"""
"""
a = 4
b = 3
c = a*b
print(c)
"""
"""
print(3**2)
"""

"""
print(8//3)
"""
"""
a = "python"
b = "C++"

print(a + b)
"""

"""
a = "5"
b = "4"

print(a + b)
"""

"""
a = 5
b = "4"
b = 4

print(a + b)
"""
"""
a = 5
b = "4"
b = int(b)
print(a + b)
"""
"""
a = "Python"
print(int(a))
"""
"""
a = 5

print(float(a))

"""
"""
a = 5
b = 3
a = str(a) #"5"
b = str(b) #"3"
print(a + b)
"""

"""
isim = input("Isminizi giriniz:")

print(isim)
print(type(isim))
"""

"""
yas = int(input("yasinizi giriniz:")) #"22" -> 22

print(yas + 2)
"""

"""
print(3*(5+4))
"""

"""
If elif else
    > -> büyüktür
    >= -> büyük eşittir
    < -> küçüktür
    <= -> küçük eşittir
    == -> eşit midir
    != -> eşit değil midir
"""

"""
yas = int(input("yasinizi giriniz:"))

if(yas > 20):
    print("yasin 20'den büyük")
    print("******")


print("Kodum burada bitti.")
"""

"""
yas = int(input("yasinizi giriniz:")) #21

if(yas > 20):
    print("yasin 20'den büyük")
    print("******")
else:
    print("Yaşın 20'den küçük")


print("Kodum burada bitti.")
"""
"""
instagram
"""

"""
kullanici_adi = "deneme"
sifrem = "123456"

girilen_kullanici_adi = input("Kullanici adiniz:")
girilen_sifre = input("Sifreniz:")

if(kullanici_adi == girilen_kullanici_adi and sifrem == girilen_sifre):
    print("Başarıyla giriş yapıldı.")
elif(kullanici_adi != girilen_kullanici_adi and sifrem == girilen_sifre):
    print("Kullanıcı adı yanlış")
elif(kullanici_adi == girilen_kullanici_adi and sifrem != girilen_sifre):
    print("Şifreniz yanlış")
else:
    print("Kullanıcı adınız ve şifreniz yanlış")

print("******")
"""

"""
yas = int(input("Yasinizi giriniz:")) #40

if(yas > 10):
    print("yaşın 10'dan büyük")

if(yas > 20):
    print("yaşın 20'den büyük")

if(yas > 30):
    print("yaşın 30'dan büyük")

"""

"""
yas = int(input("Yasinizi giriniz:")) #40

if(yas > 10):
    print("yaşın 10'dan büyük")
elif(yas > 20):
    print("yaşın 20'den büyük")
elif(yas > 30):
    print("yaşın 30'dan büyük")
"""

"""
yas = int(input("Yasinizi giriniz:")) #40

if(yas > 30):
    print("yaşın 30'dan büyük")
elif(yas > 20):
    print("yaşın 20'den büyük")
elif(yas > 10):
    print("yaşın 10'dan büyük")

"""
"""
a = True
b = False

if(b):
    print("hello world")
elif(a):
    print("world hello!")
"""

"""
BBM333
1 Vize -> %40
1 Final -> %50
1 Ödev -> %10

50 altı kalır
50-55 zorunlu geçme D
55 üstü geçer
"""

"""
print("----BMM333 Geçme Kontrol Uygulaması----")
vize = float(input("Vize notunuz:"))
final = float(input("Final notunuz:"))
ödev = float(input("Ödev notunuz:"))

ortalamam = ((vize*0.4) + (final*0.5) + (ödev*0.1))

if(ortalamam >= 55):
    print("Tebrikler Geçtiniz")
elif(50 < ortalamam < 55):
    print("Zorunlu geçer")
else:
    print("Kaldınız")

"""
