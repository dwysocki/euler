module Main
  where

main=print (multiples [3, 5] [1,2..1000-1])

divisor :: Int -> (Int -> Bool)
divisor d = \x -> (x `mod` d) == 0

multiples :: [Int] -> [Int] -> Int
multiples divisors range = sum (filter (\x -> any id (sequence isMultiple x))
                                       range)
  where isMultiple = map divisor divisors
