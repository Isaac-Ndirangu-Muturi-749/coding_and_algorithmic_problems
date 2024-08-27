class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize result and carry
        result = []
        carry = 0

        # Reverse both strings
        a = a[::-1]
        b = b[::-1]

        # Determine the length of the longer string
        max_len = max(len(a), len(b))

        # Perform binary addition bit by bit
        for i in range(max_len):
            # Get the current digits or use 0 if the index is out of bounds
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0

            # Calculate the sum of bits and carry
            total = bit_a + bit_b + carry
            result_bit = total % 2  # The result bit (0 or 1)
            carry = total // 2      # The carry for the next position

            # Append the result bit to the result list
            result.append(str(result_bit))

        # If there's a carry left, append it
        if carry:
            result.append('1')

        # Reverse the result and join it to form the final binary string
        return ''.join(result[::-1])
