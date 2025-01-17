
# https://leetcode.com/problems/the-kth-factor-of-n/solutions/6292118/finding-the-k-th-factor-of-a-number-by-h-k7rd/

"""
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

"""


def kthFactor(n: int, k: int) -> int:
    i = 1
    arr = []
    while  i <= n:
        factor = n % i
        if factor == 0:
            arr.append(i)

        print(factor)


        if len(arr) == k:
            print(arr)
            return i

        i += 1

    return -1

result = kthFactor(12, 3)
print(result)

result = kthFactor(7, 2)
print(result)

result = kthFactor(4, 4)
print(result)