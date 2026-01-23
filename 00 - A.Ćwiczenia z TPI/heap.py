heap = list(range(15))

parent = 0
children = (2*parent + 1, 2*parent + 2)
print(parent, children)

parent = 0
child = 2*parent + 1
grandchild = 2*child + 1
grandgrandchild = 2*grandchild + 1
print(parent, child, grandchild, grandgrandchild)

print([2**k - 1 for k in range(4)])
print((15).bit_length())

def generations(heap):
    n_gens = len(heap).bit_length()
    return [heap[2**k - 1: 2**(k+1) - 1] for k in range(4)]

def print_heap(heap, itemwidth = 4):
    levels = generations(heap)
    width = 2**len(levels) * itemwidth
    for level in levels:
        for item in level:
            item = str(item)
            item = f'{item:_^{width // 2 - 1}}'
            print(f"{item: ^{width}}", end='')
        print()
        width //= 2

print_heap(heap)


# x = 123
# y = 20
# print(f"{x:_^{y}}")

import random

heap = random.sample(range(15), 15)
print(heap)

print_heap(heap)

import heapq

heapq.heapify(heap)
print_heap(heap)

heapq.heappop(heap)
print_heap(heap)


heap = []
for x in random.sample(range(15), 15):
    heapq.heappush(heap, x)
    print('PUSH', x)
    print_heap(heap)
    print("_" * 80)

while heap:
    heapq.heappop(heap)
    print('POP', heap)
    print_heap(heap)
    print("_" * 80)


class PriorityQueue:
    def __init__(self):
        self.heap = []
    def add(self, item, priority):
        heapq.heappush(self.heap, [priority, item])

# PORZADEK LEKSYKOGRAFICZNY - PORZADEK SORTOWANIA STRINGÓW
# SORTOWANIE LEKSYKOGRAFICZNE

    def pop(self):
        if self.heap:
            _, item = heapq.heappop(self.heap)
            return item
        raise IndexError
    
pq = PriorityQueue()
pq.add('Buy grocery', 1)
pq.add('Pay rent', 2)
pq.add('Study AI', 10)
print_heap(pq.heap, 15)
