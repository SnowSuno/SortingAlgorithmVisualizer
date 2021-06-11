NAME = 'Bubble Sort'
INFO = 'Time complexity\n' \
       '  Ω(n)\n  Θ(n²)\n  O(n²)\n\n' \
       'Space complexity\n' \
       '  O(1)'

def sort(s):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(s) - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                s[i], s[i+1] = s[i+1], s[i]

            yield

