# 88. Merge Sorted Array
# 포인터 3개 이용

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1

        while idx1 >= 0 and idx2 >= 0:

            if nums1[idx1] > nums2[idx2]:
                nums1[i] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[i] = nums2[idx2]
                idx2 -= 1
            i -= 1

        while idx2 >=0:
            nums1[i] = nums2[idx2]
            idx2 -= 1
            i -= 1

        print(nums1)

print(Solution.merge('', [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution.merge('', [1], 1, [], 0))
print(Solution.merge('', [0], 0, [1], 1))
