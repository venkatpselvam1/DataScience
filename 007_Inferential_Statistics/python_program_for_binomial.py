x=float(input())#number of applicants
m=int(input())#probability of accepting an application
n=int(input())#find the probability that at most n applications are accepted
def nCr(n, r):
    return (fact(n) / (fact(r)
                * fact(n - r)))
# Returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res
ans = 0.0
for i in range(n+1):
    nc = nCr(m,i)
    ans+= nc * (x ** (i)) * ((1-x) ** (m-i))
print(round(ans,4))
