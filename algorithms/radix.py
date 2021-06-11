NAME = 'Radix Sort'
INFO = 'Time complexity\n' \
       '  Ω(nk)\n  Θ(nk)\n  O(nk)\n\n' \
       'Space complexity\n' \
       '  O(n + k)'

def sort(s):
    max_digit = len(str(max(s)))

    prev = [[num] for num in s]
    for digit in range(max_digit-1, -1, -1):
        i = 0

        curr = [[] for _ in range(10)]
        for line in prev:
            for num in line:
                index = int(str(num).zfill(max_digit)[digit])
                curr[index].append(num)
                s[i] = num
                yield
                i += 1
        prev = curr

    i = 0
    for line in prev:
        for num in line:
            s[i] = num
            yield
            i += 1
