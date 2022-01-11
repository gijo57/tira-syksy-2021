def count(s):
    substrings = 0
    starts = {}
    for i in range(len(s)):
        if s[i] in starts:
            starts[s[i]] += 1
        else:
            starts[s[i]] = 1
        substrings += starts[s[i]]
    return substrings


if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10
