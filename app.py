from PySide2.QtWidgets import QApplication
from controllers.main_windows import PantallaPrint
        
xancho=0
yalto=0
#pestaña general de los grados para la pestaña de busqueda tabla
if __name__ == "__main__":

    app = QApplication()
    xtitulo = "Sistema de control institucional"
    app.valorglobal=10
    # tamaño=app.desktop().screenGeometry()
    # xancho=tamaño.getRect()[2]
    # yalto=tamaño.getRect()[3]
    
    windows = PantallaPrint()
    windows.setWindowTitle(xtitulo)
    # windows.representantespantalla(xancho, yalto)
    windows.show()
    
    app.exec_()
