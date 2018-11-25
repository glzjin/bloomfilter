from BloomFilter.BloomFilter import BloomFilter
from PostgreSQL import Database
from netease import Artist


def get_songs():
    # pull all data from netease music
    singers = ['周杰伦', '宋祖英', '羽泉', '郁钧剑', '赵本山']

    for singer in singers:
        songs = Artist.Artist(singer).songs()
        print(songs)
        for song in songs:
            print(song)
            database.insert(song)


def create_bloom_filter(mod_number, datas):
    bloom_filter = BloomFilter(mod_number)
    for data in datas:
        bloom_filter.add(data[0])

    return bloom_filter


if __name__ == "__main__":
    database = Database.DataBase(host="localhost", database="test1124", user="postgres", password="miaomiaomiao")

    # get_songs()

    # and pull all things we get to memory
    datas = database.pull_all()

    # create a bloom filter
    print("Create a 4096 mod bloom filter...")
    bloom_filter = create_bloom_filter(4096, datas)

    # test
    print("Test a element doesn't exist: ")
    print(bloom_filter.exist("喀山"))
    print("Test a element exist: ")
    print(bloom_filter.exist("舍得"))
    print("False positive: ")
    print(bloom_filter.get_false_positive())
