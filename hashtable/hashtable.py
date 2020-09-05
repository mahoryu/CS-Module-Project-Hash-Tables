class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"[{self.key}, {self.value}] Next: {self.next}"

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.capacity = capacity
        self.storage = [None] * capacity
        self.elements = 0

    def __str__ (self):
        for item in self.storage:
            print(item)
        return ""

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.elements / self.capacity

    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit
    #     Implement this, and/or DJB2.
    #     """


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def find(self, node, key):
        """
        Loops through the linked list to find the the node
        with the correct key and returns None if not found.
        """
        if node.key == key:
            return node
        else:
            while node.next:
                node = node.next
                if node.key == key:
                    return node
            return None

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        new_node = HashTableEntry(key,value)
        # if empty add the node
        if not self.storage[index]:
            self.storage[index] = new_node
            self.elements += 1
        else:
            temp = self.find(self.storage[index], key)
            if temp:
                temp.value = value
            else:
                new_node.next = self.storage[index]
                self.storage[index] = new_node
                self.elements += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """

        index = self.hash_index(key)
        bucket = self.storage[index]

        if not bucket:
            print("Key Not Found")
        else:
            # remove if the node is the head
            if bucket.key == key:
                self.storage[index] = bucket.next
                self.elements -= 1
            else:
                temp1 = bucket
                temp2 = bucket.next
                # loop through the list with 2 pointers and
                # delete the node if the key is found
                while temp2:
                    if temp2.key == key:
                        temp1.next = temp2.next
                        self.elements -= 1
                        return
                    else:
                        temp1 = temp1.next
                        temp2 = temp2.next
                # looped though whole list and didn't find it
                # so print out the warning message
                print("Key Not Found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        bucket = self.storage[index]

        # if the slot is empty return None
        if not bucket:
            return None
        else:
            temp = self.find(bucket, key)
            if temp:
                return temp.value
            else:
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # make sure it stays at or above the min of 8 slots
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY

        # check if same size as current and end if it is
        if new_capacity == self.get_num_slots():
            return

        # make a temp stoarge that is a copy of the current storage
        temp_store = self.storage
        # resize the current storage to an empty new_cap storage
        self.storage = [None] * new_capacity

        # loop through old storage and use hash functions to add
        # them to the new storage
        for node in temp_store:
            if node:
                self.put(node.key,node.value)
                while node.next:
                    node = node.next
                    self.put(node.key,node.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
