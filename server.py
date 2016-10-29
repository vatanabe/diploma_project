from flask import Flask
from parsing1 import values_count
from parsing2 import values_count2
from parsing3 import data

app = Flask(__name__)

@app.route("/1")
def first():
    result = "<table><tr><th>Продукт</th><th>Количество</th></tr>"
    for name in values_count:
        result += "<tr><td>%s</td><td>%s</td></tr>" % (name, values_count[name])
    result += "</table>"
    return result

@app.route("/2")
def second():
    result = "<table><tr><th>Продукт</th><th>Количество</th></tr>"
    for name in values_count2:
        result += "<tr><td>%s</td><td>%s</td></tr>" % (name, values_count2[name])
    result += "</table>"
    return result

@app.route("/3")
def third():
    result = "<table><tr><th>Продукт</th><th>Количество</th></tr>"
    for name in data:
        print (name)
        result += "<tr><td>%s</td><td>%s</td></tr>" % (name, data[name])
    result += "</table>"
    return result

if __name__ == "__main__":
    app.run(port=5000, debug=True)


#Counter({'54': 3, 'D8': 2, 'H5': 2, 'K5': 1, 'I5': 1})