def solve(n, m, k, weeds):
  """
  Solves the herbicide problem.

  Args:
    n: The number of weeds.
    m: The total number of days.
    k: The number of sprays needed to kill a weed.
    weeds: The days on which new weeds show up.

  Returns:
    "Yes" if all the weeds are gone after m days, and "No" otherwise.
  """

  weed_spray_counts = [0] * n
  for day in range(m):
    for i in range(n):
      if weeds[i] <= day and weed_spray_counts[i] < k:
        weed_spray_counts[i] += 1
  for count in weed_spray_counts:
    if count < k:
      return "No"
  return "Yes"


def main():
  """
  The main function.
  """

  t = int(input())
  for _ in range(t):
    n, m, k = map(int, input().split())
    weeds = list(map(int, input().split()))
    print(solve(n, m, k, weeds))


if __name__ == "__main__":
  main()
