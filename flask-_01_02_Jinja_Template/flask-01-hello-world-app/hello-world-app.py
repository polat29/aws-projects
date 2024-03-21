from flask import Flask 
app = Flask(__name__)

@app.route("/") # ana sayfayi temsil eder
def head ():
     return "hello word ramazan"
@app.route("/secondpage")
def second():
     return "this is second page"

@app.route('/fourth/<string:id>')
def fourth(id):
     return f'Id of this page is {id}'





if __name__ == '__main__':

    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)