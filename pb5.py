

def LCS(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_position = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i

    longest_common_substr = str1[end_position - max_length:end_position]

    return longest_common_substr

# Example usage:
str1 = "intelligent"
str2 = "inconsidered"
result = LCS(str1, str2)
print(result) 


str1 = "russian"
str2 = "ukrainian"
result = LCS(str1, str2)
print(result) 

str1 = "war"
str2 = "love"
result = LCS(str1, str2)
print(result) 
str1 = "romanian"
str2 = "roman"
result = LCS(str1, str2)
print(result) 


str1 = "intelligent"
str2 = "ingenious"
result = LCS(str1, str2)
print(result) 
str1 = "philosophically"
str2 = "zoophilous"
result = LCS(str1, str2)
print(result) 