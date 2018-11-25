import requests
from netease import Songs


class Artist():
    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.base_url = "http://localhost:3000"

    def pull(self):
        res = requests.get(self.base_url + "/search/multimatch", params={"keywords": self.artist_name, type: 100})
        if "artist" in res.json()['result']:
            return res.json()['result']['artist'][0]['id']

    def songs(self):
        return Songs.Songs(self.pull()).pull()


if __name__ == "__main__":
    artist = Artist("羽泉")
    print(artist.songs())
