from flask import Flask
from parsing1 import values_count

app = Flask(__name__)

@app.route("/")
def index():
    #return "Поднял локальный сервер на Flask"
    return values_count

if __name__ == "__main__":
    app.run(port=5000, debug=True)