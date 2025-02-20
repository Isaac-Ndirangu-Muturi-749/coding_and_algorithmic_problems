class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # Custom sorting function for letter-logs
        def get_key(log):
            id_, rest = log.split(" ", 1)
            # Return a tuple: (0, content, identifier) for letter-logs
            # Return a tuple: (1, None, None) for digit-logs to maintain relative order
            return (0, rest, id_) if rest[0].isalpha() else (1, None, None)

        # Sort logs using the custom key function
        return sorted(logs, key=get_key)
