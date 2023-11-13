website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1  - ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerinin silin

result = ' Hello World '.strip()
result= ' Hello World '.lstrip()#soldaki boşluğu siler
result= ' Hello World '.rsplit() #sağdaki boşluk
print(result) 

#2 - 'www.sadikturan.com' içindeki sadıkturan bilgisi  haricindeki her karakteri silin
silme='www.sadikturan.com'
replace= silme.replace('www.','').replace('.com','')
print(replace)

silme2='www.sadikturan.com'.strip('w.moc')
print(silme2)

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın
result=course.lower()
result=course.title()
#  4 - 'website ' içerisinde kaç tane a karakteri var (caunt('a'))
result=website.count('a')
# 5 - 'website' www ile başlayıp com ile bitiyor mu
result=website.startswith('www')
result=website.startswith('htt')
result=website.endswith('com')
## 5 - 'website' içinde com ile bitiyor mu
result=website.find('com')
result=website.find('com',0,10)#0 ile 10 arasında com var mı
result=course.find('Python') # 0 yazar başladığı index
result=course.rfind('Python')#26
#6- 'website' içinde com ifadesi  var mı
result=website.index('com')
result=website.rindex('com')
# 7- 'course ' içindeki karakterlerin hepsi alfabetik mi(isalpha,isdigit)
result=course.isalpha()
result=course.isdigit()
result='hello'.isalpha()
# 8-  'contens' ifadesini satırda 50 karakter içine yerleştir sağ ve soluna ekleyin
result='contens'.center(50,'*')#*********************contens**********************
result='contens'.ljust(20,'*')
result='contens'.rjust(50,'*')
# 9- 'course '  kkarekter dizisindeki tüm boşlukları '- ile değiştirin'
result=course.replace(' ','-')
#10-'Hello World' karaekter dizisinini 'World'  ifadesini 'there' olarak değiştirin

result='Hello World'.replace('World', 'there')
# 11 'course' karakter dizisini  boşluk karakterlerinden ayırın

result=course.split(':')#['Python Kursu', ' Baştan Sona Python Programlama Rehberiniz (40 saat)']
result=course.split(' ')#['Python', 'Kursu:', 'Baştan', 'Sona', 'Python', 'Programlama', 'Rehberiniz', '(40', 'saat)']

result=result[2]#'Baştan'









print(result)









