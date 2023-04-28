#!/bin/bash
clear
echo " __     __             _           __  __           _         _____                _     _     _           ";
echo " \ \   / /            | |         |  \/  |         (_)       / ____|              | |   | |   | |          ";
echo "  \ \_/ /_ _ _ __   __| | _____  _| \  / |_   _ ___ _  ___  | (___   ___ _ __ ___ | |__ | |__ | | ___ _ __ ";
echo "   \   / _\` | '_ \ / _\` |/ _ \ \/ / |\/| | | | / __| |/ __|  \___ \ / __| '__/ _ \| '_ \| '_ \| |/ _ \ '__|";
echo "    | | (_| | | | | (_| |  __/>  <| |  | | |_| \__ \ | (__   ____) | (__| | | (_) | |_) | |_) | |  __/ |   ";
echo "    |_|\__,_|_| |_|\__,_|\___/_/\_\_|  |_|\__,_|___/_|\___| |_____/ \___|_|  \___/|_.__/|_.__/|_|\___|_|   ";
echo "                                                                                                           ";
echo "                                                                                                           ";

git clone https://github.com/just-mn/YandexMusicScrobbler
cd YandexMusicScrobbler
pip install -r requirements.txt
clear
echo " __     __             _           __  __           _         _____                _     _     _           ";
echo " \ \   / /            | |         |  \/  |         (_)       / ____|              | |   | |   | |          ";
echo "  \ \_/ /_ _ _ __   __| | _____  _| \  / |_   _ ___ _  ___  | (___   ___ _ __ ___ | |__ | |__ | | ___ _ __ ";
echo "   \   / _\` | '_ \ / _\` |/ _ \ \/ / |\/| | | | / __| |/ __|  \___ \ / __| '__/ _ \| '_ \| '_ \| |/ _ \ '__|";
echo "    | | (_| | | | | (_| |  __/>  <| |  | | |_| \__ \ | (__   ____) | (__| | | (_) | |_) | |_) | |  __/ |   ";
echo "    |_|\__,_|_| |_|\__,_|\___/_/\_\_|  |_|\__,_|___/_|\___| |_____/ \___|_|  \___/|_.__/|_.__/|_|\___|_|   ";
echo "                                                                                                           ";
echo "                                                                                                           ";

echo -n "Enter LastFM username: "
read lastfmusername
echo -n "Enter LastFM password: "
stty -echo
read lastfmpasswd
stty echo
echo
echo -n "Enter yandex music token (check how to get token in readme.md): "
stty -echo
read ymtoken
stty echo
echo

sed -i 's/LastFM_username = "UR_LASTFM_USER"/LastFM_username = "'"$lastfmusername"'"/' scrobbler.py
sed -i 's/LastFM_password = "UR_LASTFM_PASSWD"/LastFM_password = "'"$lastfmpasswd"'"/' scrobbler.py
sed -i 's/YandexMusic_TOKEN = "UR_YM_TOKEN"/YandexMusic_TOKEN = "'"$ymtoken"'"/' scrobbler.py