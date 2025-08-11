## 4.2 - page 85

We discoverd that the system has the pattern of letting the first jug have some integer times a - some integer times b, so we create this formula which is going to be our invariant for this problem:

s . a + t . b

We use positive signal here because it is a linear combination and any negative t will negate the b part of this equation.

## Linear combination

A linear combination of elements (like numbers or vectors) is an expression formed by multiplying each element by a scalar and then adding the results.

Scalars are just numbers (integers in this specific case) that scale (multiply) the jug capacities a and b.

## Greatest common divisor

A number that can divide two elements. In the water jug problem we're trying to divide both digits using the formula gcd(a, b).

Example: gcd(18, 24) = 6 <- 6 can divide both

# Bézout identity

Let a and b be integers with greatest common divisor d. Then there exist integers x and y such that ax + by = d

# Water gallons

We found out that every amount of water in each jug "a" and "b" can be represented as a linear combination.

Then we entered the divisibility theory.

### 4.2.1

We prove that m | a by using the division algorithm and proving that the remainder is zero (r in a = q . m + r)

### Corollary 4.2.2

Every multiple of gcd(a, b) is also a linear combination of a and b since n = gcd(a, b) . k and gcd(a, b) = xa + yb

Initially it looks easy to prove and trivial, but the point about proving it is that it guarantees that for every n multiple of gcd, n = ax + by for some integers x and y (n is a linear combination of a and b)

# Water jug process

All of this started when we discovered that linear combinations are related to common divisors.

First we proved that every jug has a linear combination of a and b amount of water. Then we proved that m (the smallest linear combination of a and b) is equal to gdc(a, b), then we proved that in order to be a linear combination, an integer has to be a multiple of gdc(a, b).

## Solution

We proved that if the target amount of water is a multiple of gcd(a, b), then we just need to fill the smaller jug and pour it into the bigger jug infinitely until it reaches the target amount of water.

### Lessons

- The obvious is not obvious until you prove it
- greatest common divisors and linear combinations can be useful
- some proofs demand work and not to be lazy

# The fundamental theorem of Arithmetic

Prime numbers are the foundation of all natural numbers.

- Just like atoms are the basic building blocks of matter.

# Alan Turing

- devised the bridge between mathematics and computation

# Importance of lemmas and corollaries

When we proof something with a lemma and a corollary we open a broader view of this proposition... We can then utilize the extra knowledge that we acquired with these corollary and lemma to ease our calculations and more.

TLDR: There are always easier ways to do the same (thing)! You just need to link these ways together.

A is an approach. B is another approach easier than A.

If i prove that the result obtained by A is the same by B then i can link both approaches and stick with the easiest.

thing = calculation, solution, API...

### Don't be lazy. Make it natural (easier).

# Multiplicative inverse

The multiplicative inverse of a number is the number that, when multiplied by the original number, gives 1.

For a number a, its multiplicative inverse is a number b, such that:

a x b = 1

then b is the multiplicative inverse of a

## In modular arithmetic

We use the multiplicative inverse to find the number which, when multiplied by a, is congruent to 1 modulo nn — that is, it leaves a remainder of 1 when divided by nn.

# How to decrypt Turing's code

We found that m\*k-1 is congruent to m which means that both divided by p share the same remainder. Therefore to know what m is we just need to check the REM(m\*k-1, p)

# Coprime

Integers a and b are relatively prime if their greatest common divisor (gcd) is 1. This means they share no common prime factors.

# RSA - introduction

RSA uses a system different than Turing's, it makes the modulo be the product of two large primes, instead of modulo a prime introduced by Turing's theory.

### Composite number

A **composite number** is a positive integer greater than 1 that has **more than two distinct positive factors** — meaning it can be divided evenly by 1, itself, and at least one other number.

In simpler terms:

- **Prime numbers** have exactly two factors: 1 and themselves.
- **Composite numbers** have more than two factors.

Example:

- **4** is composite because its factors are 1, 2, and 4.
- **6** is composite because its factors are 1, 2, 3, and 6.

The smallest composite number is **4**.
The number **1** is neither prime nor composite.

### Lemma 4.7.3

It starts by assuming the remainders are equal and shows that this assumption leads to a contradiction, namely that ki​ must be equal to kj​, which goes against our initial assumption that ki​ and kj​ were different members of the set.

- Super complicated but we reached a conclusion by using the definition of remainder and gcd.
