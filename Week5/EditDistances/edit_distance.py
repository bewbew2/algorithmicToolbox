# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)

    dist = [[0 for _ in range(m+1)] for __ in range(n+1)]
    dist[0] = [i for i in range(m+1)]
    for j in range(n+1):
        dist[j][0] = j

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            ins = dist[i][j - 1] + 1
            dlt = dist[i - 1][j] + 1
            mat = dist[i - 1][j - 1]
            mma = dist[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                dist[i][j] = min(ins, dlt, mat)
            else:
                dist[i][j] = min(ins, dlt, mma)
    return dist[n][m]

    #write your code here
    return 0

if __name__ == "__main__":
    print(edit_distance(input(), input()))
