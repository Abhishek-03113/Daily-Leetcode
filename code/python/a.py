import sys

def process_test_case(N, P, A):
    left_max = [float('-inf')] * N
    nearest_left = -1
    current_max = 0
    for i in range(N):
        if A[i] == 0:
            nearest_left = i
            current_max = 0
            left_max[i] = 0
        else:
            if nearest_left != -1:
                current_max = max(current_max, A[i])
                left_max[i] = current_max

    right_max = [float('-inf')] * N
    nearest_right = -1
    current_max = 0
    for i in range(N-1, -1, -1):
        if A[i] == 0:
            nearest_right = i
            current_max = 0
            right_max[i] = 0
        else:
            if nearest_right != -1:
                current_max = max(current_max, A[i])
                right_max[i] = current_max

    result = []
    for i in range(N):
        if A[i] == 0:
            result.append(0)
        else:
            x_left = None
            if left_max[i] != float('-inf'):
                x_left = max(A[i], left_max[i])
            x_right = None
            if right_max[i] != float('-inf'):
                x_right = max(A[i], right_max[i])
            
            X = float('inf')
            if x_left is not None:
                X = x_left
            if x_right is not None:
                if x_right < X:
                    X = x_right
            
            t = (X + P - 1) // P
            result.append(t)
    return result

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, P = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        res = process_test_case(N, P, A)
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()