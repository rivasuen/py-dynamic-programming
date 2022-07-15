##########################
# Return an array containing ANY combination of elements that add up to exactly the target_sum.
# If no combination, return None
#
# Base case:
# default = None
# if target_sum == 0, return []
#
# target_sum = 7, nums = [5, 4, 3, 7]
# 0 = 0 -> []
# 7 - 5 = 2; 2 - 4 = -2 -> None
# 7 - 4 = 3; 3 - 3 = 0 -> [4, 3]
##########################

def how_sum(target_sum, nums):
    # O(n^m *m) time
    # O(m) space
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in nums:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, nums)
        if remainder_result is not None:
            return [*remainder_result, num]  # [PY] *array = [JS] ...array
    return None


def how_sum_memo(target_sum, nums, memo={}):
    # O(n*m^2) time
    # O(m^2) space
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in nums:
        remainder = target_sum - num
        remainder_result = how_sum_memo(remainder, nums)
        if remainder_result is not None:
            memo[target_sum] = [*remainder_result, num]  # [PY] *array = [JS] ...array
            return memo[target_sum]
    memo[target_sum] = None
    return None


def how_sum_tabulation(target_sum, nums):
    # O(m^2n) time
    # O(m^2) space
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target_sum:
                    table[i + num] = [*table[i], num]
    return table[target_sum]


def how_sum_demo():
    m1, n1, ans1 = 7, [2, 4], None
    m2, n2, ans2 = 8, [2, 3, 5], [2, 2, 2, 2]
    m3, n3, ans3 = 300, [7, 14], None
    print("### how_sumDemo ###")
    print("Brute Force:")
    print_demo(m1, n1, how_sum(m1, n1), ans1)
    print_demo(m2, n2, how_sum(m2, n2), ans2)
    print("Memoization:")
    print_demo(m1, n1, how_sum_memo(m1, n1), ans1)
    print_demo(m2, n2, how_sum_memo(m2, n2), ans2)
    print_demo(m3, n3, how_sum_memo(m3, n3), ans3)
    print("Tabulation:")
    print_demo(m1, n1, how_sum_tabulation(m1, n1), ans1)
    print_demo(m2, n2, how_sum_tabulation(m2, n2), ans2)
    print_demo(m3, n3, how_sum_tabulation(m3, n3), ans3)
    print("##########################")


def print_demo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
