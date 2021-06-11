NAME = 'Merge Sort'
INFO = 'Time complexity\n' \
       '  Ω(n log(n))\n  Θ(n log(n))\n  O(n log(n))\n\n' \
       'Space complexity\n' \
       '  O(n)'

def sort(visual):
    s = visual[:]
    for _ in merge_sort(s, visual, 0):
        yield

def merge_sort(s, visual, start_index):
    n = len(s)
    if n == 1:
        yield
        return
    mid_index = n // 2

    s1, s2 = s[:mid_index], s[mid_index:]
    # for sub_s in (s1, s2):
    for _ in merge_sort(s1, visual, start_index):
        yield
    for _ in merge_sort(s2, visual, start_index+mid_index):
        yield

    for _ in merge(s1, s2, s, visual, start_index):
        yield


def merge(s1, s2, s, visual, start_index):
    i1 = i2 = 0
    while i1 + i2 < len(s):
        if i2 == len(s2) or (i1 < len(s1) and s1[i1] < s2[i2]):
            s[i1 + i2] = s1[i1]
            visual[start_index + i1 + i2] = s1[i1]
            i1 += 1
        else:
            s[i1 + i2] = s2[i2]
            visual[start_index + i1 + i2] = s2[i2]
            i2 += 1
        yield


if __name__ == '__main__':
    L = [9, 4, 5, 7, 3, 6, 2, 1, 8]
    # L = [2, 1]
    for _ in sort(L):
        pass
    print(L)
