from collections import defaultdict,deque
import math
class Solution:
    def solve(self, num1, num2):
        # Initialize the hashmap
        hmap = defaultdict(int)

        def is_prime(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        # Populate hashmap with prime numbers between 1000 and 9999
        for i in range(1000, 10000):
            if is_prime(i):
                hmap[i] = 1

        # BFS
        q = deque()
        num1 = str(num1)
        num2 = str(num2)

        q.append([num1, 0])
        visited = set()
        visited.add(num1)

        while q:
            n, count = q.popleft()

            if n == num2:
                return count

            for idx in range(4):
                for num in range(10):
                    if not idx and not num:
                        continue

                    s = n[:idx] + str(num) + n[idx + 1:]

                    if s in visited:
                        continue

                    if hmap[int(s)] == 1:
                        q.append([s, count + 1])
                        visited.add(s)

        return -1
