# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 
def lcm(num1,num2):  # girilen rakamlarin ekokunu alan bir fonksiyon yazilmis ismi lcm
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications)



# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html", methods=["GET"]) # burada get methodu uygulandi yani 
       # yani sadece karmisizda bir site yada sayfa gorecegiz 
       # ama post methodunda gelen sayfa bazi degerler isteyecek bizden ve biz bazi degerler girecegiz
       #  server ise bize girilen degerler sonucu bir sonus dondurecek buda post methodu 




# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST": # post islemi uygulanacak 
        num1 = request.form.get("number1") # posr isleminde degerlerin girilmesi icin request kullanilmali 
        num2 = request.form.get("number2") # degerleri kutucuklardan cekecek ve hesaplayip bir deger donecek
        return render_template("result.html", result1 = num1, result2 = num2, lcm = lcm(int(num1),int(num2)), developer_name = '')
    else:   # result1 ve result2 bizim girdigimiz degerler .result htmle bakip result1 result2 ve sonuc gorulebilir
        return render_template("result.html", developer_name = "polat")
       # degerler girilmez ve bir post islemi yapilmaz isze else calisacak.sen sadece get request yapmis oldun
# Add a statement to run the Flask application which can be debugged.
if __name__== "__main__":
     app.run(debug=True)
     #app.run(host='0.0.0.0', port=80)

     # fonk calistirmak icin  sondan bir onceki satiri yorumdan cikar 
     # uygulamanin ana sayfasini cagirdik ve iki kutucuk gormus olduk yani get methodu uygulanmis olduk
     # simdi gelen kutucuklara degerler girelim , bu adimda post methodu yapiyoruz artik deger girerek
     # degerler girildi hespla tusuna basildi sonuc goruldu
     # girilen degerler result edildi sonra lcw fonsiyonunda isleme alindi ve sonuc lcw diye dondu
     # get methodu yapmadan direk post methodu uygulamamz . ana sayfa cagirilmadan direk calc sayfasinicagirdigimizda hata alacagis 
     # cunku clac islemi ilk  sayfada ilk html icinde o cagirilmada degerlerin girilecegi kutucuklar gorulemeyecek
     # video 1.41 dakikasina bakilabilir 

     # son satiri yorumdan cikar ve bir ust satiri yorum yap

     # ve handling forms a baslayalim