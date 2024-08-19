from flask import Flask, request,render_template, url_for,redirect
from datetime import datetime
import pandas as pd
from docxtpl import DocxTemplate

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/guardar_datos", methods = ["POST"])

def guardar_datos():
    para = request.form['para'];
    de = request.form['de'];
    copia = request.form['copia'];
    
    fecha = datetime.now().strftime('%Y/%m/%d, %H:%M:%S');
    
    asunto = request.form['asunto'];
    comentarios = request.form['comentarios'];
    
    print(para)
    print(de)
    print(copia)
    print(fecha)
    print(asunto)
    print(comentarios)
    
    with open(f'memo.txt','a') as archivo:
        #diccionarro = {'para':para, 'de':de,'copia':copia,'fecha':fecha,'asunto':asunto,'comentarios':comentarios}
        #archivo.write(diccionario)
        archivo.write(f'{para},{de},{copia},{fecha},{asunto},{comentarios}\n')
    
    return redirect(url_for('index'))

    #asignacion de las variables al documento y guarda en pdf
    
    #doc.save(f'prueba.docx')


if (__name__ == '__main__'):
    app.run(debug=True)