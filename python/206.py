''' Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit. '''

s = "1_2_3_4_5_6_7_8_9_0"
# print(s[::2])
lo = int(1020304050607080900**0.5 / 10) * 10
hi = int(1929394959697989990**0.5 / 10 + 1) * 10
# print(lo, hi)
# print(lo*lo, hi*hi)

for n in range(lo, hi, 10):
    if str(n*n)[::2] == '1234567890':
        print(n)
        break
