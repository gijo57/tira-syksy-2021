def count(t):
    n = len(t)
    left_maxes = [0]*n
    right_mins = [0]*n
    left_maxes[0] = t[0]
    right_mins[-1] = t[-1]

    for i in range(1, n):
        if t[i] > left_maxes[i-1]:
            left_maxes[i] = t[i]
        else:
            left_maxes[i] = left_maxes[i-1]

    for i in range(n-2, -1, -1):
        if t[i] < right_mins[i+1]:
            right_mins[i] = t[i]
        else:
            right_mins[i] = right_mins[i+1]

    splits = 0
    for i in range(len(t)-1):
        if left_maxes[i] < right_mins[i+1]:
            splits += 1
    return splits


if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([1,2,3,1])) # 0
