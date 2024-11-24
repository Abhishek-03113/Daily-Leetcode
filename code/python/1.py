def solve_test_case(N, K, constraints):
    forbidden_values = [set() for _ in range(N)]  # positions 0 to N-1
    for L, R, m in constraints:
        L -= 1
        R -= 1
        for i in range(L, R + 1):
            forbidden_values[i].add(m)
    A = [0] * N
    for i in range(N):
        for v in range(1, N + 1):
            if v not in forbidden_values[i]:
                A[i] = v
                break
        else:
            return [-1]
    return A

def solve_all_cases(T, test_cases):
    results = []
    for N, K, constraints in test_cases:
        result = solve_test_case(N, K, constraints)
        results.append(result)
    return results

def process_input():
    T = int(input())
    test_cases = []
    for _ in range(T):
        N, K = map(int, input().split())
        constraints = []
        for _ in range(K):
            L, R, m = map(int, input().split())
            constraints.append((L, R, m))
        test_cases.append((N, K, constraints))
    return T, test_cases

def main():
    T, test_cases = process_input()
    results = solve_all_cases(T, test_cases)

    for result in results:
        if result[0] == -1:
            print(-1)
        else:
            print(*result)

if __name__ == "__main__":
    main()