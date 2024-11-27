class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # Array to store how many papers have citation >= i
        paper_counts = [0] * (n + 1)

        # Fill the paper_counts array
        for c in citations:
            # If a paper has more citations than n, consider it as n (since h-index is bounded by n)
            paper_counts[min(n, c)] += 1

        # Start checking from the maximum possible h-index (which is n)
        h = n
        papers = paper_counts[n]

        # Traverse backwards to check for the valid h-index
        while h > 0 and papers < h:
            h -= 1
            papers += paper_counts[h]

        return h
