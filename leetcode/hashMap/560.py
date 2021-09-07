# 560. Subarray Sum Equals K
# 이런 문제는 주어지는 배열에 어떤 조건이 있는지 인터뷰어에게 질문할것
# 정렬된 배열인지, 음수가 포함되어있는지 등
# cumulative sum dift -> 해쉬 이용해서 풀이


class Solution:


# 틀린 코드
# 18라인 for문 내에서 해쉬를 미리 셋팅하면 안됨
# 자기값을 참조하게됨
# -1, k=0인경우 -1 - 0 = -1, 이때 -1 자기값이 해쉬에 있으면 cnt를 +하기 때문
# def subarraySum(self, nums: list[int], k: int) -> int:
#     ch = dict()
#     idx = 0
#     ch[nums[0]] = [idx]
#
#     cumulative_sum = [nums[0]]
#
#     # o(n)
#     for i in nums[1:]:
#         idx += 1
#         cumulative_sum.append(cumulative_sum[-1] + i)
#
#         if ch.get(cumulative_sum[-1]) is not None:
#             ch[cumulative_sum[-1]].append(idx)
#         else:
#             ch[cumulative_sum[-1]] = [idx]
#
#     cnt = 0
#
#     print(ch)
#     print(cumulative_sum)
#
#     for cml_sum in cumulative_sum:
#         target = cml_sum - k
#         if target in ch:
#             cnt += len(ch[target])
#
#     return cnt


    def subarraySum(self, nums: list[int], k: int) -> int:
        cml_sums = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            cml_sums.append(tmp_sum)

        table = {}
        count = 0
        table[0] = [1]

        for idx, cml_sum in enumerate(cml_sums):
            target = cml_sum - k
            if target in table:
                count += len(table[target])

            if cml_sum not in table:
                table[cml_sum] = [idx]
            else:
                table[cml_sum].append(idx)

        return count


print(Solution.subarraySum('', [6, 3, 2, 5, 3, -3], 10))
print(Solution.subarraySum('', [6, 10, 4, 6, 4], 10))
print(Solution.subarraySum('', [1, 1, 1], 2))
print(Solution.subarraySum('', [1], 0))
print(Solution.subarraySum('', [-1, -1, 1], 0))  # 1 -> -1, 1
