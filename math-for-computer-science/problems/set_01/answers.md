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

A) Check image 01 inside this folder
