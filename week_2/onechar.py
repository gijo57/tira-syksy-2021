def count(s):
    substrings = 0
    length = 0
    for i in range(len(s)):
        if i != 0 and s[i] == s[i-1]:
            length += 1
        else:
            length = 1
        substrings += length
    return substrings


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abbbcaa"))  # 11
    print(count("abcde"))  # 5
