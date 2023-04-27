import time
import pylast
from yandex_music import Client

LastFM_username = "UR_LASTFM_USER"
LastFM_password = "UR_LASTFM_PASSWD"
YandexMusic_TOKEN = "UR_YM_TOKEN"

network = pylast.LastFMNetwork(
    api_key="6b5d8a7decab0c7b547a90dbbf37efc7",
    api_secret="9778621ef705328e52b161bd76a7ac40",
    username=LastFM_username,
    password_hash=pylast.md5(LastFM_password),
)
client = Client(YandexMusic_TOKEN)

last_artist = ""
last_title = ""
last_duration = 0
last_start_time = 0
scrobbled = False

while True:
    queues = client.queues_list()
    last_queue = client.queue(queues[0].id)
    try:
        try:
            try:
                current_track_id = last_queue.get_current_track()
                current_track = current_track_id.fetch_track()
                artist = current_track.artists[0].name
                title = current_track.title
                duration = current_track.duration_ms // 1000
            except TypeError:
                pass
        
        except Exception:
            pass

        if artist != last_artist or title != last_title or duration != last_duration:
            if last_artist != "" and last_title != "" and last_duration != 0 and not scrobbled:
                time_passed = int(time.time()) - last_start_time
                if time_passed >= last_duration // 2:
                    network.scrobble(artist=last_artist, title=last_title, timestamp=last_start_time + last_duration // 2)
                    scrobbled = True

            last_artist = artist
            last_title = title
            last_duration = duration
            last_start_time = int(time.time())
            scrobbled = False

            network.update_now_playing(artist=last_artist, title=last_title)
    except NameError:
        time.sleep(30)
        pass

    time.sleep(5)
