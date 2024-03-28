#Import Flask modules
from flask import Flask, redirect, url_for, render_template # yeni kutuphaneler eklenmis redireck url-for

#Create an object named app 
app = Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')
@app.route("/") # ana sayfamiz
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>' 
  # karsimiza gelecek olan sey return un devamindaki yapi


# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')
@app.route('/about') # ikinci sayfa 
def about():
    return '<h1>This is my about page </h1>'
 #

# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')
@app.route('/error') # hata sayfasi ekranda sen yetkili degilsin yazisi gorulecek
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'



# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')
@app.route("/admin") # adin sayfasina gitmek istedigimizde bizi eror sayfasina yonlendirecek . 
def admin():  # cunku admin sayfasi cok yetkili bir sayfa 
    return redirect(url_for('error')) # sen admin degilsin burada ne isin var diyecek
    # bunuda redireck kutuphanesi saglamis olacak

# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')
@app.route('/<name>') # html sayfasini teamplet ile kullanabilirken direk kendinide kod bloklari arasinda kullanabiliriz
def greet(name):
    greet_format=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name }!<h1>
    <h1>Welcome to my Greeting Page</h1>
</body>
</html>
    """
    return greet_format




# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')
@app.route('/greet-admin') # edmimi selamla sayfasi bir ustteki sayfaya yonlendirilmis olacagiz
def greet_admin():  # name degiskenine dikkat edersek iki taraftada kullanildi
    return redirect(url_for('greet', name='Master Admin!!!!'))




# Rewrite a function named greet which uses template file named `greet.html` under `templates` folder 
# and assign to the dynamic route of ('/<name>'). 
# Please find a template html file named `greet.html` which takes `name` as parameter under `templates` folder 


# @app.route('/<name>')
# def greet(name):
#     return render_template('greet.html', name=name)



# Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10'). 
# Please find a template html file named `list10.html` which shows a list counting from 1 to 10 under `templates` folder 
@app.route('/list10')
def list10():
    return render_template('list10.html') # render teamlete kullanmis demmkekki html kullanacak
 # flask -03-handlinge baktigimizda list10.html gorulebilir
 # bir for dongumzvar ve bu  dongudeki sayilari sirayla ekrana yazilacak 

# Create a function named evens which show the even numbers from 1 to 10 within `evens.html` 
# and assign to the route of ('/evens'). 
# Please find a template html file named `evens.html` which shows a list of even numbers from 1 to 10 under `templates` folder 
@app.route('/evens')
def evens():
    return render_template('evens.html') # reander teamplete html 
  # html de bir for dongudu var ve range ile olusturulan sayi listesinden 2 ye bolonenleri yazacak


# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__== "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)

    # lokalde calistirabilmek icin son satiri yoruma  alalim , degisiklikleri kaydedelim ve calistiralim
    # ana sayfayi gor 
    # ikinci sayfa about a bak
    #error sayfasina bak
    # admin sayfasina gitmeye calisalim ve bir hata alalim  ve error sayfasinin geldigini gorelim
    # 302 hatasi aldik asagida gorulebilir , yonlendirme oldugu icin bu hata alindi .302 hatalari sinavlarda cikiyor
    # name sayfasini gormek icin herhangi bir isism yaz sayfa kismina herkes kendi isimini yazabilir 
    # name diye bir degiskene atandigi icin bu sekide calismis oldu
    # html blogu icerisindeki name degiskenini gorebiliriz

    # greet admin sayfasina gidip sayfanin yonlendirildigini gorebiliriz .
    # bu sefer kendi ismimiz degilde degiskene verilen degerl yansitildi

    # list10 sayfasini kontrol edelim 
    # bir for dongusunun nasil calistigini gorelim

    # evens sayfasinda cift sayilarin ekrana grldigini gorelim . render teamlete evens.html i kullanacak

    # durdur son satiri yorumdan cikar bir ust satiri yoruma al