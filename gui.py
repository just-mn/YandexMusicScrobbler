import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lastfm_username_label = QLabel('LastFM Username:')
        self.lastfm_username_input = QLineEdit()
        layout.addWidget(self.lastfm_username_label)
        layout.addWidget(self.lastfm_username_input)

        self.lastfm_password_label = QLabel('LastFM Password:')
        self.lastfm_password_input = QLineEdit()
        self.lastfm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.lastfm_password_label)
        layout.addWidget(self.lastfm_password_input)

        self.yandex_music_token_label = QLabel('Yandex Music Token:')
        self.yandex_music_token_input = QLineEdit()
        layout.addWidget(self.yandex_music_token_label)
        layout.addWidget(self.yandex_music_token_input)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        lastfm_username = self.lastfm_username_input.text()
        lastfm_password = self.lastfm_password_input.text()
        yandex_music_token = self.yandex_music_token_input.text()

        with open('scrobbler.py', 'r') as f:
            content = f.read()

        content = re.sub(r'LastFM_username = "UR_LASTFM_USER"', f'LastFM_username = "{lastfm_username}"', content)
        content = re.sub(r'LastFM_password = "UR_LASTFM_PASSWD"', f'LastFM_password = "{lastfm_password}"', content)
        content = re.sub(r'YandexMusic_token = "UR_YM_TOKEN"', f'YandexMusic_token = "{yandex_music_token}"', content)

        with open('scrobbler.py', 'w') as f:
            f.write(content)

        print('Credentials updated in scrobbler, run "python scrobbler.py"')


        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
