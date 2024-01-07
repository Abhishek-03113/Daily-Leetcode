def is_valid(mid):
            count = 0
            current_sum = 0

            for i in range(N):
                current_sum += arr[i]

                if current_sum > mid:
                    count += 1
                    current_sum = arr[i]

            count += 1  # Count the last subarray
            return count <= K

        def minimum_maximum_subarray_sum():
            low = max(arr)
            high = sum(arr)
            result = float('inf')

            while low <= high:
                mid = low + (high - low) // 2

                if is_valid(mid):
                    result = min(result, mid)
                    high = mid - 1
                else:
                    low = mid + 1

            return result

        return minimum_maximum_subarray_sum()
