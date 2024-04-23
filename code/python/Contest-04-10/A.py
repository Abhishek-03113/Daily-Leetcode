def can_be_eighth_power(arr):
    count_of_2 = arr.count(2)
    return count_of_2 % 8 == 0

def main():
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        if can_be_eighth_power(arr):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
