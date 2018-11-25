import hashlib
import zlib


class Hasher:
    @staticmethod
    def alder32(data):
        return hex(zlib.adler32(data.encode("utf-8"))).split('x')[-1]

    @staticmethod
    def crc32(data):
        return hex(zlib.crc32(data.encode("utf-8"))).split('x')[-1]

    @staticmethod
    def md5(data):
        m2 = hashlib.md5()
        m2.update(data.encode("utf-8"))
        return m2.hexdigest()

    @staticmethod
    def sha1(data):
        sha1Obj = hashlib.sha1()
        sha1Obj.update(data.encode("utf-8"))
        return sha1Obj.hexdigest()

    @staticmethod
    def sha256(data):
        sha256Obj = hashlib.sha256()
        sha256Obj.update(data.encode("utf-8"))
        return sha256Obj.hexdigest()

    @staticmethod
    def hex_to_dec(data):
        return int(data, 16)

    @staticmethod
    def get_hash_method_list():
        return [Hasher.alder32, Hasher.crc32, Hasher.sha1, Hasher.sha256, Hasher.md5]


if __name__ == "__main__":
    for method in Hasher.get_hash_method_list():
        print(Hasher.hex_to_dec(method("Hello")))
