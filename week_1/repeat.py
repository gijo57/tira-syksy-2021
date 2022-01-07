def find(s):
    shortest_substring_length = len(s)
    for i in range(len(s), 0, -1):
        substring = s[:i]
        factor = int(len(s)/len(substring))
        if (substring*factor == s and len(substring) < shortest_substring_length):
            shortest_substring_length = len(substring)
    return shortest_substring_length


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
