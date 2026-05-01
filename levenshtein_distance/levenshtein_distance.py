def levenshtein_distance(s1: str | list[str], s2: str | list[str]) -> int:
    """
    莱文斯坦距离：插入 / 删除 / 替换 最少编辑次数
    dp[i][j] : s1 前 i 个字符 与 s2 前 j 个字符的编辑距离

    动态规划公式：
    边界条件
    if j == 0: dp[i][0] = i
    if i == 0: dp[0][j] = j

    字符相等
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1]

    字符不相等
    dp[i][j] = 1 + min(
        dp[i-1][j],   # 删除 s1 字符
        dp[i][j-1],   # 插入 s2 字符
        dp[i-1][j-1]  # 替换字符
    )
    """
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # print(dp)
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    a = ["1", "2"]
    b = ["1", "2"]
    print(levenshtein_distance(a, b))  # 0

    # 一个替换
    a = ["1", "2"]
    b = ["1", "X"]
    print(levenshtein_distance(a, b))  # 1

    # 两个替换 + 一个插入
    a = ["import os", "print(123)"]
    b = ["import sys", "print(666)", "test"]
    print(levenshtein_distance(a, b))  # 3 ✅
