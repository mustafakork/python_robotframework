website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1 - 'course' karakter dizisinde kaç karakter bulunmaktadır
length=len(course)
print(len(course))
#2-'website içinden www karakterlerini alın.'
print(website[7:10])#www
#3- website içerisinde  com karakterlerini alın
print(website[len(website)-3:len(website)])  #  com 
print(website[-3:])  #  com


print("=====================================")

# course  içerisinden ilk 15 ve son 15 karakterleri alın
print(course[0:15])
print(course[length-15:length])#
print(course[-15:]) 

# course terten yazdırma
print(course[::-1])  #tersten Yazdırma
s='12345'*5
print(s)#1234512345123451234512345  5 kere yan yana yazar
print(s[::5])
print(s[0:10:2])

name='Bora'
surnama='Yılmaz'
age=32
job="Mühendis"

print(f'\'Benim adım {name} {surnama}, yasim {age} ve Mesleği {job}\'')#'Benim adım Bora Yılmaz, yasim 32 ve Mesleği Mühendis'
print('Benim adım {} {}, yaşım {} ve mesleğim {}'.format(name,surnama,age,job))#Benim adım Bora Yılmaz, yaşım 32 ve mesleğim Mühendis