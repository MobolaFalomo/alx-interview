#!/usr/bin/python3
""" Method that determines if a given data set represents a valid UTF-8 encoding"""

def validUTF8(data):
    # Initialize a variable to keep track of the number of bytes left for the current character
    bytes_left = 0
    
    # Iterate through each integer in the data list
    for num in data:
        # If bytes_left is 0, we are starting a new character
        if bytes_left == 0:
            # Count the number of leading '1' bits to determine the number of bytes for this character
            mask = 1 << 7
            while mask & num:
                bytes_left += 1
                mask >>= 1
                
            # Handle invalid cases where the count is not within the range 1 to 4
            if bytes_left == 1 or bytes_left > 4:
                return False
            
            # Decrement bytes_left for the first byte since it's already processed
            bytes_left -= 1
        else:
            # Check if the current byte starts with '10' as the two most significant bits
            if num >> 6 != 0b10:
                return False
            # Decrement bytes_left for subsequent bytes
        bytes_left -= 1
    
    # If there are still bytes left after processing all data, it's an incomplete sequence
    return bytes_left == 0
