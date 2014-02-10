from fractions import gcd
from math import pow

# which and how many elements are in group Z_p * ?
#
# Usage:
#
# print z_star_group(13)
# print "size:" + str(len(z_star_group(13)))
def z_star_group(N):
    group = []
    for i in range(1,N):
        if(gcd(i, N) == 1):
            group.append(i)
    return group


# http://en.wikipedia.org/wiki/Discrete_logarithm
#
# Usage:
#
# computes dlog2(5) in Z_13
# print dlog(5, 2, 13)
def dlog(val, base, prime):
    for i in range(0, prime - 2):
        res = (pow(base, i)) % prime
        if(res == val):
            return i

# def: x^e = c in Z_p is called e'th rooth of c
def eth_root(e, c, p):
    for i in range(0, p):
        if((pow(i, e) % p) == c):
            return i

# extended Euclidean algorithm
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
