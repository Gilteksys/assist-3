import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from cadastro_cliente import CadastroClienteWindow
from ordem_servico import OrdemServicoWindow
from PyQt5.QtWidgets import QPushButton, QCalendarWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Carregar o arquivo .ui
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, 'teste.ui')
        loadUi(ui_file, self)

        self.setWindowTitle('ASSIST-3.0')

        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(200, 550, 300, 200)
        self.calendar.hide()

        self.calendar_button = QPushButton('Calendário', self)
        self.calendar_button.setGeometry(10, 600, 100, 30)
        self.calendar_button.clicked.connect(self.toggle_calendar)

        self.pushButton.clicked.connect(self.on_button_clientes_clicked)    
        self.pushButton_3.clicked.connect(self.on_ordem_servico_clicked)
        self.pushButton_5.clicked.connect(self.close)  # Conectar o botão "Sair" ao método close

    def toggle_calendar(self):
        if self.calendar.isVisible():
            self.calendar.hide()
            self.calendar_button.setText('Calendário')
        else:
            self.calendar.show()
            self.calendar_button.setText('Calendário')

    def on_button_clientes_clicked(self):
        self.cadastro_cliente_window = CadastroClienteWindow()
        self.cadastro_cliente_window.show()

    def on_ordem_servico_clicked(self):
        self.ordem_servico_window = OrdemServicoWindow()  
        self.ordem_servico_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

