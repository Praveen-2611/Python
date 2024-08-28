import heapq
from collections import Counter

def longest_different_adjacent_sequence(S):
    # Step 1: Frequency Calculation
    freq = Counter(S)
    
    # Step 2: Max-Heap Construction
    # Using negative counts for max-heap effect with min-heap
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Building the Result
    prev_count, prev_char = 0, ''
    result = []
    
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)
        
        # If the previous character is still available, push it back
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))
        
        # Update previous character and its count
        prev_count, prev_char = count + 1, char
    
    return ''.join(result)
