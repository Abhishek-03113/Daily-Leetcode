def solve_test_case(N, K, constraints):

    arr = [N] * N

    for L, R, m in constraints:
        L -= 1
        R -= 1

        if min(arr[L:R+1]) <= m:

            if m > 1:
                arr[L] = m - 1
            else:

                can_fix = False
                for i in range(L, R + 1):
                    if arr[i] == m:
                        if m + 1 <= N:
                            arr[i] = m + 1
                        can_fix = True
                        break
                if not can_fix:
                    return [-1]

    for L, R, m in constraints:
        L -= 1
        R -= 1
        if min(arr[L : R + 1]) == m:
            return [-1]

    return arr


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
