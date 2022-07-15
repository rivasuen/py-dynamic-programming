##########################
# Travel a 2D Grid, can move down and right
#
# Base case:
# (0,0) or (0,x) or (x,0) = 0
# (1,1) = 1
##########################
def gridTraveler(m, n):
    # O(2^n+m) time
    # O(n+m) space
    key = str(m) + ',' + str(n)
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)


def gridTravelerMemo(m, n, memo={}):
    # O(mn) time
    # O(m+n) space
    key = str(m) + ',' + str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[key] = gridTravelerMemo(m - 1, n) + gridTravelerMemo(m, n - 1)
    return memo[key]


def gridTabulation(m, n):
    # O(mn) time
    # O(mn) space
    table = [[0] * (n + 1) for i in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n: table[i][j + 1] += current
            if i + 1 <= m: table[i + 1][j] += current
    return table[m][n]


def gridTravelerDemo():
    m1, n1, ans1 = 3, 2, 3
    m2, n2, ans2 = 2, 3, 3
    m3, n3, ans3 = 18, 18, 2333606220
    print("### gridTravelerDemo ###")
    print("Brute Force:")
    printDemo(m1, n1, gridTraveler(m1, n1), ans1)
    print("Memoization:")
    printDemo(m1, n1, gridTravelerMemo(m1, n1), ans1)
    printDemo(m2, n2, gridTravelerMemo(m2, n2), ans2)
    printDemo(m3, n3, gridTravelerMemo(m3, n3), ans3)
    print("Tabulation:")
    printDemo(m1, n1, gridTabulation(m1, n1), ans1)
    printDemo(m2, n2, gridTabulation(m2, n2), ans2)
    printDemo(m3, n3, gridTabulation(m3, n3), ans3)
    print("##########################")


def printDemo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
