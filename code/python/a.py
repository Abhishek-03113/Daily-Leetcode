from collections import Counter


def getResources(inc, dec, n, performance):
    num_servers = len(performance)
    resources = [0] * num_servers

    ranks = []
    for i in range(num_servers):

        unique_values = set()
        for p in performance:
            if p >= performance[i]:
                unique_values.add(p)
        ranks.append(len(unique_values))

    rank_counts = {}
    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    for i in range(num_servers):
        resources[i] = inc * (n + 1 - ranks[i]) - dec * rank_counts[ranks[i]]

    return resources


inc = 200
dec = 50
n = 5
performance = [2, 1, 3 ,3 ,1] 
print(getResources(inc, dec, n, performance))
