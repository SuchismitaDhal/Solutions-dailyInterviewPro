def solve(scores, n):
    scores = sorted(scores)
    dp = [[0]*n for _ in range(n)]
    sol = 0

    for i in range(n):
        t = scores[0] + i + 1
        curr = 0
        visited = set()
        for j in range(n):
            d = t - scores[j]
            if d not in visited:
                dp[i][j] = 1
                visited.add(d)
                curr += 1
                sol = max(sol, curr)
    return sol


n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
print(solve(scores, n))
