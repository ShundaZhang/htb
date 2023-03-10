import Data.Char (ord)
import Data.Bits (xor)

-- Complete the incantation...
flag = "HTB{XXX}"

extractFlag :: String -> String
extractFlag (s:rest)
  | s == 'H' ||  s == 'T' ||  s == 'B'
  = extractFlag rest
  | s == '{' && last rest == '}'
  = init rest
  | otherwise = error ("Invalid format")

chunks :: Int -> [a] -> [[a]]
chunks n l
  | n == 0 = []
  | n == 1 = [[x] | x <- l]
  | length l <= n = [l]
  | otherwise = [take n l] ++ (chunks n (drop n l))

takeLast :: Int -> [a] -> [a]
takeLast n = reverse . take n . reverse

a = [-43, 61, 58, 5, -4, -11, 64, -40, -43, 61, 62, -51, 46, 15, -49, -44, 47, 4, 6, -7, 47, 7, -59, 52, 17, 11, -56, 61, -74, 52, 63, -21, 53, -17, 66, -10, -58, 0]
b = [6, 106, 10, 0, 119, 52, 51, 101, 0, 0, 15, 48, 116, 22, 10, 58, 93, 59, 106, 43, 30, 47, 93, 62, 97, 63]
c = [304, 357, 303, 320, 304, 307, 349, 305, 257, 337, 340, 309, 396, 333, 320, 380, 362, 368, 286]
d = [52, 52, 95, 95, 110, 49, 51, 51, 95, 110, 110, 53, 116, 51, 98, 63]

checkFlag :: String -> Bool
checkFlag flag =
  length content == 76 &&
  all (==True) (map (\ (l,r) -> l == r) (zip one a)) &&
  all (==True) (map (\ (l,r) -> l == r) (zip two b)) &&
  all (==True) (map (\ (l,r) -> l == r) (zip three c)) &&
  all (==True) (map (\ (l,r) -> l == r) (zip four d))
  where content = map ord (extractFlag flag)
        one     = map (\ [l, r] -> (l - r)) (chunks 2 content)
        two     = map (foldr xor 0) (chunks 3 content)
        three     = map (foldr (+) 0) (chunks 4 content)
        four     = map head (chunks 5 content)

main = putStrLn (if (checkFlag flag)
    then "The spell went off without a hitch!"
    else "You disappear in a puff of smoke!"
  )
