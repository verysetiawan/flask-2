from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    nilai = 100
    #perulangan
    angka = [1,2,3,4,5,6,7,8,9,10]
    return render_template("index.html", value=nilai, angka=angka)

if __name__ == "__main__":
    app.run (debug=True)