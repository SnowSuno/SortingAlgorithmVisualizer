NAME = 'Insertion Sort'
INFO = 'Time complexity\n' \
       '  Ω(n)\n  Θ(n²)\n  O(n²)\n\n' \
       'Space complexity\n' \
       '  O(1)'

def sort(s):
    for i in range(1, len(s)):
        while i != 0:
            if s[i - 1] <= s[i]:
                break

            s[i - 1], s[i] = s[i], s[i - 1]
            i -= 1
            yield

