class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return None
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)

        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                return self.table[key_hash].pop(i)
        return None


H = HashTable(5)

H.insert("Carlito's Way", "Brian De Palma")
H.insert("The Devil’s Advocate", "Taylor Edwin Hackford")
H.insert("Heat", "Michael Mann")
H.insert("The Godfather", "Francis Ford Coppola")
H.insert("Donnie Brasco", "Michael Cormac Newell")
H.insert("Casino", "Martin Charles Scorsese")
H.delete("Casino")

print(H.get("Carlito's Way"))
print(H.get("The Devil’s Advocate"))
print(H.get("Heat"))
print(H.get("The Godfather"))
print(H.get("Donnie Brasco"))



