def generate(n):
    result = 0
    num_index = 0
    while num_index < n:
        result += 1
        if len(set(str(result))) < len(str(result)):
            num_index += 1
    return result


if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505
