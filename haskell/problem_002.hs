module Main
  where

main=print (evenFibSum 4000000)

fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

evenFibSum :: Int -> Int
evenFibSum limit = sum (filter even (takeWhile (<= limit) fibs))
