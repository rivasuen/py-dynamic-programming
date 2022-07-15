##########################
# FIBONACCI
#
# Base case:
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
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo={}):
    # O(n) time
    # O(n) space
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


def fib_tabulation(n):
    # O(n) time
    # O(n) space
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        if i + 1 <= n:
            table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]

    return table[n]


def fib_demo():
    n1, ans1 = 7, 13
    n2, ans2 = 8, 21
    n3, ans3 = 50, 12586269025
    print("### fibDemo ###")
    print("Brute Force:")
    print_demo(n1, fib(n1), ans1)
    print("Memoization:")
    print_demo(n1, fib_memo(n1), ans1)
    print_demo(n2, fib_memo(n2), ans2)
    print_demo(n3, fib_memo(n3), ans3)
    print("Tabulation:")
    print_demo(n1, fib_tabulation(n1), ans1)
    print_demo(n2, fib_tabulation(n2), ans2)
    print_demo(n3, fib_tabulation(n3), ans3)
    print("##########################")


def print_demo(val, res, ans):
    print(val, ": ", res, "(", ans, ")")
