ways [] = 1 : repeat 0
ways (coin:coins) = let n = zipWith (+) (ways coins) (take coin (repeat 0) ++ n) in n
 
answer = ways [200,100,50,20,10,5,2,1] !! 200

