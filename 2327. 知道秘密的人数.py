"""
在第 1 天，有一个人发现了一个秘密。

给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 forget ，表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。

给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 109 + 7 取余 后返回。

示例 1：
输入：n = 6, delay = 2, forget = 4
输出：5
解释：
第 1 天：假设第一个人叫 A 。（一个人知道秘密）
第 2 天：A 是唯一一个知道秘密的人。（一个人知道秘密）
第 3 天：A 把秘密分享给 B 。（两个人知道秘密）
第 4 天：A 把秘密分享给一个新的人 C 。（三个人知道秘密）
第 5 天：A 忘记了秘密，B 把秘密分享给一个新的人 D 。（三个人知道秘密）
第 6 天：B 把秘密分享给 E，C 把秘密分享给 F 。（五个人知道秘密）
示例 2：

输入：n = 4, delay = 1, forget = 3
输出：6
解释：
第 1 天：第一个知道秘密的人为 A 。（一个人知道秘密）
第 2 天：A 把秘密分享给 B 。（两个人知道秘密）
第 3 天：A 和 B 把秘密分享给 2 个新的人 C 和 D 。（四个人知道秘密）
第 4 天：A 忘记了秘密，B、C、D 分别分享给 3 个新的人。（六个人知道秘密）
 

提示：
- 2 <= n <= 1000
- 1 <= delay < forget <= n
"""

"""
Attempt 1: Sep 9, 2025. 解法没有标答好，时间复杂度是 O(n * (forget-delay))。有很大一部分求和被重复统计了。
更好的做法应该是，只统计每一天刚刚得知消息的人数；这些人数足够 encode 所有信息，最后把符合条件的人数求一遍和就好。
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        cache = [1] * n
        for i in range(delay, len(cache)):
            init = 1 if i <= forget - 1 else 0
            cache[i] = (init + sum(cache[k] for k in range(max(0, i - forget + 1), i - delay + 1))) % int(1e9 + 7)
        return cache[-1]
    
sol = Solution()
print(sol.peopleAwareOfSecret(6, 2, 4))
print(sol.peopleAwareOfSecret(4, 1, 3))