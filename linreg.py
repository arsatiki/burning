from __future__ import division

# TOOD add doctests

def summands(point):
    x, y = point
    return (x, x**2, y, x*y)

def sums(points):
    summandseq = map(summands, points)
    return map(sum, zip(*summandseq))

def bestfit(points):
    n = len(points)
    Sx, Sx2, Sy, Sxy = sums(points)

    divisor = Sx**2 - n * Sx2
    
    k = (Sy * Sx - n * Sxy) / divisor
    b = (Sx * Sxy - Sy * Sx2) / divisor
    
    return k, b