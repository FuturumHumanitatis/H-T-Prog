# Theory of Nicomah
def nicomah_func(start, n):
    return int((start + n) * (n - 1) / 2) ** 2


n = 16 ** 9
start = 2

print(sum(map(int, list(str(nicomah_func(start, n))))))
