
import random

class RandomizedSet:

    def __init__(self):
        # Dictionary to store the value and its index in the array
        self.val_to_index = {}
        # List to store the elements
        self.values = []

    def insert(self, val: int) -> bool:
        # If the value already exists, return False
        if val in self.val_to_index:
            return False

        # Add the value to the list and store its index in the hashmap
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If the value does not exist, return False
        if val not in self.val_to_index:
            return False

        # Get the index of the value to remove
        index_to_remove = self.val_to_index[val]
        last_val = self.values[-1]

        # Move the last element to the place of the element to remove
        self.values[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove

        # Remove the last element from the list and delete the val from the hashmap
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
