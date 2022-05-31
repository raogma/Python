def get_magic_triangle(n):
    res = [[1], [1, 1]]
    prev = [1, 1]
    for _ in range(n - 2):
        new = [1, 1]
        for i in range(len(prev) - 1):
            num = prev[i] + prev[i + 1]
            new.insert(i + 1, num)
        res.append(new)
        prev = new
    return res


get_magic_triangle(5)