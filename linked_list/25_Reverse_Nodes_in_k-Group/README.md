Solution: Reverse Nodes in k-Group

The problem requires reversing nodes in groups of k while preserving the order of any leftover nodes that do not form a complete group. The key challenge is to reverse nodes in k-sized segments while ensuring efficiency.


---

Approach

1. Count the total number of nodes (n) in the linked list to determine how many full groups of k exist.


2. Iterate through the linked list in chunks of k and reverse each group.


3. Keep track of previous and next pointers to correctly link the reversed sections.


4. If fewer than k nodes remain at the end, leave them as they are.




---

Algorithm

1. Calculate the length n of the linked list.


2. Use a loop to reverse k nodes at a time:

Reverse the current group of k nodes.

Connect the reversed segment to the previous segment.

Move to the next group.



3. Stop when there are fewer than k nodes left.


4. Return the new head of the list.




---

Implementation

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Count the number of nodes in the list
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Step 2: Create dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy  # Pointer to the end of the last reversed group
        current = head

        # Step 3: Reverse nodes in groups of k
        while count >= k:
            prev = None
            tail = current  # The tail of the current group

            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect previous group's end to the reversed segment
            prev_group_end.next = prev
            tail.next = current  # Connect tail of reversed segment to the remaining list

            # Update pointers for the next group
            prev_group_end = tail
            count -= k

        return dummy.next  # The new head of the reversed list


---

Explanation of Code

1️⃣ Count the Total Nodes

count = 0
temp = head
while temp:
    count += 1
    temp = temp.next

This determines the number of full k-sized groups in the list.


2️⃣ Use a Dummy Node

dummy = ListNode(0)
dummy.next = head
prev_group_end = dummy
current = head

The dummy node helps simplify linking the reversed groups.

prev_group_end keeps track of where to attach the next reversed segment.


3️⃣ Reverse Nodes in k-sized Groups

while count >= k:
    prev = None
    tail = current  # Mark the tail of the current group

    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

Reverse k nodes by adjusting next pointers.

prev becomes the new head of the reversed segment.

current moves to the next group's head.


4️⃣ Connect the Reversed Group

prev_group_end.next = prev  # Attach reversed segment
tail.next = current  # Connect tail of reversed group to remaining list
prev_group_end = tail  # Move `prev_group_end` to the new tail
count -= k

The previous group's tail (prev_group_end) is connected to the new head (prev).

tail.next = current ensures the rest of the list is connected.

prev_group_end = tail prepares for the next iteration.



---

Complexity Analysis

Time Complexity: O(n)

Each node is visited once for counting and once for reversing.


Space Complexity: O(1)

We use only constant extra space.




---

Example Walkthrough

Example 1:

Input:  head = [1,2,3,4,5], k = 2

Step-by-step:

Original:   1 → 2 → 3 → 4 → 5
Reverse 2:  2 → 1 → 4 → 3 → 5
Output:     [2,1,4,3,5]

Example 2:

Input:  head = [1,2,3,4,5], k = 3

Step-by-step:

Original:   1 → 2 → 3 → 4 → 5
Reverse 3:  3 → 2 → 1 → 4 → 5
Output:     [3,2,1,4,5]


---

Edge Cases

1. Single Node List:

head = [1], k = 1 → Output: [1] (No change)


2. List Size Less Than k:

head = [1,2], k = 3 → Output: [1,2] (No change)


3. Exact Multiple of k:

head = [1,2,3,4,5,6], k = 3 → Output: [3,2,1,6,5,4]




---

Final Thoughts

The algorithm efficiently reverses nodes in k-sized groups while preserving order for remaining nodes.

Time complexity is O(n), making it optimal for large linked lists.

The use of a dummy node simplifies pointer manipulation, preventing edge-case errors.


✅ Best approach for reversing nodes in groups of k! 🚀

