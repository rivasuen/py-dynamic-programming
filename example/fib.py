##########################
# FIBONACCI
#
# Init value:
# fib(1) =1
# fib(2) = 1
# So, if n <=2, return 1
#
# fib(5) = fib(4) + fib(3)
# fib(5) = fib(5-1) + fib(5-2)
##########################
def fib(n):
    # O(2^n) time
    # O(n) space
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)


def fibMemo(n, memo={}):
    # O(n) time
    # O(n) space
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibMemo(n - 1) + fibMemo(n - 2)
    return memo[n]


def fibTabulation(n):
    # O(n) time
    # O(n) space
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        if i + 1 <= n: table[i + 1] += table[i]
        if i + 2 <= n: table[i + 2] += table[i]

    return table[n]


def fibDemo():
    n1, ans1 = 7, 13
    n2, ans2 = 8, 21
    n3, ans3 = 50, 12586269025
    print("### fibDemo ###")
    print("Brute Force:")
    printDemo(n1, fib(n1), ans1)
    print("Memoization:")
    printDemo(n1, fibMemo(n1), ans1)
    printDemo(n2, fibMemo(n2), ans2)
    printDemo(n3, fibMemo(n3), ans3)
    print("Tabulation:")
    printDemo(n1, fibTabulation(n1), ans1)
    printDemo(n2, fibTabulation(n2), ans2)
    printDemo(n3, fibTabulation(n3), ans3)
    print("##########################")


def printDemo(val, res, ans):
    print(val, ": ", res, "(", ans, ")")
