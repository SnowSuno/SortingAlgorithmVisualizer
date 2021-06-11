NAME = 'Selection Sort'
INFO = 'Time complexity\n' \
       '  Ω(n²)\n  Θ(n²)\n  O(n²)\n\n' \
       'Space complexity\n' \
       '  O(1)'

def sort(s):
    for rep in range(len(s) - 1):
        min_index = rep
        for i in range(rep + 1, len(s)):
            if s[i] < s[min_index]:
                min_index = i
            # yield
        s[rep], s[min_index] = s[min_index], s[rep]
        yield
