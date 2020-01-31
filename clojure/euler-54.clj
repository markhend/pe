(with-open [rdr (clojure.java.io/reader "c:/Dropbox/Code/Euler/54input.txt")]
  (doseq [line (line-seq rdr)] (println rdr)))

