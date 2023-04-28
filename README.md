# YandexMusic Scrobbler
A simple script to return YandexMusic scrobbling 
## How to install (for linux-like systems)
<code>sh -c "$(curl -fsSL https://raw.githubusercontent.com/just-mn/YandexMusicScrobbler/main/setup.sh)" && cd YandexMusicScrobbler && python scrobbler.py</code>
## FAQ
### How to get a YandexMusic token?
Follow the [link](https://oauth.yandex.com/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d), log into your Yandex account and after refreshing the page, copy the access_token value from the address bar as soon as possible before you are transferred to the web player.
### Does scrobbling of tracks from "My vibe" work?
No. Yandex did not provide such a function in their API.
### Will scrobbling work when the script is not running?
No.
### If the same track is played multiple times in a row, will it be included in the scrobble list?
No.
### Can I run the script on a non linux system?
Yes. Because it's written in Python. If you don't know how to do it, google it.