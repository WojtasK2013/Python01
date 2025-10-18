def f(n):
    if n == 0: return 0
    return f(n // 10) + n % 10
def g(n):
    if n == 0: return 0
    return g(n - 1) + f(n)
+w=g(200)

print(w)