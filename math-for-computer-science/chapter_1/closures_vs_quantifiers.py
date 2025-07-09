americans = ["Alice", "Bob", "Charlie"]
dreams = ["be a rockstar", "own a farm", "travel the world"]

print("=== ∃d. ∀a. H(a, d) ===")
# Shared dream (like ∃d. ∀a. H(a, d))
def shared_dream_factory():
    d = "own a home"  # chosen once, fixed for all

    def dream_for_all():
        # we need to understand lambda
        return lambda a: f"{a} has the shared dream: {d}"
    
    return dream_for_all()

shared_dream = shared_dream_factory()
for a in americans:
    print(shared_dream(a))


print("\n=== ∀a. ∃d. H(a, d) ===")
# Personalized dream (like ∀a. ∃d. H(a, d))
def personalized_dream_factory():
    def dream_for_each(a):
        # pick a personal dream — here, indexed for simplicity
        d = dreams[americans.index(a)]
        return f"{a} has their personal dream: {d}"
    
    return dream_for_each

personalized_dream = personalized_dream_factory()
for a in americans:
    print(personalized_dream(a))
