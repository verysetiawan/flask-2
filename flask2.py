from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    nilaiku = 100
    return render_template ("index.html", variabelbaru=nilaiku)

if __name__ == "__main__":
    app.run (debug=True)