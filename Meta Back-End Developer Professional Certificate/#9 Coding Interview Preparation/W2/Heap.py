import heapq

# Create a min heap
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)

print("Min Heap:", min_heap)

# Remove the smallest element
smallest = heapq.heappop(min_heap)
print("Smallest element:", smallest)
print("Min Heap after removing the smallest element:", min_heap)

# Create a max heap using min heap with negative values
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)

print("Max Heap (using negation):", [-x for x in max_heap])

# Remove the largest element (remember to negate it back)
largest = -heapq.heappop(max_heap)
print("Largest element:", largest)
print("Max Heap after removing the largest element:", [-x for x in max_heap])
