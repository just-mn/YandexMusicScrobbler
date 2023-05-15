import sys
import os
import yaml
import pylast
from yandex_music import Client
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lastfm_session_label = QLabel('Click "Login us LastFM" button for LastFM auth')
        self.yandex_music_token_label = QLabel('Yandex Music Token (check README)')
        self.yandex_music_token_input = QLineEdit()
        self.setWindowTitle('Setup')
        self.setWindowIcon(QIcon('./assets/icon.png'))
        layout.addWidget(self.lastfm_session_label)
        self.lastfm_session_button = QPushButton('Login us LastFM')
        self.lastfm_session_button.clicked.connect(self.lastfm_login)
        layout.addWidget(self.lastfm_session_button)
        layout.addWidget(self.yandex_music_token_label)
        layout.addWidget(self.yandex_music_token_input)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def lastfm_login(self):
        sg = pylast.SessionKeyGenerator(
            pylast.LastFMNetwork(
                api_key="086a0b632e5e3297ac1850fdb8e19ad2",
                api_secret="a25433d094644b8447b1e278cd253bf4",
            )
        )
        url = sg.get_web_auth_url()
        token = sg.web_auth_tokens[url]
        webbrowser.open(url)
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Confirm Login')
        msgBox.setWindowIcon(QIcon('./assets/warning.png'))
        msgBox.setText("Нажмите ОК после разрешения доступа к аккаунту")
        msgBox.exec_()

        try:
            self.lastfm_session_key, self.lastfm_username = sg.get_web_auth_session_key_username(url, token)
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Error')
            msgBox.setWindowIcon(QIcon('./assets/error.png'))
            msgBox.setText("Не удалось подключится к аккаунту LastFM")
            msgBox.exec_()

    def login(self):
        try:
            client = Client(self.yandex_music_token_input.text())
            yandex_display_name = client.account_status().account.display_name
            if os.path.isfile('data.yaml'):
                with open('data.yaml', 'r') as file:
                    data = yaml.load(file, Loader=yaml.FullLoader)
                data['LastFM_sk'] = self.lastfm_session_key
                data['LastFM_user'] = self.lastfm_username
                data['YaMusic_token'] = self.yandex_music_token_input.text()
                with open('data.yaml', 'w') as file:
                    yaml.dump(data, file)
            elif not os.path.isfile('data.yaml'):
                data = {
                    'LastFM_sk': self.lastfm_session_key,
                    'LastFM_user': self.lastfm_username,
                    'YaMusic_token': self.yandex_music_token_input.text()
                    }
                with open('data.yaml', 'w') as file:
                    yaml.dump(data, file)
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Done')
            msgBox.setWindowIcon(QIcon('./assets/saved.png'))
            msgBox.setText(f'Вы успешно вошли!\nYandex: {yandex_display_name}\nLastFM: {self.lastfm_username}')
            msgBox.exec_()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Error')
            msgBox.setWindowIcon(QIcon('./assets/error.png'))
            msgBox.setText("Не удалось подключится к аккаунту YandexMusic")
            msgBox.exec_()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
