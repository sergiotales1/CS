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

Structural induction is a proof technique used to prove properties about recursively defined data structures.

Base case -> the initial items of the set, that doesn't depend in any other value.

Constructor case -> recursive proposition that will create other values of this set, arising from this. Create new elements using the elements we already have within the set.

### pag 69

We create a constructor case that will add [ or ] for every item in the brackets set. Every new string becomes a candidate to the next strings that are arriving from this one. In this way, generating infinitely new bracket strings.

## Using Structural induction to proof recursive data types propositions

- Prove P for the base cases of the definition

- Prove P for the constructor cases of the definition, assuming that it is true for the component data items

page - 72

## Functions on Recursively defined data types

So a function will map a value from the domain set to a value from an element of the codomain.

f: A -> B

so b is called the value of f (function) at argument a

B is not part of the codomain, instead, it usually is about the rule in which the output (element of B) will arise.

#### Definition

In essence, functions on recursively defined data types leverage the very structure of the data to break down processing into manageable, self-similar steps, making complex operations elegant and provably correct.

### f(S)

f(S) is the set of all unique output values that a function f produces when you apply f to every single element within a specific subset S of its domain.

### The range of f

It is the set of values that arise from applying f to every single one element of its domain.

#### Remember

Propositional variables are just propositions like Q -> P or P.

# Why use recursively defined data types and what's this correlation with structural induction ?
