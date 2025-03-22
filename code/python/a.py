def compute_mex(a, l, r):
    present = [False] * 4
    for i in range(l, r + 1):
        if a[i] < 4:
            present[a[i]] = True

    for x in range(4):
        if not present[x]:
            return x
    return 4


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ops = []

    while len(a) > 3:
        has_zero = any(x == 0 for x in a)

        if has_zero:
            pos = next((i for i, x in enumerate(a) if x == 0), -1)

            if pos == 0:
                m = compute_mex(a, 0, 1)
                ops.append((1, 2))
                a = [m] + a[2:]
            else:
                m = compute_mex(a, pos - 1, pos)
                ops.append((pos, pos + 1))
                a = a[: pos - 1] + [m] + a[pos + 1 :]
        else:
            m = compute_mex(a, 0, len(a) - 1)
            ops.append((1, len(a)))
            a = [m]
            break

        if len(a) == 3:
            p = compute_mex(a, 0, 1)
            if p != 0 and a[2] != 0:
                ops.append((1, 2))
                a = [p, a[2]]
            else:
                q = compute_mex(a, 1, 2)
                if a[0] != 0 and q != 0:
                    ops.append((2, 3))
                    a = [a[0], q]
                else:
                    ops.append((1, 3))
                    m = compute_mex(a, 0, 2)
                    a = [m]

        if len(a) == 2:
            m = compute_mex(a, 0, 1)
            ops.append((1, 2))
            a = [m]

    print(len(ops))
    for op in ops:
        print(op[0], op[1])


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
