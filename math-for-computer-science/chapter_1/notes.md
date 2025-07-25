### Propositions

What are propositions?
Statements that can be either true or false. They can help you to find logical solutions and also tu push humanity knowledge boundaries after testing and proving them.

## Purpose

Allow logical reasoning — to let us ask: When is this true, and what does that tell us?

They can be always false, always true or sometimes false or true but they have to be something.

✅ A proposition doesn’t need to be always true.

### Predicates

What are predicates?
A predicate is a statement involving variables that becomes a proposition when you give specific values to those variables.

P(n, d): "n² + n = d"

Why is it called predicate?
It's because it can be true or not depending on the value of the variable, so the logic is almost like the predicate of the variable (subject), just like the grammar meaning of this word.

A predicate is just a piece of logic that need a subject to be true or false, and in order to become a proposition it needs a subject like a quantifier.

### Quantifiers

Quantifiers specify how many elements (in a domain) satisfy a predicate — either all of them or at least one.

They can be existential quantifiers ∃ which is read as "exists" or universal ∀ which is read as "for all"

#### Why do we need predicates and quantifiers?

With them, we can express generalized propositions by using predicates (which depend on variables) and quantifiers (which specify how broadly a statement applies, such as to all or some elements in a domain).

### Quantifiers Are Like Closures in JavaScript

Quantifiers in logic behave much like closures in JavaScript:

- **Each quantifier introduces a variable with its own scope**, and the **order of quantifiers matters**, because later quantifiers can **depend on** or **capture** the earlier ones.
- Similarly, in JavaScript, **closures capture variables from their defining environment**, and what a closure can "see" depends on **where and when** it was defined.

Just like:

- A function defined **inside a scope** has access to variables declared **outside** it,
- A quantifier can "see" the variables introduced by the quantifiers **before** it.

> 💡 In both systems, the **position determines visibility and dependency.**

### Domain

The nonempty set of elements that a variable range over, for example N for natural numbers.

# implication propositions

- Used for what ?
- apparently it can creates trivial propositions (insignificant)

| It rains (A) | I bring umbrella (B) | "If it rains → I bring umbrella"                |
| ------------ | -------------------- | ----------------------------------------------- |
| ✅ Yes       | ✅ Yes               | ✅ You kept your promise                        |
| ✅ Yes       | ❌ No                | ❌ You broke your promise                       |
| ❌ No        | ✅ Yes               | ✅ You didn’t promise anything, but that’s fine |
| ❌ No        | ❌ No                | ✅ Still fine — no rain, no expectation         |

## Compound propositions

### Implication

An implication is true exactly when the if-part is false or the then-part is true

### Propositional Formula

A propositional formula is a logical expression made up of propositional variables (like PP, QQ, and RR) combined using logical connectives such as:

- AND ( ∧ )

- OR ( ∨ )

- NOT ( ¬ )

- IMPLIES ( → )

- IFF ( ↔, “if and only if”)

Each propositional variable represents a statement that can be either true (T) or false (F).

A formula becomes valid if it always evaluates to true, regardless of the truth values assigned to its variables.

# Predicate Formula

A predicate formula (also called a first-order logic formula) is like a more powerful version of a propositional formula.
It allows:

- Variables (like x,yx,y)
- Predicates that describe properties or relations, like:

  - P(x)P(x): “xx is a student”
  - P(x,y)P(x,y): “xx knows yy” (a binary predicate)

- Quantifiers:

  - ∀x: “for all xx” (universal quantifier)
  - ∃x: “there exists an xx” (existential quantifier)
