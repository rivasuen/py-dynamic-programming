##########################
# Travel a 2D Grid, can move down and right
#
# Base case:
# (0,0) or (0,x) or (x,0) = 0
# (1,1) = 1
##########################
def grid_traveler(m, n):
    # O(2^n+m) time
    # O(n+m) space
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def grid_traveler_memo(m, n, memo={}):
    # O(mn) time
    # O(m+n) space
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler_memo(m - 1, n) + grid_traveler_memo(m, n - 1)
    return memo[key]


def grid_tabulation(m, n):
    # O(mn) time
    # O(mn) space
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current
    return table[m][n]


def grid_traveler_demo():
    m1, n1, ans1 = 3, 2, 3
    m2, n2, ans2 = 2, 3, 3
    m3, n3, ans3 = 18, 18, 2333606220
    print("### grid_traveler_demo ###")
    print("Brute Force:")
    print_demo(m1, n1, grid_traveler(m1, n1), ans1)
    print("Memoization:")
    print_demo(m1, n1, grid_traveler_memo(m1, n1), ans1)
    print_demo(m2, n2, grid_traveler_memo(m2, n2), ans2)
    print_demo(m3, n3, grid_traveler_memo(m3, n3), ans3)
    print("Tabulation:")
    print_demo(m1, n1, grid_tabulation(m1, n1), ans1)
    print_demo(m2, n2, grid_tabulation(m2, n2), ans2)
    print_demo(m3, n3, grid_tabulation(m3, n3), ans3)
    print("##########################")


def print_demo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
