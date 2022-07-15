##########################
# Is it POSSIBLE to generate the target_sum by using numbers from array?
# return True/False
#
# Base case:
# if target_sum == 0, return True
# if target_sum < 0, return False
#
# target_sum = 7, nums = [5, 4, 3, 7]
# 7 - 5 = 2; 2 - 4 = -2 -> False
# 7 - 4 = 3; 3 - 3 = 0 -> True
##########################
# m = target sum
# n = array length
def can_sum(target_sum, nums):
    # O(n^m) time
    # O(m) space
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums):
            return True

    return False


def can_sum_memo(target_sum, nums, memo={}):
    # O(mn) time
    # O(m) space
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in nums:
        remainder = target_sum - num
        if can_sum_memo(remainder, nums):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


def can_sum_tabulation(target_sum, nums):
    # O(mn) time
    # O(m) space
    table = [False] * (target_sum + 1)
    table[0] = True
    for i in range(target_sum + 1):
        if table[i] is True:
            for num in nums:
                if i + num <= target_sum:
                    table[i + num] = True
    return table[target_sum]


def can_sum_demo():
    m1, n1, ans1 = 7, [2, 4], False
    m2, n2, ans2 = 8, [2, 3, 5], True
    m3, n3, ans3 = 300, [7, 14], False
    print("### can_sumDemo ###")
    print("Brute Force:")
    print_demo(m1, n1, can_sum(m1, n1), ans1)
    print("Memoization:")
    print_demo(m1, n1, can_sum_memo(m1, n1), ans1)
    print_demo(m2, n2, can_sum_memo(m2, n2), ans2)
    print_demo(m3, n3, can_sum_memo(m3, n3), ans3)  # BUG: Dict pass by value
    print("Tabulation:")
    print_demo(m1, n1, can_sum_tabulation(m1, n1), ans1)
    print_demo(m2, n2, can_sum_tabulation(m2, n2), ans2)
    print_demo(m3, n3, can_sum_tabulation(m3, n3), ans3)
    print("##########################")


def print_demo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
