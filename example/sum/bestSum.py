##########################
# Return an array containing the SHORTEST combination of numbers that add up to exactly the target_sum
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

def best_sum(target_sum, nums):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in nums:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, nums)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    return shortest_combination


def best_sum_memo(target_sum, nums, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None
    shortest_combination = None
    for num in nums:
        remainder = target_sum - num
        remainder_combination = best_sum_memo(remainder, nums)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination


def best_sum_tabulation(target_sum, nums):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target_sum:
                    combination = [*table[i], num]
                    if table[i + num] is None or len(combination) < len(table[i + num]):
                        table[i + num] = combination
    return table[target_sum]


def best_sum_demo():
    m1, n1, ans1 = 7, [5, 3, 4, 7], [7]
    m2, n2, ans2 = 8, [1, 4, 5], [4, 4]
    m3, n3, ans3 = 100, [1, 2, 5, 25], [25, 25, 25, 25]
    print("### bestSumDemo ###")
    print("Brute Force:")
    print_demo(m1, n1, best_sum(m1, n1), ans1)
    print_demo(m2, n2, best_sum(m2, n2), ans2)
    print("Memoization:")
    print_demo(m1, n1, best_sum_memo(m1, n1), ans1)
    print_demo(m2, n2, best_sum_memo(m2, n2), ans2)
    print_demo(m3, n3, best_sum_memo(m3, n3), ans3)
    print("Tabulation:")
    print_demo(m1, n1, best_sum_tabulation(m1, n1), ans1)
    print_demo(m2, n2, best_sum_tabulation(m2, n2), ans2)
    print_demo(m3, n3, best_sum_tabulation(m3, n3), ans3)
    print("##########################")


def print_demo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
