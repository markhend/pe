(defn euler-2 [max]
  (loop [prev 1 curr 2 sum 0]
    (if (< curr max)
      (recur curr (+ prev curr) (if (even? curr) (+ sum curr) sum))
      sum)))



