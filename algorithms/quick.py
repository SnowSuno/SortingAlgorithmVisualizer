NAME = 'Quick Sort'
INFO = 'Time complexity\n' \
       '  Ω(n log(n))\n  Θ(n log(n))\n  O(n²)\n\n' \
       'Space complexity\n' \
       '  O(log(n))'

def sort(s):
    return quick_sort(s, 0, len(s)-1)

def partition(s, low, high):
    i = (low - 1)
    pivot = s[high]

    for j in range(low, high):
        if s[j] <= pivot:

            i = i + 1
            s[i], s[j] = s[j], s[i]
        yield

    s[i + 1], s[high] = s[high], s[i + 1]
    yield i + 1

def quick_sort(s, low, high):
    if len(s) == 1:
        return
    if low < high:
        for pi in partition(s, low, high): yield

        for _ in quick_sort(s, low, pi - 1): yield
        for _ in quick_sort(s, pi + 1, high): yield
