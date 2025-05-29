import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce


def solve():
    n, m = map(int, input().split())
    batteries = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    critical = set([0])

    for _ in range(m):
        s, t, w = map(int, input().split())
        graph[s].append((t, w))
        critical.add(w)

    critical = sorted(critical)

    pq = [(0, 1, 0)]
    best = {}

    while pq:
        final_batteries, checkpoint, current_batteries = heappop(pq)

        if checkpoint == n:
            print(final_batteries)
            return

        state_key = (checkpoint, current_batteries)
        if state_key in best and best[state_key] <= final_batteries:
            continue
        best[state_key] = final_batteries

        max_available = batteries[checkpoint - 1]
        targets = set([current_batteries])

        for threshold in critical:
            if current_batteries < threshold <= current_batteries + max_available:
                targets.add(threshold)

        if max_available > 0:
            targets.add(current_batteries + max_available)

        for target_batteries in targets:
            take = target_batteries - current_batteries
            if 0 <= take <= max_available:
                new_final = final_batteries + take

                for next_checkpoint, min_req in graph[checkpoint]:
                    if target_batteries >= min_req:
                        next_state = (next_checkpoint, target_batteries)
                        if next_state not in best or best[next_state] > new_final:
                            heappush(
                                pq, (new_final, next_checkpoint, target_batteries))

    print(-1)


for _ in range(int(input())):
    solve()
