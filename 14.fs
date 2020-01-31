let p14 = 
    let collatz n = 
        let rec loop n i = 
            match n with
            |n when n = 1I -> i
            |n when n%2I = 0I -> loop (n/2I) (i+1I)
            |n -> loop (3I*n+1I) (i+1I)
        loop n 1I 
    [1I..1000000I]|> Seq.maxBy collatz