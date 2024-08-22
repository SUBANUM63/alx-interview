# Minimum Operations

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Minimum Operations**<br/>[0-minoperations.py](0-minoperations.py) contains a script that meets the following requirements:
  + In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.
    + Prototype: `def minOperations(n)`.
    + To solve this problem, you need to recognize that the optimal way to reach exactly n H characters using the least number of operations involves determining the factors of n. This is because the most efficient strategy is to repeatedly copy and paste a block of characters that is a divisor of n.

  + # Steps to Solve:
      + Initialization: Start with a counter to keep track of the number of operations and a variable to represent the current number of H characters.
      + Factorization: To achieve n characters, you need to find the largest factor of n (other than n itself), copy all, and paste the required number of times to reach n.
      + Loop and Multiply: Reduce n by dividing it by its smallest prime factor until n becomes 1, counting the operations (which is the factor itself) each time.
    + Returns an integer.
    + If `n` is impossible to achieve, return `0`.
  + # Explanation:
    + n = 9:
    + Start with n = 9.
    + The smallest prime divisor of 9 is 3, so we divide 9 by 3, reducing it to 3, and add 3 operations (Copy All + Paste twice).
Now, 3 is also divisible by 3, so we divide by 3 again, reducing n to 1 and adding 3 more operations (Copy All + Paste twice).
    + Total operations = 6.
  + # Examples:
    + n = 6:

    + 6 can be divided by 2, resulting in 3, and then divided by 3, resulting in 1.
    + Operations: 2 + 3 = 5.
    + n = 15:

    + 15 can be divided by 3 (gives 5), and 5 is a prime number itself.
    + Operations: 3 + 5 = 8.
  + # Conclusion:
      + The method efficiently computes the minimum number of operations needed by factorizing n and summing up the divisors, ensuring that you get exactly n H characters in the fewest steps.
