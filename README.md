# YandexMusic Scrobbler
A simple script to return YandexMusic scrobbling

## Installation
1. Obtain a YandexMusic token:
   - Follow the [link](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d), log into your Yandex account and after refreshing the page, copy the access_token value from the address bar as soon as possible before you are transferred to the web player.
   ![token](https://github.com/just-mn/YandexMusicScrobbler/blob/main/assets/token.png?raw=true)

2. Clone the repository, install requirements and run the setup script
   ```
   git clone https://github.com/just-mn/YandexMusicScrobbler.git && cd YandexMusicScrobbler && pip install -r requirements.txt && python setup.py
   ```

3. Start scrobbler:
   ```
   python scrobbler.py
   ```
## Create a systemd daemon (optional, for pro)
   - Open the systemd service file with the following command:
     ```
     sudo nano /etc/systemd/system/scrobbler.service
     ```
   - Copy and paste the following configuration into the file:
     ```
     [Unit]
     Description=Scrobbler Service
     After=network.target

     [Service]
     User=<your_username>
     WorkingDirectory=/home/<your_username>/YandexMusicScrobbler/
     ExecStart=/usr/bin/python3 /home/<your_username>/YandexMusicScrobbler/scrobbler.py
     Restart=always

     [Install]
     WantedBy=multi-user.target
     ```
     Replace `<your_username>` with your Linux username.
   - Save the file and reload the systemd daemon:
     ```
     sudo systemctl daemon-reload
     ```
   - Enable and start the scrobbler service:
     ```
     sudo systemctl enable scrobbler.service
     sudo systemctl start scrobbler.service
     ```