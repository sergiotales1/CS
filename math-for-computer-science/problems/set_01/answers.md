# [Problem set](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/52e4d5a499a39c41c129e1eb4e831e20_MIT6_042JF10_assn01.pdf)

### 1-

a) - ∃x. S(x) ^ A(x)

b) - ∀x. (T(x) ^ S(x)) -> A(x)

c) - ∀x. T(x) -> A(x)
For every x, if T(x) then A(x)

d) - ∃x ∃y ∃z. (¬(E(x, y)) ^ ¬(E(x, z)) ^ ¬(E(z, y))). (T(x) ^ ¬(S(x))) ^ (T(y) ^ ¬(S(y))) ^ (T(z) ^ ¬(S(z)))

### 2-

A) Equivalent
B) Unequal

| P   | Q   | R   | ¬P ∨ (¬Q ∨ ¬R) | ¬(P ∧ (Q ∨ R)) | ¬(P ∨ (Q ∧ R)) | (¬P) ∧ (¬Q ∨ ¬R) |
| --- | --- | --- | -------------- | -------------- | -------------- | ---------------- |
| T   | T   | T   | F              | F              | F              | F                |
| T   | T   | F   | T              | F              | F              | F                |
| T   | F   | T   | T              | F              | F              | F                |
| F   | T   | T   | T              | T              | F              | F                |
| T   | F   | F   | T              | T              | F              | T                |
| F   | F   | T   | T              | T              | T              | T                |
| F   | T   | F   | T              | T              | T              | T                |
| F   | F   | F   | T              | T              | T              | T                |

### 3-

A)
(I) (A nand A) nand (B nand B)
(II) (A nand A) nand (B nand B)
(III) (A NAND (A NAND B)) NAND (A NAND (A NAND B))(A NAND (A NAND B)) NAND (A NAND (A NAND B)) ← derived from equivalence

(Only with try and error)

B) (A nand A)

4 - Separe the coins in two groups of 6 and measure them, discard the heavier side and keep the lighter side. Separe this group in two groups of 3 coins and weigh both. Discard the heavier and keep the lighter side. Take two coins out of the 3 lighter coins and measure them together.

If the measurement reaches an equal result then the lighter coin, namely, the fake one is the third coin unweighted.

if the measurement points out a lighter coin then this is the fake coin.
