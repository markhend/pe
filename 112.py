n = 101
bounce_cnt = 1.0
while bounce_cnt/n < .99:
    inc = dec = same = 1
    n += 1
    s = str(n)
    for i in range(len(s)-1):
        if s[i+1] > s[i]:
            dec = 0
            same = 0
        if s[i+1] < s[i]:
            inc = 0
            same = 0
    if inc == 0 and dec == 0 and same == 0:
        bounce_cnt += 1
##        print n, "is bouncy"
##    else:
##        print n, "is not bouncy"
print n


##Working from left-to-right if no digit is exceeded by the digit
##to its left it is called an increasing number; for example, 134468.
##Similarly if no digit is exceeded by the digit to its right
##it is called a decreasing number; for example, 66420.
##We shall call a positive integer that is neither increasing
##nor decreasing a "bouncy" number; for example, 155349.
##Clearly there cannot be any bouncy numbers below one-hundred,
##but just over half of the numbers below one-thousand (525) are bouncy.
##In fact, the least number for which the proportion of bouncy numbers
##first reaches 50% is 538.
##Surprisingly, bouncy numbers become more and more common and
##by the time we reach 21780 the proportion of bouncy numbers is
##equal to 90%.
##Find the least number for which the proportion of bouncy numbers
##is exactly 99%.
