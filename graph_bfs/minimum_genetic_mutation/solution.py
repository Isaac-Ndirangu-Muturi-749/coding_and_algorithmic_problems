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
