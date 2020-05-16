from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    #menambahkan nilai/variabel 
    nilaiku = 100
    #menambahkan looping
    hari = ("senin","selasa","rabu","kamis","jumat","sabtu","minggu")
    #conditioning if else
    statushari = "minggu" #jika hari adalah minggu maka libur, selainya kerja
    return render_template ("index.html", var1=nilaiku, var2=hari, var3=statushari)

if __name__ == "__main__":
    app.run (debug=True)