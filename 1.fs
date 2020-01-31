(* If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. *)

(*
let p1 = 
    let target = 999

    let sumDivisibleBy n = 
        let p = target / n
        n * p * (p + 1) / 2

    sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
*)

let p1 = 
    [1..999] |> List.filter (fun x -> x % 3 = 0 || x % 5 = 0) |> List.sum
