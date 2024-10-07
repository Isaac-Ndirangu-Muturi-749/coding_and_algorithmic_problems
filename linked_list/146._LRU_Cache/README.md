To implement an LRU (Least Recently Used) cache with an efficient solution where both `get` and `put` operations run in O(1) time, we can use two data structures:

1. **Hash Map (Dictionary)**: This will allow us to store key-value pairs for fast lookups. The key will map to the value and, crucially, to the position of that key in a doubly linked list.
2. **Doubly Linked List**: This will keep track of the order in which keys are used. The most recently used keys will be near the head, and the least recently used keys will be near the tail. When a key is accessed or added, we move it to the front. When the cache exceeds capacity, we remove the key at the tail (least recently used).

### Steps:
1. **Initialization**:
   - Create a `capacity` to store the maximum size of the cache.
   - Use a dictionary to store the key-value pairs and their positions in the doubly linked list.
   - Use a doubly linked list to track the order of key usage.

2. **get(key)**:
   - If the key exists, return its value and move the key to the front of the list (mark it as recently used).
   - If the key doesn’t exist, return -1.

3. **put(key, value)**:
   - If the key already exists, update its value and move it to the front of the list.
   - If the key doesn’t exist, insert the key-value pair at the front of the list.
   - If the cache exceeds its capacity, evict the least recently used key from both the dictionary and the tail of the list.

### Code Implementation:

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # This will store the key -> node
        # Initialize the head and tail of the doubly linked list
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """Add a new node right after the head (most recent)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists, remove it from the list
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove the least recently used node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

### Explanation:
- **Node Class**: Each node in the doubly linked list contains a key and value, and pointers to both the previous and next nodes.

- **LRUCache Class**:
  - `__init__`: Initializes the cache with a given capacity and sets up a dummy head and tail for the doubly linked list. These dummy nodes help simplify the list management when inserting or removing nodes.
  - `_remove(node)`: Removes a node from its current position in the linked list.
  - `_add(node)`: Inserts a node right after the head, marking it as the most recently used.
  - `get(key)`: If the key exists, the node is moved to the front of the list (as it's now the most recently used), and the value is returned. If the key doesn’t exist, return -1.
  - `put(key, value)`: Adds a new key-value pair to the cache or updates an existing key. If adding the new key exceeds the cache capacity, the least recently used node (at the tail of the list) is removed.

### Example Walkthrough:

```python
lRUCache = LRUCache(2)  # Initialize LRU Cache with capacity 2
lRUCache.put(1, 1)      # Cache is {1=1}
lRUCache.put(2, 2)      # Cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1, Cache is {2=2, 1=1}
lRUCache.put(3, 3)      # LRU key was 2, evicts key 2, Cache is {1=1, 3=3}
print(lRUCache.get(2))  # return -1 (not found)
lRUCache.put(4, 4)      # LRU key was 1, evicts key 1, Cache is {3=3, 4=4}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4
```

### Time Complexity:
- **get()**: O(1) since both hash table lookup and the linked list operations (add/remove) are O(1).
- **put()**: O(1) for the same reason.

### Space Complexity:
- **O(capacity)** for storing the cache data and the doubly linked list nodes.

This solution efficiently maintains the LRU cache with constant time complexity for both get and put operations.
