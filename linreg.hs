sums :: (Floating a) => [(a, a)] -> (a, a, a, a)

sums = sum4 . (map summands)
    where summands (x, y) = (x, x**2, y, x*y)

sum4 :: (Num a) => [(a, a, a, a)] -> (a, a, a, a)

sum4 = foldr plus4 (0, 0, 0, 0)
    where plus4 (a1, a2, a3, a4) (b1, b2, b3, b4) = (a1+b1, a2+b2, a3+b3, a4+b4)

bestfit points = ((sy * sx - n * sxy) / scale, (sx * sxy - sy * sx2) / scale)
    where (sx, sx2, sy, sxy) = sums points
          n = length points
          scale = sx ** 2 - n * sx2