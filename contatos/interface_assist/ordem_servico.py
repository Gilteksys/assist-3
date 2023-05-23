from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class OrdemServicoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ordem de Serviço")
        self.setGeometry(100, 100, 400, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        self.label_cliente_id = QLabel("ID do Cliente:")
        self.edit_cliente_id = QLineEdit()
        layout.addWidget(self.label_cliente_id)
        layout.addWidget(self.edit_cliente_id)

        self.label_aparelho = QLabel("Aparelho:")
        self.edit_aparelho = QLineEdit()
        layout.addWidget(self.label_aparelho)
        layout.addWidget(self.edit_aparelho)

        self.label_marca = QLabel("Marca:")
        self.edit_marca = QLineEdit()
        layout.addWidget(self.label_marca)
        layout.addWidget(self.edit_marca)

        self.label_modelo = QLabel("Modelo:")
        self.edit_modelo = QLineEdit()
        layout.addWidget(self.label_modelo)
        layout.addWidget(self.edit_modelo)

        self.label_serial = QLabel("Serial:")
        self.edit_serial = QLineEdit()
        layout.addWidget(self.label_serial)
        layout.addWidget(self.edit_serial)

        self.label_observacao = QLabel("Observação:")
        self.edit_observacao = QLineEdit()
        layout.addWidget(self.label_observacao)
        layout.addWidget(self.edit_observacao)

        button = QPushButton("Criar Ordem de Serviço")
        button.clicked.connect(self.on_create_ordem_servico_clicked)
        layout.addWidget(button)

        self.network_manager = QNetworkAccessManager(self)

    def on_create_ordem_servico_clicked(self):
        url = QUrl("http://localhost:8000/contatos/ordem_servico_create/")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        query = QUrlQuery()

        query.addQueryItem("cliente_id", self.edit_cliente_id.text())
        query.addQueryItem("aparelho", self.edit_aparelho.text())
        query.addQueryItem("marca", self.edit_marca.text())
        query.addQueryItem("modelo", self.edit_modelo.text())
        query.addQueryItem("serial", self.edit_serial.text())
        query.addQueryItem("observacao", self.edit_observacao.text())

        data = query.toString().encode("utf-8")
        reply = self.network_manager.post(request, data)
        reply.finished.connect(self.on_request_finished)

    def on_request_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            print("Ordem de Serviço criada com sucesso!")
        else:
            print("Erro ao criar Ordem de Serviço:", reply.errorString())
        reply.deleteLater()
