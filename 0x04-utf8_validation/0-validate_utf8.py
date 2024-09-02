#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits (MSBs)
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    # Iterate over each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (ASCII)
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                # Invalid (leading bits are '11',
                # but expecting 2, 3, or 4 bytes)
                return False
            elif (byte & (mask1 >> 2)) == mask1 >> 1:
                # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 >> 3)) == mask1 >> 2:
                # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 >> 4)) == mask1 >> 3:
                # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            # Continuation bytes must start with '10xxxxxx'
            if (byte & mask1) == mask1 and (byte & mask2) == 0:
                num_bytes -= 1
            else:
                return False

    # If num_bytes is not 0, then we were expecting more continuation bytes
    return num_bytes == 0
