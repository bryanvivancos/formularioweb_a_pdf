from flask import Flask, request,render_template, url_for,redirect
from datetime import datetime
import pandas as pd
from docxtpl import DocxTemplate

####documento de memo y header

doc = DocxTemplate("memorando.docx")
columns=["para","de","copia","fecha","asunto","comentarios"]

####

####inicio pagina con Flask

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
    
    print(columns)
    
    with open(f'bd.csv','a') as archivo:
        
        archivo.write(f'{para};{de};{copia};{fecha};{asunto};{comentarios}\n')
        
    df = pd.read_csv('bd.csv',names=columns, delimiter=";")
    print(df)
    
    for indice,fila in df.iterrows():
        contenido = {
            "para":fila["para"],
            "de":fila["de"],
            "copia":fila["copia"],
            "fecha":fila["fecha"],
            "asunto":fila["asunto"],
            "comentarios":fila["comentarios"]}

####asignacion de las variables al documento y guarda en .docx

    doc.render(contenido)
    doc.save(f'memos/memo_{fila["para"]}.docx')
        
    return redirect(url_for('index'))

#####

if (__name__ == '__main__'):
    app.run(debug=True)