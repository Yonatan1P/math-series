def fibonacci(n):
    answer=0
    if n == 0:
        answer=0
    if n == 1:
        answer=1
    if n > 1:
        answer=fibonacci(n-1)+fibonacci(n-2)
    return answer

def lucas(n):
    answer=0
    if n == 0:
        answer = 2
    if n == 1:
        answer =3
    if n > 1:
        answer=lucas(n-1)+lucas(n-2)
    return answer

def sum_series(n,first=0,second=1):
    answer=0
    if n == 0:
        answer = first
    if n == 1:
        answer = first + second
    if n > 1:
        answer=sum_series(n-1,first,second)+sum_series(n-2,first,second)
    return answer