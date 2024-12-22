class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0  # Pointer to write the compressed result
        read = 0   # Pointer to read through the input array

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character to the array
            chars[write] = char
            write += 1

            # If count > 1, write the digits of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
