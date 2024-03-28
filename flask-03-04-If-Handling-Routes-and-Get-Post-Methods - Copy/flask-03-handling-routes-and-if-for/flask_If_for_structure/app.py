# Import Flask modules
from flask import Flask, render_template # from flask demis demekki flask kullanacak , ornek kutuphane render teamplete
# Create an object named app   # ana giris kismi burasidir kullanilacak kuruphaneler burada gorulur 
app = Flask(__name__) #  burasi ana satir , burada app adinda bir nesne olusturuluyor

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route("/") # / ile baslayan kisin uygulamanin ana sayfasi oluyordu
def head():   # @app rout ile baslayan ve ile return ile biten yerler  arasi ise uygulamanin ekran sayfalari oluyor
    first="This is my first conditions experience"
    return render_template("index.html",message=first) # eger bir html dosyasi calistirmak istiyorsam render temalete kullanmaliyim
# calistirmak icinde bir teamplete dosyasi olusturup dosyalari buraya koymamiz gerekiyordu
#html dosyasi icinde bir message satiri var ve bu bir degiskene atanmis  massage degiskeni 
 #first degerini dondurecek yoksa  index.htmldeki  else blogu calisacak
# Create a function named header which prints numbers elements of list one by one in `index.html` 
# and assign to the route of ('/')
@app.route("/list") # ikinci list isimli sayfamiz 
def header():
   # names =["tom", "osvaldo", "guile", "tommy"] # names listesi olusturulmus 
    numbers = range (1,11) #numbers isimli bir liste olusturuldu
    return render_template("body.html", object = numbers) # list ismli sayfada krsimiza body html geleck 
# body.html icinde bir for dongusu var ve bu dongude suslu parantez icinde bir x var . yani bir degisken kullanilmis
# objekt degisskenine once numbers daha sonrada names i atayip ne sonuc verdigini gorecegiz
# run this app in debug mode on your local.
if __name__== "__main__": # ana satirda (4) te olusturulan nesne burada kontrol edilecek
    app.run(debug=True)   # burasi ise dosyanin calistirilma satirlaridir default 5000 protunds calisir
    #app.run(host='0.0.0.0', port=80) # instance icinde calistirmk icin ihtiyacimiz olan port
#  zaten sec grouptada 80 portunu acmistik
 
 # lokalde  calisturmak icin lokal satirini yorumda cikarmamiz gerekecek 
 #  ilk sayfamizi caalistiralim ve first="This is my first conditions experience" geldigini gorelim
 # bu zaten atanan degerdi 
 #simdi return render_template("index.html", message=first)  satirindaki message kismini ve degerini silelim 
  # ve index.html deki else blogunun geldigini gormeye calisalim
    # degistir - kaydet - ve programi durdurup yeniden calistir  ctrl-c durdur
    # neden yazi degisti cunku elif blogu calismadi oda else gitti

    # simdi list isimli dosyaya gecis yapalim ve  ekrani goruntuleyelim for dongusu calismasini incele
    # sindi objek degiskenine numbers degilde names leri atayalim
    # yani # names =["tom", "osvaldo", "guile", "tommy"]  satirini aktif hale getirelim ve  numbersi yoruma lalim
    # degisiklikleri kaydedip tekrar calistiralim ve sayfayi yenileyip degisikligi gorelim
    # bu dosya ile isimiz bitti bu dosya githuba push etmeden once lokali kapatim son satir aktif hale getirilmeli
