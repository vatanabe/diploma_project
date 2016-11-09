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
    result = "<table><tr><th>Продукт</th><th>Количество</th><th>На складе</th><th>Наличие</th></tr>"
    for name in values_count1:
        if values_count1[name] <= amount1(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (search1(name), values_count1[name], amount1(name), availability)
    result += "</table>"
    return result

@app.route("/2")
def second():
    result = "<table><tr><th>Продукт</th><th>Количество</th><th>На складе</th><th>Наличие</th></tr>"
    for name in values_count2:
        if values_count2[name] <= amount2(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (search2(name), values_count2[name], amount2(name), availability)
    result += "</table>"
    return result

@app.route("/3")
def third():
    result = "<table><tr><th>Продукт</th><th>Количество</th><th>На складе</th><th>Наличие</th></tr>"
    for name in data:
        if values_count2[name] <= amount3(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (search3(name), data[name], amount3(name), availability)
    result += "</table>"
    return result

if __name__ == "__main__":
    app.run(port=5000, debug=True)