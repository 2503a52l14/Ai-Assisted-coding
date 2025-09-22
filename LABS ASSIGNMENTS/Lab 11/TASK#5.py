class HashTable:
    """
    A class representing a hash table with collision handling using chaining.
    """

    def __init__(self, size=10):
        """
        Initializes the hash table with a given size.

        Args:
            size: The number of buckets in the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Generates a hash for the given key.

        Args:
            key: The key to hash.

        Returns:
            The index in the hash table for the given key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        """
        Searches for a value associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.

        Args:
            key: The key to delete.

        Returns:
            True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        """
        Displays the contents of the hash table.
        """
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("orange", 3)
    hash_table.display()
    print("Search 'banana':", hash_table.search("banana"))
    hash_table.delete("apple")
    hash_table.display()
    print("Search 'apple':", hash_table.search("apple"))