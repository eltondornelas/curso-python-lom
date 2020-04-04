# Aula - Instalação e primeiro contato com o PyQT5
"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...

# pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()  # cw = central widget
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 40px;')  # add CSS
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # adiciona o botão na grid = grade -> contém linhas e colunas
        # (0, 0, 1, 1) -> (linhas, colunas, qtd_linha_botao_ocupa, qtd_coluna_botao_ocupa)

        # self.btn.clicked.connect(lambda: print('hellow world!!'))
        self.btn.clicked.connect(self.acao)
        # evento de quando o botão é clicado

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa...')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()  # instanciando uma classe, normalmente.
    app.show()  # ativa o app
    qt.exec_()  # executa o app
