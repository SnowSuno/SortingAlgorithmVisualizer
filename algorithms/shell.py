NAME = 'Shell Sort'
INFO = 'Time complexity\n' \
       '  Ω(n log(n))\n  Θ(n log(n)²)\n  O(n log(n)²)\n\n' \
       'Space complexity\n' \
       '  O(1)'

def sort(s):
    skip_index = (5, 3, 1)

    for k in skip_index:
        for _ in skip_insertion_sort(s, k):
            yield

def skip_insertion_sort(s, k):
    for i in range(len(s)):
        while i >= k:
            if s[i - k] <= s[i]:
                break

            s[i - k], s[i] = s[i], s[i - k]
            yield
            i -= k
