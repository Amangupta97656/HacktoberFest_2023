class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        for entry in self.table[hashed_key]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash(key)
        for entry in self.table[hashed_key]:
            if entry[0] == key:
                return entry[1]
        return None

    def remove(self, key):
        hashed_key = self._hash(key)
        for entry in self.table[hashed_key]:
            if entry[0] == key:
                self.table[hashed_key].remove(entry)
                return

def main():
    hash_table = HashTable(10)
    
    hash_table.insert("name", "John")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")
    
    print("Value for 'name':", hash_table.get("name"))
    print("Value for 'age':", hash_table.get("age"))
    
    hash_table.remove("age")
    print("Value for 'age' after removal:", hash_table.get("age"))

if __name__ == "__main__":
    main()
