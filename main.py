#importa librerias
import pandas as pd
import aspose.pdf as ap #pendiente convertirlo a pdf 
from datetime import datetime
from docxtpl import DocxTemplate


#guarda documento word en variable
doc = DocxTemplate("memorando.docx")

#asignacion de valores a las variables
para = "Bryan"
de = "Bryan J"
copia = "BJ, JB"
fecha = datetime.today().strftime("%d/%m/%Y")
asunto = " Bienvenida "
comentarios = " Este es un comentario "

#creacion de diccionario donde se unen las variables
diccionario = {'para':para, 'de':de,'copia':copia,'fecha':fecha,'asunto':asunto,'comentarios':comentarios}

#asignacion de las variables al documento y guarda en pdf
doc.render(diccionario)
doc.save(f'prueba.docx')

