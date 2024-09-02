# UTF-8 Validation

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **UTF-8 Validation**<br/>[0-stats.py](0-stats.py) contains a script with a function that determines if a given data set represents a valid UTF-8 encoding:
  + Prototype: `def validUTF8(data)`.
  + Return: `True` if data is a valid UTF-8 encoding, else return `False`.
  + A character in UTF-8 can be 1 to 4 bytes long.
  + The data set can contain multiple characters.
  + The data will be represented by a list of integers.
  + Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.
## UTF-8 Encoding Rules:
  + 1-byte character (ASCII): Starts with 0xxxxxxx (0-127 in decimal).
  + 2-byte character: Starts with 110xxxxx followed by 10xxxxxx.
  + 3-byte character: Starts with 1110xxxx followed by two 10xxxxxx.
  + 4-byte character: Starts with 11110xxx followed by three 10xxxxxx.
