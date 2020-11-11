def fibonacci(n):
    answer=0
    if n == 0:
        answer=0
    if n == 1:
        answer=1
    if n > 1:
        answer=fibonacci(n-1)+fibonacci(n-2)
    return answer