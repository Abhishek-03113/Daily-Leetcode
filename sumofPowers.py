smallest_prime_factor = [i for i in range(end + 1)]
        for i in range(2, int(end**0.5) + 1):
            if smallest_prime_factor[i] == i:
                for j in range(i*i, end + 1, i):
                    smallest_prime_factor[j] = i
        distinct_prime_factors_count = 0
        for num in range(start, end + 1):
            while num > 1:
                distinct_prime_factors_count += 1
                num //= smallest_prime_factor[num]
        return distinct_prime_factors_count
