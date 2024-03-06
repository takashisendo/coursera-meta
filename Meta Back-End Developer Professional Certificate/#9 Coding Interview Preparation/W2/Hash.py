# Given array
numbers = [1,45,5,34,23,5,82,12,35,21,8,9]
# Hashing function modulus 7
hashes = [number % 7 for number in numbers]
# Count occurrences of each hash
hash_counts = {}
for hash_value in hashes:
    if hash_value in hash_counts:
        hash_counts[hash_value] += 1
    else:
        hash_counts[hash_value] = 1
# Count collisions (occurrences more than 1)
collisions = sum(count - 1 for count in hash_counts.values() if count > 1)
print(collisions)
