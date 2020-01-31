s = [s for s in "123456789"]

for i=1:factorial(length(s))
    A = nthperm(s,i)
    if A[1]+A[2]+A[3]==A[4]+A[3]+A[5]==A[6]+A[5]+A[7]==A[8]+A[7]+A[9]==58+A[9]+A[2]
        # println("sol at ",i)
        println(A[1],A[2],A[3],' ',A[4],A[3],A[5],' ',A[6],A[5],A[7],' ',
            A[8],A[7],A[9]," 10",A[9],A[2])
    end
end

