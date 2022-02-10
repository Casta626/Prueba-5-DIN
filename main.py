import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage,QLineEdit, QHBoxLayout, QLabel, QComboBox, QTextEdit, QVBoxLayout,QMessageBox, QAbstractItemView
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
# Para ajustar el texto de los comentarios
import textwrap
# Para poner la fecha de hoy
from datetime import datetime
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtCore import QUrl, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QHBoxLayout, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

from PySide6.QtGui import QAction

from pyqtgraph.Qt import QtGui

from ui_design2 import Ui_MainWindow



import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtHelp import QHelpEngineCore
from PySide6.QtGui import QAction




class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Ayuda en línea:")
        # Creamos un visor web
        self.webAyuda = QWebEngineView()
        self.webAyuda.setUrl("mycollection.qhc")

        layout.addWidget(self.label)
        layout.addWidget(self.webAyuda)
        self.setLayout(layout)

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusBar()

        

        self.graphWidget = pg.PlotWidget(self.tabDatos)
        self.graphWidget.setGeometry(QRect(10, 360, 441, 251))
        self.verticalLayout_2.addWidget(self.graphWidget)

        # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.webpdf.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        rutaConPDF2 = Path("result.pdf")
        
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.webpdf.load(QUrl(rutaConPDF2.absolute().as_uri()))
#####################################################################
        self.pushButton.pressed.connect(self.generateGraphic)
        self.pushButton_2.pressed.connect(self.generatePDF)




        ######################

        self.pushButton.setStatusTip("Genera una gráfica en el cuadro inferior con los datos indicados")
        self.pushButton.setToolTip("Genera una gráfica en el cuadro inferior con los datos indicados")
        self.pushButton.setWhatsThis("Escribe los datos de los diferentes puntos a dibujar y pulsa este boton para generar debajo de los botones una grafica con estos datos representados")

        self.pushButton_2.setStatusTip("Genera un informe en PDF que puede consultarse en la pestaña informe")
        self.pushButton_2.setToolTip("Genera un informe en PDF que puede consultarse en la pestaña informe")
        self.pushButton_2.setWhatsThis("Pulsa este boton para generar un informe en PDF que incluya los datos de la grafica y la representacion de la misma que puede visualizarse en la pestaña informe")

        # self.webAyuda.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # # Con Path guardamos la ruta relativa al documento
        # rutaConAyuda = Path("mycollection.qhc")
        
        # # Cargamos el fichero con la ruta absoluta como uri
        # # Usando http o https también se pueden cargar páginas web
        # self.webAyuda.load(QUrl(rutaConAyuda.absolute().as_uri()))

        help_menu = self.menuBar().addMenu("&Ayuda")
        
        help_action = QAction("&Solicitar ayuda sobre un componente", self)
        help_action.setStatusTip("Acción de abrir la ayuda")
        help_action.triggered.connect(self.toggle_window)

        help_menu.addAction(help_action)

        self.w = AnotherWindow()

    def toggle_window(self, checked):
        
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()

        ######################

        
# Esta era para añadir la gráfica al pdf
    def generateGraphic(self):
        plt = pg.plot([1,5,2,4,3])

        # Creamos una instancia de exportación con el ítem que queremos exportar
        exporter = pg.exporters.ImageExporter(plt.plotItem)

        # Establecemos los parámetros de la exportación (anchura)
        exporter.parameters()['width'] = 100   # (afecta a la altura de forma proporcional)

        # Elegimos el nombre del archivo en el que exportamos la gráfica como imagen
        exporter.export('graphic.png')

        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 650
        canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

        template_obj = pagexobj(template)

        # Creamos un canvas de reportlab para dibujar en el PDF resultante
        canvas = Canvas(outfile)

        # Generamos un objeto canvas con la plantilla
        xobj_name = makerl(canvas, template_obj)
        # Y lo añadimos al canvas creado para el resultado
        canvas.doForm(xobj_name)

        # Elegimos la altura de la imagen
        ystart = 250

        # Dibujamos la imagen dejando 50 píxeles a la izquierda
        canvas.drawImage("graphic.png", 50, ystart, width=None,height=None,mask=None)

        # Guardamos el canvas
        canvas.save()
        

# esta era para hacer la grafica abajo
    def generateGraphi(self):

        self.data = {
            'x1': str(self.spinBox.value()),
            'x2': str(self.spinBox_2.value()),
            'x3': str(self.spinBox_3.value()),
            'x4': str(self.spinBox_4.value()),
            'x5': str(self.spinBox_5.value()),
            'x6': str(self.spinBox_6.value()),
            'x7': str(self.spinBox_7.value()),
            'x8': str(self.spinBox_8.value()),
            'x9': str(self.spinBox_9.value()),
            'x10': str(self.spinBox_10.value()),
            'y1': str(self.spinBox_11.value()),
            'y2': str(self.spinBox_12.value()),
            'y3': str(self.spinBox_13.value()),
            'y4': str(self.spinBox_14.value()),
            'y5': str(self.spinBox_15.value()),
            'y6': str(self.spinBox_16.value()),
            'y7': str(self.spinBox_17.value()),
            'y8': str(self.spinBox_18.value()),
            'y9': str(self.spinBox_19.value()),
            'y10': str(self.spinBox_20.value())
            
        }

         # Todas las gráficas son un widget PlotWidget
        # Proporciona un canvas en el que dibujar cualquier gráfica
        self.graphWidget = pg.PlotWidget(self.tabDatos)
        self.graphWidget.setGeometry(QRect(10, 360, 441, 251))
        # self.setCentralWidget(self.graphWidget)

        # Representamos los puntos de hora y temperatura
        x = [str(self.spinBox.value()),str(self.spinBox_2.value()),str(self.spinBox_3.value()),str(self.spinBox_4.value()),str(self.spinBox_5.value()),
        str(self.spinBox_6.value()),str(self.spinBox_7.value()),str(self.spinBox_8.value()),str(self.spinBox_9.value()),str(self.spinBox_10.value())]
        y = [str(self.spinBox_11.value()),str(self.spinBox_12.value()),str(self.spinBox_13.value()),str(self.spinBox_14.value()),str(self.spinBox_15.value()),
        str(self.spinBox_16.value()),str(self.spinBox_17.value()),str(self.spinBox_18.value()),str(self.spinBox_19.value()),str(self.spinBox_20.value())]

        # Podemos cambiar el fondo, con muchas formas de definir el color
        # self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa')
        # self.graphWidget.setBackground((100,50,255,25)) #RGBA
        self.graphWidget.setBackground(QtGui.QColor(100,50,254,25))

        # Y los dibujamos (x,y)
        self.graphWidget.plot(x, y)
        

    def generatePDF(self):

        # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.webpdf.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        rutaConPDF2 = Path("result.pdf")
        
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.webpdf.load(QUrl(rutaConPDF2.absolute().as_uri()))
        # self.web.load(QUrl("https://github.com/"))

        self.data = {
            'x1': str(self.spinBox.value()),
            'x2': str(self.spinBox_2.value()),
            'x3': str(self.spinBox_3.value()),
            'x4': str(self.spinBox_4.value()),
            'x5': str(self.spinBox_5.value()),
            'x6': str(self.spinBox_6.value()),
            'x7': str(self.spinBox_7.value()),
            'x8': str(self.spinBox_8.value()),
            'x9': str(self.spinBox_9.value()),
            'x10': str(self.spinBox_10.value()),
            'y1': str(self.spinBox_11.value()),
            'y2': str(self.spinBox_12.value()),
            'y3': str(self.spinBox_13.value()),
            'y4': str(self.spinBox_14.value()),
            'y5': str(self.spinBox_15.value()),
            'y6': str(self.spinBox_16.value()),
            'y7': str(self.spinBox_17.value()),
            'y8': str(self.spinBox_18.value()),
            'y9': str(self.spinBox_19.value()),
            'y10': str(self.spinBox_20.value())
            
        }
        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 600

        canvas.drawString(150, ystart, self.data['x1'])
        canvas.drawString(150, ystart-(23*1), self.data['x2'])
        canvas.drawString(150, ystart-(24*2), self.data['x3'])
        canvas.drawString(150, ystart-(23*3), self.data['x4'])
        canvas.drawString(150, ystart-(24*4), self.data['x5'])
        canvas.drawString(150, ystart-(23*5), self.data['x6'])
        canvas.drawString(150, ystart-(24*6), self.data['x7'])
        canvas.drawString(150, ystart-(23*7), self.data['x8'])
        canvas.drawString(150, ystart-(24*8), self.data['x9'])
        canvas.drawString(150, ystart-(23*9), self.data['x10'])

        canvas.drawString(430, ystart, self.data['y1'])
        canvas.drawString(430, ystart-(23*1), self.data['y2'])
        canvas.drawString(430, ystart-(24*2), self.data['y3'])
        canvas.drawString(430, ystart-(23*3), self.data['y4'])
        canvas.drawString(430, ystart-(24*4), self.data['y5'])
        canvas.drawString(430, ystart-(23*5), self.data['y6'])
        canvas.drawString(430, ystart-(24*6), self.data['y7'])
        canvas.drawString(430, ystart-(23*7), self.data['y8'])
        canvas.drawString(430, ystart-(24*8), self.data['y9'])
        canvas.drawString(430, ystart-(23*9), self.data['y10'])


        # # Ponemos la fecha de hoy
        # # today = datetime.today()
        # # canvas.drawString(480, ystart, today.strftime('%F'))

        # # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # # En este caso, cada línea son 28 puntos
        # canvas.drawString(294, ystart, self.data['x2'])
        # # canvas.drawString(230, ystart-28, self.data['apellidos'])

        # canvas.drawString(175, ystart-(32), self.data['x3'])

        # canvas.drawString(290, ystart-(32), self.data['x4'])

        # canvas.drawString(423, ystart-(32), self.data['x5'])

        # canvas.drawString(168, ystart-(2*32), self.data['x6'])

        # canvas.drawString(285, ystart-(2*32), self.data['x7'])

        # canvas.drawString(128, ystart-(3*32), self.data['x8'])

        # canvas.drawString(472, ystart-(3*32), self.data['x9'])

        # # canvas.drawString(472, ystart-(2*32), self.data['prueba'])

        # # Sería posible establecer un límite en el número de caracteres:
        # # field.setMaxLength(25)

        # # Reemplazamos los saltos de línea por espacios en los comentarios
        # comments = self.data['x10'].replace('\n', ' ')
        # if comments:
        #     # Separamos el texto de la primera línea (más corta que el resto)
        #     lines = textwrap.wrap(comments, width=65)
        #     # Nos quedamos la primera línea
        #     first_line = lines[0]
        #     # Guardamos el resto en remainder
        #     remainder = ' '.join(lines[1:])

        #     # Separamos el resto con una anchura mayot
        #     lines = textwrap.wrap(remainder, 75)
        #     # Nos quedamos con las cuatro primeras que son el máximo (sin incluir la primera)
        #     lines = lines[:4]

        #     # Escribimos la primera línea
        #     canvas.drawString(147, ystart-(4*32), first_line)
        #     # Y luego las otras cuatro
        #     for n, l in enumerate(lines, 1):
        #         canvas.drawString(80, ystart-(4*32) - (n*32), l)

        canvas.save()
        QMessageBox.information(self, "Finalizado", "Se ha generado el PDF")


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Informes automatizados')
window.show()
app.exec()