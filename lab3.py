n = 6
series = 'sum'
a,b = 1,1

def fibonacci(n):
    a,b = 1,1
    for i in range (n-1):
        a,b = b, a+b
    return a

def sum(n):
    i = 0
    answer = 0
    for i in range(n+1):
        answer += i
    return answer

if series == 'fibonacci':
    print fibonacci(n)            
elif series == 'sum':
    print sum(n)
else:
    print 'Invalid String'
