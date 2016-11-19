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
    result = "<head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' \
    content='IE=edge'><meta name='viewport' content='width=device-width, \
    initial-scale=1'><link href='static/css/bootstrap.min.css' rel='stylesheet'>\
    </head><body><!DOCTYPE html><html lang='en'><table class='table table-bordered table-hover'>\
    <tr><th>Продукт</th><th>Начальное количество</th><th>Итоговое количество</th>\
    <th>Брак</th><th>На складе</th><th>Наличие</th><th>Готовность</th></tr>"
    for name in values_count1:
        if values_count1[name] <= amount1(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr>\
        <td>%s</td>\
        <td>%s</td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td>%s</td>\
        <td>%s</td>\
        <td><p><button type='button' class='btn btn-primary btn-sm'>Готово</button></p></td>\
        </tr>" % (search1(name), values_count1[name], amount1(name), availability)
    result += "</table></body></html>"
    return result

@app.route("/2")
def second():
    result = "<head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' \
    content='IE=edge'><meta name='viewport' content='width=device-width, \
    initial-scale=1'><link href='static/css/bootstrap.min.css' rel='stylesheet'>\
    </head><body><!DOCTYPE html><html lang='en'><table class='table table-bordered table-hover'>\
    <tr><th>Продукт</th><th>Начальное количество</th><th>Итоговое количество</th>\
    <th>Брак</th><th>На складе</th><th>Наличие</th><th>Готовность</th></tr>"
    for name in values_count2:
        if values_count2[name] <= amount2(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr>\
        <td>%s</td>\
        <td>%s</td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td>%s</td>\
        <td>%s</td>\
        <td><p><button type='button' class='btn btn-primary btn-sm'>Готово</button></p></td>\
        </tr>" % (search2(name), values_count2[name], amount2(name), availability)
    result += "</table></body></html>"
    return result

@app.route("/3")
def third():
    result = "<head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' \
    content='IE=edge'><meta name='viewport' content='width=device-width, \
    initial-scale=1'><link href='static/css/bootstrap.min.css' rel='stylesheet'>\
    </head><body><!DOCTYPE html><html lang='en'><table class='table table-bordered table-hover'>\
    <tr><th>Продукт</th><th>Начальное количество</th><th>Итоговое количество</th>\
    <th>Брак</th><th>На складе</th><th>Наличие</th><th>Готовность</th></tr>"
    for name in data:
        if values_count2[name] <= amount3(name):
            availability = "Достаточно"
        else:
            availability = "Нехватка"
        result += "<tr>\
        <td>%s</td>\
        <td>%s</td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td><div class='col-xs-6'><input type='number' class='form-control' placeholder='Введите..'></div></td>\
        <td>%s</td>\
        <td>%s</td>\
        <td><p><button type='button' class='btn btn-primary btn-sm'>Готово</button></p></td>\
        </tr>" % (search3(name), data[name], amount3(name), availability)
    result += "</table></body></html>"
    return result

if __name__ == "__main__":
    app.run(port=5000, debug=True)