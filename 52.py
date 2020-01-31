''' It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. '''

n = 1
while True:
    s = set("".join(sorted(str(n*x))) for x in range(1, 7))
    if len(s) == 1:
        print(n)
        break
    n += 1
