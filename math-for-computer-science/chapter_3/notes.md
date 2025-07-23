# Well Ordering Principle

how do we know that the fraction m / n for m, n being any of the positive integers can be reduced to m′ and n′? (lowest terms)

Remember z+ = positive integers

# Induction - page 49

Induction proof is a technique used to prove that P(n) is true for all non negative integers.

Just like knocking over a line of dominoes... if P(n) then P(n + 1)

## Base case

Show that the statement P(n) holds for the smallest number (n = 0 | n = 1). Basically knocking over the first domino.

## Inductive hypothesis

Assume that P(k) holds where k > n (n = 0 | n = 1), then prove that P(k + 1) is true using the assumption that P(k) holds. This step shows that if any domino falls, the next will also fall.

# Strong induction

Instead of just assuming that p(n) is true, we assume that p(1), ..., p(n) is true and we use this to discover if p(n + 1) is also true.

# Structural induction

Base case -> the initial items of the set, that doesn't depend in any other value.

Constructor case -> recursive proposition that will create other values of this set, arising from this. Create new elements using the elements we already have within the set.

### pag 69

We create a constructor case that will add [ or ] for every item in the brackets set. Every new string becomes a candidate to the next strings that are arriving from this one. In this way, generating infinitely new bracket strings.

## Using Structural induction to proof recursive data types propositions

- Prove P for the base cases of the definition

- Prove P for the constructor cases of the definition, assuming that it is true for the component data items

page - 72
