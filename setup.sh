#!/bin/bash
clear
echo "

  _      _   ___ _____ ___ __  __  __   ____  __ 
 | |    /_\ / __|_   _| __|  \/  | \ \ / /  \/  |
 | |__ / _ \\__ \ | | | _|| |\/| |  \ V /| |\/| |
 |____/_/ \_\___/ |_| |_| |_|  |_|   |_| |_|  |_|
                                                 
"
git clone https://github.com/just-mn/lastfmym
cd lastfmym
pip install -r requirements.txt
clear
echo "

  _      _   ___ _____ ___ __  __  __   ____  __ 
 | |    /_\ / __|_   _| __|  \/  | \ \ / /  \/  |
 | |__ / _ \\__ \ | | | _|| |\/| |  \ V /| |\/| |
 |____/_/ \_\___/ |_| |_| |_|  |_|   |_| |_|  |_|
                                                 
"

read -p "Enter LastFM username: " lastfmusername
read -p "Enter LastFM password: " lastfmpasswd
read -p "Enter yandex music token (check how to get token in readme.md): " ymtoken

sed -i 's/LastFM_username = "UR_LASTFM_USER"/LastFM_username = '"'$lastfmusername'"'/' lastfmym.py
sed -i 's/LastFM_password = "UR_LASTFM_PASSWD"/LastFM_password = '"'$lastfmpasswd'"'/' lastfmym.py
sed -i 's/YandexMusic_TOKEN = "UR_YM_TOKEN"/YandexMusic_TOKEN = '"'$ymtoken'"'/' lastfmym.py