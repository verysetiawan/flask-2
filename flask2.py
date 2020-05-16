from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    #menambahkan nilai/variabel 
    nilaiku = 100
    #menambahkan looping
    hari = ("senin","selasa","rabu","kamis","jumat","sabtu")
    return render_template ("index.html", variabelbaru=nilaiku, variabelhari=hari)

if __name__ == "__main__":
    app.run (debug=True)