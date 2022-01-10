def area(rec1, rec2, rec3):
    recs = [rec1, rec2, rec3]
    total_area = 0
    overlaps = []
    for rec in recs:
        total_area += calculate_area(rec)
    for i in range(len(recs)-1):
        overlap = calculate_overlap(rec, recs[i])
        overlaps.append(overlap)
    # print(total_area, overlaps)
    return total_area - sum([x[0] for x in overlaps])


def calculate_overlap(rec1, rec2):
    x_start = min(rec1[2], rec2[2])
    x_end = max(rec1[0], rec2[0])
    y_start = min(rec1[1], rec2[1])
    y_end = max(rec1[3], rec2[3])
    overlap_x = x_start - x_end
    overlap_y = y_start - y_end
    print('x', x_start, x_end, overlap_x)
    print('y', y_start, y_end, overlap_y)
    if overlap_x > 0 and overlap_y > 0:
        return overlap_x * overlap_y, (x_start, x_end, y_start, y_end)
    return 0, 0


def calculate_area(rec):
    return abs(rec[2] - rec[0]) * abs(rec[3] - rec[1])


if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    rec4 = [1,2,3,0]
    rec5 = [-3,2,1,-3]
    rec6 = [-2,-2,2,-3]
    rec7 = [0,3,3,2]
    rec8 = [-1,3,2,-3]
    rec9 = [-1,0,1,-3]
    print(area(rec1, rec2, rec3))  # 16
    print(area(rec4, rec5, rec6))  # 25
    print(area(rec7, rec8, rec9))  # 19
