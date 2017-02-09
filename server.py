from flask import Flask, render_template, request
from parsing1 import values_count1
from parsing2 import values_count2
from parsing3 import data
from product_search import search1, search2, search3, search4, change_color, reject_quantity, produced_quantity, file_search
from product_amount import amount1, amount2, amount3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from products_db import Action, InputFile, ProductInFile, Product, Storage

app = Flask(__name__)
#главная страница
@app.route("/")
def index():
    return render_template('index.html', title="ТЫРЫПЫРЫ")
#уникальная страница для каждой текущей работы
@app.route("/files/<int:id>")
def test(id):
    return str(id)
#поиск id файлов, которые в работе
def input_file_id():
    ids = []
    for (input_file_id,) in db_session.query(ProductInFile.input_file_id).filter_by(product_in_file_status='started'):
        if input_file_id not in ids:
            ids.append(input_file_id)
    return(ids)
    print(ids)
#страница с выводом состава файла первого типа
@app.route("/1")
def first():
    return render_template('1.html', title="OMG", values_count1=values_count1, amount1=amount1, search1=search1, 
    search4=search4, change_color=change_color, produced_quantity=produced_quantity, reject_quantity=reject_quantity,
    file_search=file_search)
#страница с выводом состава файла второго типа
@app.route("/2")
def second():
    return render_template('2.html', title="MIN_DESIGN", values_count2=values_count2, amount2=amount2, search2=search2)
#страница с выводом состава файла третьего типа    
@app.route("/3")
def third():
    return render_template('3.html', title="OPT_LOCAL_MIFARE", data=data, amount3=amount3, search3=search3)
#страница - подтверждение строки
@app.route("/submit1", methods=["POST"])
def submit1():
    engine = create_engine('sqlite:///data.sqlite')
    db_session = scoped_session(sessionmaker(bind=engine))
    #product_in_file = ProductInFile
    change = db_session.query(ProductInFile).filter_by(id=request.form.get('id')).first()
    change.reject_quantity=request.form.get('reject_quantity')
    change.produced_quantity=request.form.get('produced_quantity')
    change.product_in_file_status="processed"
    db_session.commit()
    return render_template('1.html', title="OMG", values_count1=values_count1, amount1=amount1, search1=search1,
    search4=search4, change_color=change_color,  produced_quantity=produced_quantity, reject_quantity=reject_quantity,
    file_search=file_search)
#страница - подтверждение всей страницы работы
@app.route("/submit2", methods=["POST"])
def submit2():
    engine = create_engine('sqlite:///data.sqlite')
    db_session = scoped_session(sessionmaker(bind=engine))
    product_in_file = ProductInFile
    storage = Storage
    product = Product
    file_name = db_session.query(InputFile).filter_by(input_file_name=request.form.get('file_name')).first()
    print("file name")
    if db_session.query(ProductInFile).filter_by(input_file_id=file_name.id, product_in_file_status="started").count() > 0:
        return "Необходимо принять каждую строку"
    else:
        product_in_file = product_in_file.query.filter_by(input_file_id=file_name.id, product_in_file_status="processed").all()
        print(product_in_file)
        for product in product_in_file:
            print("for")
            produce = Storage(product_id=product.product_id, product_type="complete", product_quantity=product.produced_quantity)
            db_session.add(produce)
            print(produce)
            reject = Storage(product_id=product.product_id, product_type="perso_reject", product_quantity=product.reject_quantity)
            db_session.add(reject)
            print(reject)
            db_session.commit()
    return render_template('1.html', title="OMG", values_count1=values_count1, amount1=amount1, search1=search1,
    search4=search4, change_color=change_color,  produced_quantity=produced_quantity, reject_quantity=reject_quantity,
    file_search=file_search)

if __name__ == "__main__":
    app.run(port=5000, debug=True)