import sys
import heapq

# data = list(map(int, input().strip().split()))
data = list(map(int, sys.stdin.read().strip().split()))
N, L = data[0], data[1]
# T = [int(input()) for i in range(L)]
T = data[2:]

salesmen = [0] * N
queue = [(0, i) for i in range(N)]
heapq.heapify(queue)

for i in range(L):
    val, id = heapq.heappop(queue)
    val += T[i]
    salesmen[id] += 1
    heapq.heappush(queue, (val, id))
    
for i, calls in enumerate(salesmen):
    print(i+1, calls)



