from collections import deque


def create(n):
    result = deque([1])
    for i in range(2, n+1):
        if i % 2 == 0:
            result.append(i)
        else:
            result.appendleft(i)
    return list(result)


if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]
