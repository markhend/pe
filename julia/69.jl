function prime_factors(n)
    factors = intset()
    d = 2
    while n > 1
        while n%d == 0
            add(factors,d)
            n /= d
        end
        d += 1
    end
    factors
end

#function phi(n)
#    sum = 0
#    for k=1:n
#       sum += gcd(k,n)*cos(two_pi*k/n)
#    end
#    C[n] = sum
#    sum
#end

function euler_phi(n)
    F = prime_factors(n)
    result = n
    for p in F
        result *= (1-1/p)
    end
    result
end
            
answer = 0
number = 0

for i=30030:30030:1e6
    tmp = i/euler_phi(i)
    if tmp > answer
        answer = tmp
        number = i
    end
end

println(number,' ', answer)

# Started with i=1:1000 and max is 210
# With i=1:10000 max is 2310
# With i=1:100000 max is 30030
# 210|2310|30030 so I checked multiples of 30030 and got max at 510510
# 510510 = 2*3*5*7*11*13*17
