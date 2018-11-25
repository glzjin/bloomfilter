from BloomFilter.Hasher import Hasher


class BloomFilter:
    def __init__(self, mod_number = 16):
        self.mod_number = mod_number
        self.filter_array = {}
        for i in range(0, mod_number):
            self.filter_array[i] = 0

        self.one_count = 0

    def add(self, element):
        for method in Hasher.get_hash_method_list():
            index = Hasher.hex_to_dec(method(element)) % self.mod_number
            if self.filter_array[index] == 0:
                self.filter_array[index] = 1
                self.one_count += 1

    def exist(self, element):
        for method in Hasher.get_hash_method_list():
            index = Hasher.hex_to_dec(method(element)) % self.mod_number
            if self.filter_array[index] == 0:
                return False

        return True

    def get_false_positive(self):
        return pow(1 / self.one_count, len(Hasher.get_hash_method_list()))


if __name__ == "__main__":
    bloom_filter = BloomFilter(256)
    bloom_filter.add("Hello")
    bloom_filter.add("How")
    bloom_filter.add("good")

    print(bloom_filter.exist("good"))
    print(bloom_filter.exist("bad"))
    print(bloom_filter.exist("How"))

    print(bloom_filter.get_false_positive())
