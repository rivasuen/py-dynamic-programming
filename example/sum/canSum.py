##########################
# Is it possible to generate the targetSum by using numbers from array?
# return True/False
#
# Base case:
# if targetSum == 0, return True
# if targetSum < 0, return False
#
# targetSum = 7, nums = [5, 4, 3, 7]
# 7 - 5 = 2; 2 - 4 = -2 -> False
# 7 - 4 = 3; 3 - 3 = 0 -> True
##########################
# m = target sum
# n = array length
def canSum(targetSum, nums):
    # O(n^m) time
    # O(m) space
    if targetSum == 0: return True
    if targetSum < 0: return False
    for num in nums:
        remainder = targetSum - num
        if canSum(remainder, nums):
            return True

    return False


def canSumMemo(targetSum, nums, memo={}):
    # O(mn) time
    # O(m) space
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    for num in nums:
        remainder = targetSum - num
        if canSumMemo(remainder, nums):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


def canSumTabulation(targetSum, nums):
    # O(mn) time
    # O(m) space
    table = [False] * (targetSum + 1)
    table[0] = True
    for i in range(targetSum + 1):
        if table[i] is True:
            for num in nums:
                if i + num <= targetSum:
                    table[i + num] = True
    return table[targetSum]


def canSumDemo():
    m1, n1, ans1 = 7, [2, 4], False
    m2, n2, ans2 = 8, [2, 3, 5], True
    m3, n3, ans3 = 100, [7, 14], False
    print("### canSumDemo ###")
    print("Brute Force:")
    printDemo(m1, n1, canSum(m1, n1), ans1)
    print("Memoization:")
    printDemo(m1, n1, canSumMemo(m1, n1), ans1)
    printDemo(m2, n2, canSumMemo(m2, n2), ans2)
    printDemo(m3, n3, canSumMemo(m3, n3), ans3)  # BUG: Dict pass by value
    print("Tabulation:")
    printDemo(m1, n1, canSumTabulation(m1, n1), ans1)
    printDemo(m2, n2, canSumTabulation(m2, n2), ans2)
    printDemo(m3, n3, canSumTabulation(m3, n3), ans3)
    print("##########################")


def printDemo(val1, val2, res, ans):
    print(val1, ",", val2, ": ", res, "(", ans, ")")
