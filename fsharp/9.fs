let p8 = 
    [ for a in [ 1..1000 / 3 ] do
          for b in [ (a + 1)..(1000 - a) / 2 ] do
              let c = 1000 - (a + b)
              if (a * a + b * b = c * c) then yield (a, b, c, a * b * c) ]
