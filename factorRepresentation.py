#given a number N , find the number of ways of showing the N as a sum of 1,3,4
#test cases N=4
# answer=4  [4],[1,3],[3,1],[1,1,1,1]

#test case N=5
#answer=6 [1,1,1,1,1],[1,1,3],[1,3,1],[3,1,1],[1,4],[4,1]

#this is divide and conquer type of problem
# f(N) = f(N-1) + f(N-3) + f(N-4) 

def factor(n):
    if n < 0:
        return 0
    if n in [0,1,2]:
        return 1
    answer = factor(n-1) + factor(n-3) + factor(n-4)
    return answer

print(factor(5))
