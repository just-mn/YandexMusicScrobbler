import time
import os
import yaml
import pylast
import yandex_music

try:
    with open('data.yaml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
except:
    print('You are not complete login\nTry run gui.py for setup script')
    exit()
network = pylast.LastFMNetwork(
    api_key="086a0b632e5e3297ac1850fdb8e19ad2",
    api_secret="a25433d094644b8447b1e278cd253bf4",
    session_key=data['LastFM_sk'],
    username=data['LastFM_user']
)
YandexMusic_token = data['YaMusic_token']
client = yandex_music.Client(YandexMusic_token)

os.system('cls' if os.name == 'nt' else 'clear')
print(" __     __             _           __  __           _         _____                _     _     _           ")
print(" \ \   / /            | |         |  \/  |         (_)       / ____|              | |   | |   | |          ")
print("  \ \_/ /_ _ _ __   __| | _____  _| \  / |_   _ ___ _  ___  | (___   ___ _ __ ___ | |__ | |__ | | ___ _ __ ")
print("   \   / _\` | '_ \ / _\` |/ _ \ \/ / |\/| | | | / __| |/ __|  \___ \ / __| '__/ _ \| '_ \| '_ \| |/ _ \ '__|")
print("    | | (_| | | | | (_| |  __/>  <| |  | | |_| \__ \ | (__   ____) | (__| | | (_) | |_) | |_) | |  __/ |   ")
print("    |_|\__,_|_| |_|\__,_|\___/_/\_\_|  |_|\__,_|___/_|\___| |_____/ \___|_|  \___/|_.__/|_.__/|_|\___|_|   ")
print("")
print("")

last_artist = ""
last_title = ""
last_duration = 0
duration = 1
artist = ""
title = ""
last_start_time = 0
scrobbled = False
my_vibe = False

def nowtime():
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S", current_time)
    return formatted_time

while True:
    try:
        queues = client.queues_list()
        last_queue = client.queue(queues[0].id)
        current_track_id = last_queue.get_current_track()
        current_track = current_track_id.fetch_track()
        artist = current_track.artists[0].name
        title = current_track.title
        duration = current_track.duration_ms // 1000
        my_vibe = False
        ectb = False
    except IndexError:
        title = "error"
        my_vibe = True
    except TypeError:
        title = "error"
        my_vibe = True
    except yandex_music.exceptions.BadRequestError:
        title = "error"
        ectb = True
    except:
        print(f'[{nowtime()}] Произошла ошибка при получении последнего трека')
    if artist != last_artist or title != last_title or duration != last_duration:
        if last_artist != "" and last_title != "" and last_duration != 0 and last_title != "error" and not scrobbled:
            time_passed = int(time.time()) - last_start_time
            if time_passed >= 40 or time_passed >= int(last_duration / 2):
                network.scrobble(artist=last_artist, title=last_title, timestamp=last_start_time)
                scrobbled = True
                print(f'[{nowtime()}] Отправлен скроббл: {last_title} - {last_artist}')
                print(f'           Прошло времени с прошлого скроббла: {time_passed}s')
            else:
                print(f'[{nowtime()}] Скроббл трека "{last_title}" пропущен')
                print(f'           Прошло времени с прошлого скроббла: {time_passed}s')

        last_artist = artist
        last_title = title
        last_duration = duration
        last_start_time = int(time.time())
        scrobbled = False

        if my_vibe:
            print(f'[{nowtime()}] Невозможно получить текущий трек. Похоже, что вы слушаете "Мою волну"')
        elif ectb:
            print(f'[{nowtime()}] Текущий трек официально не существует в Яндекс Музыке')
        elif last_artist != "" and last_title != "" and last_duration != 0 and not scrobbled:
            print(f'[{nowtime()}] Сейчас играет: {last_title} - {last_artist}')
            network.update_now_playing(artist=last_artist, title=last_title)

    time.sleep(5)
