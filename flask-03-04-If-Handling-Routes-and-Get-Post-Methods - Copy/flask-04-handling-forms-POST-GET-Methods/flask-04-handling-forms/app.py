# Import Flask modules
from flask import Flask, redirect, url_for, render_template, request # ayni kutuphaneler
 # reande teamlete= html , redirect ve url-for = baskabir url adresine yonlendime var 
 # reques = kutucular ve hesaplama var demektir
# Create an object named app
app = Flask(__name__)


# Create welcome page with main.html file and assign it to the root path
@app.route('/')
def home():
    return render_template('main.html', name='polat')
  # ana sayfa , name degiskeni ve atanan deger var  main htmal  iceriginebakilabilir 

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised

@app.route('/greet', methods=['GET']) # get methodu
def greet(): 
   if 'user' in request.args:  # burada bir arguman kullanilmis user ile 
        usr = request.args['user']
        return render_template('greet.html', user=usr)
   else:
        return render_template('greet.html', user='Send your user name with "greet?user=xxxxx" param in query string')
   # bu sayfa query string yapisi ile cagirilmali ve user degiskeni kullanilmali
# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')
@app.route('/login', methods=['GET', 'POST']) # get ve post kullanilacak
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        if password == 'clarusway':  # dogru girildiginde secure.html 
            return render_template('secure.html', user=user_name.title()) # title girilen paswortun bas harflerini buyuk geri kalani kucuk yazacak
        else: # yanlis girildiginde login.html calisacak
            return render_template('login.html', user=user_name.title(), control = True)
    else:
        return render_template('login.html', control = False)
   # pst islemi yapilmazsa bu else calisacak 
# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)



    # url-structure 
    # http -protokol ,  80 - http port calistigi port , 
    # search  yani path bunlar ara sayfalar 
    #query string sayfaya bagli olan ek sayfalar ve bunlarda argumanlar ile ifade edilir
    # ornek olarakta var olan bir konu ve bu konuya bagli makaleler olabilir 

    # login sayfasinda neler oluyor 
    # post uygulanacak yani kutucuklar gelecek ve bir username ve password girecegiz
    # dogru girdigimizde yani clarusway girildiginde if blogu calisacak degilse else blogu calisacsk 
    # if calistiginda secure.html calisacak ... secure html icerigine bakilabilir 


    # calistirma ana sayfayi gor 
    # greet sayfasini once greet olarak  cagir else blogunun geldigini gor , bu uyari mesajidir 
    # daha sonra  greet?user=polat diye cagiralim , simdi greet.html geldi

    # login pathi gidelim karsimiza kutucuklar gelecek get ve post islemleri uygulanacak 
    # post yaptigimizda if blogu devreye girecek
    # degerleri girelim name-polat password-clarusway  dogru degerler girildiginde  secure.html karsimiza gelecek
    # pasword yanlis girildiginde uyari yazisi gelecek ..yani login.html gelecek ..paswort yanlis tekrar dene diyor
    #simdide direk login sayfasini direk cagirmaya calisalom post yapmadan yani arma cubuguna direk /login yazalim
    # yazi vsr gelmez  sadece ana sayfa gorulur 


    # son satiri ac sondan bir onceki satiri yorum satiri yap 

    # tum py dosyalarini kontrol et ..son satir yorumdan ciktimi
    # isimlerin degismesi gereken yerler degissin githuba kendi ismimiz ile gitsin
     
     # hersey hazir .. simdi git push islemi yapalim
     # git bash terminali ac - dogru dosyada olup olmadigini kontrol et awsporjekt klasorunde 
     # git add .  - git commit -m "flask03-04 added"  - enter - ve git push
     # git hubu kontrol edelim gelmismi diye 
    

    # aws konsollari acalim
    # 1 instance olusturalim   klasik instance ayni ozelliklerde 
    # makinaya baglanalim - icine gir -connect - ssh -i vsr
    # sirasi ile asagidaki islemleri yapalim
    #sudo yum update -y
    #python3 --version
    #sudo yum install python-pip
    #pip3 list  flask olup olmadigini kontrol edelim
    #sudo pip3 install flask  , flask yukleyelim
    #sudo yum install git , git kurulumu yapalim
    #sudo git clone ve devamina githubdan repomuzun url adresini ekleyelim awsprojekt reposunun url adresi
    # awsprojekt reposuna gir ve urli kopyala 
    # ls yapip reponun geldigini gor 
    # cd ile clonlana repoya giris yap 
    # instance  bilgileri repodan aliyor vscoddan sadece takip yapiyoruz ec2 nun vscod ile bir ilgisi yok
    # cd ile flask-03-04 klasorune giris yapalim
    # ls ile dosyalari gorelim
    # cd flask-03 dosyasina gecis yapalim
    # cd flask_if_for    klasorune gecis yapalim
    # dizin olarak app-py ile ayni dizindeyim artik calistirabilirim
    # sudo python3 app.py komutu ile dosyami calistirabilirim
    # sanal makinanin puplig ipsini alip calisip calismadigini bakalim 
    # local host portlarin kapali olmali 
    # cat app.py ile son satirlar kontrol edilebilir ve  vim veya nano editorleri ile degisiklik yapilabilir 
    # sirayla dosyalari dolasip calistirma islemini yapabiliriz
