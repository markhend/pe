# deck = Array{String}(undef,52)
numbers = "23456789TJQKA"
suits = "CDHS"
deck = [x*y for x in numbers for y in suits]
f = open("54.txt", "r")
hands = readlines(f)
close(f)

