from PySide6.QtCore import *
from PySide6.QtGui import *

class Suplementos:
      def __init__(self):

         #Icons        
         self.icon_refrescar = QIcon()
         self.icon_refrescar.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
         self.icon_imprimir = QIcon()
         self.icon_imprimir.addFile(u"./assets/icons/imprimir.png", QSize(), QIcon.Normal, QIcon.Off)
         self.icon_salir = QIcon()
         self.icon_salir.addFile(u"./assets/icons/salir_icon.png", QSize(), QIcon.Normal, QIcon.Off)
         self.icon_buscar = QIcon()
         self.icon_buscar.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
         self.icon_guardar = QIcon()
         self.icon_guardar.addFile(u"./assets/icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
         self.icon_limpiar = QIcon()
         self.icon_limpiar.addFile(u"./assets/icons/clear_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        
         #Imprimir
      def imprimir_estudiantes(self, portada, titulo, body, imagenfoot, footer):
         self.prueba = f"""
            <html>
                <body align="center";>
                <h1>{portada}</h1>
                <h2>{titulo}</h2>
                
                <hr>
                <table style="border: 1px solid black;">
                <tr>
                    <th style="padding-left: 100%; padding-right: 100%; border: 1px solid black;">CATEGORIAS</th>
                    <th style="padding-right: 100%; padding-left: 100%; border: 1px solid black;">VALORES</th>                

                </tr>
                <tr>
                    <br>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[0]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[1]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[2]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[3]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[4]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[5]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[6]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[7]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[8]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[9]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[10]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[11]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[12]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[13]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[14]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[15]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[16]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[17]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[18]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[19]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[20]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{21}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; padding-right: 80%; border: 1px solid black;">{body[22]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[23]}</td>
                </tr>
                    </table>
                    <hr>
                    <table>
                        <td style="padding-left: 150%;"><img src={imagenfoot} width="64" height="64"></td>
                        <td style="vertical-align: middle;">{footer}</td>
                    </table>
                </body>   
            </html>
            """
         return self.prueba

      def imprimir_profesores(self, portada, titulo, body, imagenfoot, footer):
         self.prueba = f"""
            <html>
                <body align="center";>
                <h1>{portada}</h1>
                <h2>{titulo}</h2>
                
                <hr>
                <table style="border: 1px solid black;">
                <tr>
                    <th style="padding-left: 100%; padding-right: 100%; border: 1px solid black;">CATEGORIAS</th>
                    <th style="padding-right: 100%; padding-left: 100%; border: 1px solid black;">VALORES</th>                

                </tr>
                <tr>
                    <br>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[0]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[1]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[2]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[3]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[4]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[5]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[6]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[7]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 5%; border: 1px solid black;">{body[8]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[9]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[10]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[11]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[12]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[13]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[14]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[15]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[16]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[17]}</td>
                </tr>
                <tr>
                    <td style="padding-left: 100%; border: 1px solid black;">{body[18]}</td>
                    <td style="padding-left: 100%; border: 1px solid black; background-color: #D6EEEE;">{body[19]}</td>
                </tr>
                    </table>
                    <hr>
                    <table>
                        <td style="padding-left: 150%;"><img src={imagenfoot} width="64" height="64"></td>
                        <td style="vertical-align: middle;">{footer}</td>
                    </table>
                </body>   
            </html>
            """
         return self.prueba