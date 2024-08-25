#importa librerias
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate


#guarda documento word en variable
doc = DocxTemplate("memorando.docx")

#leer csv, se le coloca un header (nombre a las columnas)
columns=["para","de","copia","fecha","asunto","comentarios"]
df = pd.read_csv('prueba.csv',names=columns, delimiter=";")

print(df)

for indice,fila in df.iterrows():
    contenido = {
        "para":fila["para"],
        "de":fila["de"],
        "copia":fila["copia"],
        "fecha":fila["fecha"],
        "asunto":fila["asunto"],
        "comentarios":fila["comentarios"]}

#asignacion de las variables al documento y guarda en pdf
    doc.render(contenido)
    doc.save(f'memo_{fila["para"]}.docx')
    




"""
#asignacion de valores a las variables
para = "Bryan"
de = "Bryan J"
copia = "BJ, JB"
fecha = datetime.today().strftime("%d/%m/%Y")
asunto = " Bienvenida "
comentarios = " Este es un comentario "

#creacion de diccionario donde se unen las variables
diccionario = {'para':para, 'de':de,'copia':copia,'fecha':fecha,'asunto':asunto,'comentarios':comentarios}
"""