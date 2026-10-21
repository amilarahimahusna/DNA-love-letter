# DNA-love-letter

# What the code does
- It changes a message into DNA letters, and then changes it back. 1 text letter becomes 3 DNA letters
- Message → position number → 6 bits → 3 DNA letters
- 00 = A, 01 = C, 10 = G, 11 = T
- complement(A-T, C-G) makes the partner strand (A-T, C-G)
- This is a fun code, not real biology

# One small weakness
In this code, ATG and TAA can also appear inside the message, because they are also valid 3-letter words (ATG = the letter O, TAA = the letter w). The code still works, because it removes the start and end by position. But in a real gene, the first TAA would stop everything. The web page version avoids this problem by not using these special words for normal letters.
