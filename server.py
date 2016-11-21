from flask import Flask, render_template
from parsing1 import values_count1
from parsing2 import values_count2
from parsing3 import data
from product_search import search1, search2, search3
from product_amount import amount1, amount2, amount3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="ТЫРЫПЫРЫ")

@app.route("/1")
def first():
    return render_template('1.html', title="OMG", values_count1=values_count1, amount1=amount1, search1=search1)

@app.route("/2")
def second():
    return render_template('2.html', title="MIN_DESIGN", values_count2=values_count2, amount2=amount2, search2=search2)
    
@app.route("/3")
def third():
    return render_template('3.html', title="OPT_LOCAL_MIFARE", data=data, amount3=amount3, search3=search3)

if __name__ == "__main__":
    app.run(port=5000, debug=True)