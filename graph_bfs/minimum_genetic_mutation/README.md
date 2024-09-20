To solve the problem of finding the minimum number of mutations needed to mutate from the `startGene` to the `endGene`, we can approach it using **Breadth-First Search (BFS)**. The BFS approach will help us find the shortest mutation path by exploring all possible valid mutations layer by layer.

### Approach:

1. **BFS Traversal**:
   - Start from the `startGene`, and explore all valid mutations (one character change at a time) by checking if a mutation exists in the `bank`.
   - Each valid mutation will be a neighbor in the BFS traversal. We'll process it level by level to find the minimum number of mutations.

2. **Valid Mutation**:
   - A mutation is valid if it changes exactly one character in the gene string, and the resulting string is present in the `bank`.

3. **End Condition**:
   - The BFS stops when we find the `endGene`. If we can't find the `endGene` after exploring all possible valid mutations, return `-1`.

4. **Optimization**:
   - Use a set for the `bank` to achieve O(1) lookups when checking if a mutation is valid.
   - Mark genes that have been visited to avoid revisiting them in BFS.

### Algorithm Steps:

1. **Initial Setup**:
   - Use a queue to store the current gene and the number of mutations to reach that gene.
   - Use a set to store visited genes to avoid cycles.

2. **BFS Execution**:
   - For each gene in the queue, generate all possible mutations (change one character at a time).
   - If a valid mutation (exists in the `bank` and not visited) is found, add it to the queue and mark it as visited.

3. **Termination**:
   - If the `endGene` is reached, return the number of mutations.
   - If the queue is exhausted and the `endGene` was not found, return `-1`.

### Code Implementation:

```python
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # If the endGene is not in the bank, there is no valid mutation path
        if endGene not in bank:
            return -1

        # Set of valid gene mutations from the bank
        bank_set = set(bank)
        visited = set()  # To keep track of visited genes
        queue = deque([(startGene, 0)])  # Queue of (current_gene, mutation_count)

        # All possible characters a gene can mutate into
        gene_chars = ['A', 'C', 'G', 'T']

        while queue:
            current_gene, mutation_count = queue.popleft()

            # If we reach the endGene, return the mutation count
            if current_gene == endGene:
                return mutation_count

            # Explore all possible mutations by changing one character at a time
            for i in range(len(current_gene)):
                for char in gene_chars:
                    # Generate a new mutation by changing one character
                    mutated_gene = current_gene[:i] + char + current_gene[i+1:]

                    # If it's a valid mutation and hasn't been visited yet
                    if mutated_gene in bank_set and mutated_gene not in visited:
                        visited.add(mutated_gene)  # Mark it as visited
                        queue.append((mutated_gene, mutation_count + 1))  # Add it to the queue

        # If the endGene was never reached
        return -1
```

### Explanation:

1. **Initial Checks**:
   - If `endGene` is not in the `bank`, it's impossible to reach it, so return `-1`.

2. **Queue Setup**:
   - We use a queue (`deque`) to store each gene along with the number of mutations it took to reach that gene.
   - We also use a `visited` set to avoid reprocessing the same gene.

3. **Generating Mutations**:
   - For each gene in the queue, we attempt to mutate each character in the gene to `'A'`, `'C'`, `'G'`, or `'T'` and check if the mutated gene exists in the `bank`.

4. **BFS Traversal**:
   - If a valid mutation is found, it’s added to the queue with the mutation count incremented.
   - If the `endGene` is found, return the mutation count.

5. **Termination**:
   - If the queue becomes empty and we haven't found the `endGene`, return `-1`.

### Time Complexity:

- **Time Complexity**: O(m * n * 4) where `m` is the length of the gene string (always 8) and `n` is the number of strings in the bank. For each string in the queue, we generate mutations by changing each character (4 possibilities), and checking for validity takes O(1) time using the set.

- **Space Complexity**: O(n) for storing the `bank` and `visited` sets.

### Example Walkthrough:

#### Example 1:

```python
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
```

1. Start BFS from `"AACCGGTT"` with 0 mutations.
2. Mutate `"AACCGGTT"`:
   - Try changing each character to `'A'`, `'C'`, `'G'`, or `'T'`.
   - After mutating the last character to `'A'`, we get `"AACCGGTA"`, which is in the bank.
3. We found the `endGene` after 1 mutation, so return `1`.

#### Example 2:

```python
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
```

1. Start BFS from `"AACCGGTT"` with 0 mutations.
2. Mutate `"AACCGGTT"` and find `"AACCGGTA"` after 1 mutation.
3. From `"AACCGGTA"`, mutate again and find `"AAACGGTA"` after 1 more mutation.
4. We found the `endGene` after 2 mutations, so return `2`.

### Final Thoughts:

This approach ensures that we explore the minimal number of mutations and find the shortest mutation path using BFS. It guarantees that if a solution exists, we will find it, and if not, it returns `-1`.
