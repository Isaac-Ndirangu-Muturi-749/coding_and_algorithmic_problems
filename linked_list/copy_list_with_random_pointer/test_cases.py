from solution import Solution

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

# Helper function to create the linked list from a list of values and random pointers
def create_linked_list(data):
    if not data:
        return None

    # Create all nodes
    nodes = [Node(val=item[0]) for item in data]

    # Set next and random pointers
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.next = nodes[i + 1]
        if data[i][1] is not None:
            node.random = nodes[data[i][1]]

    return nodes[0]

# Helper function to convert the linked list to the expected output format
def linked_list_to_list(head):
    result = []
    nodes = []
    node_map = {}
    current = head
    index = 0
    while current:
        nodes.append(current)
        node_map[current] = index
        index += 1
        current = current.next

    current = head
    while current:
        random_index = node_map.get(current.random) if current.random else None
        result.append([current.val, random_index])
        current = current.next

    return result

def run_tests():
    solution = Solution()

    # Test case 1
    head_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = create_linked_list(head_data)
    cloned_head = solution.copyRandomList(head)
    output = linked_list_to_list(cloned_head)
    print(f"Test case 1: {output} == {head_data}")

    # Test case 2
    head_data = [[1, 1], [2, 1]]
    head = create_linked_list(head_data)
    cloned_head = solution.copyRandomList(head)
    output = linked_list_to_list(cloned_head)
    print(f"Test case 2: {output} == {head_data}")

    # Test case 3
    head_data = [[3, None], [3, 0], [3, None]]
    head = create_linked_list(head_data)
    cloned_head = solution.copyRandomList(head)
    output = linked_list_to_list(cloned_head)
    print(f"Test case 3: {output} == {head_data}")

if __name__ == '__main__':
    run_tests()
