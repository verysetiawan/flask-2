from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    
    return "<h1>Hallo Flask Python</h1> <br> <h3>Selamat datang di website flask sederhana</h3>"

if __name__ == "__main__":
    app.run (debug=True)