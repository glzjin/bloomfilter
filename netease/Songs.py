import requests


class Songs():
    def __init__(self, artist_id):
        self.artist_id = artist_id
        self.base_url = "http://localhost:3000"

    def pull(self):
        self.data = []

        res = requests.get(self.base_url + "/artist/album", params={"id": str(self.artist_id), "limit": 2000})
        for album in res.json()['hotAlbums']:
            res_album = requests.get(self.base_url + "/album", params={"id": album['id']})
            for song in res_album.json()["songs"]:
                self.data.append(song['name'])

        return self.data

if __name__ == "__main__":
    songs = Songs(6452)
    print(songs.pull())
