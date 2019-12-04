import sys
import PotenciaBombaTuberiaSimple as pbt
from PyQt5 import uic,QtWidgets

qtCreatorFile = "PotenciaRequerida.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Aqui se declaran los botones a usar :
        self.btn_calcular.clicked.connect(self.calculos_P)

    
    # Función que se ejecuta al pulsar el botón:
    def calculos_P(self):
        Q = float(self.txt_Q.text())/1000
        d = float(self.txt_d.text())
        ks = float(self.txt_ks.text())
        km = float(self.txt_km.text())
        L = float(self.txt_L.text())
        p = float(self.txt_p.text())
        u = float(self.txt_u.text())
        n = float(self.txt_n.text())/100
        z2 = float(self.txt_z2.text())
        P = pbt.PotenciaRequerida(Q,L,d,ks,km,p,u,z2,n)
        self.lbl_P.setText('{:.4f}'.format(P))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())