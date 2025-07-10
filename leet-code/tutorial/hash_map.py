text = "apple banana apple orange banana apple"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1


frequency["new key"] = "some value"
frequency["new key"] = "2"

print(frequency)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

# HashMaps are data structures used to store key value items with a very fast performance to lookup, insertions and deletions.