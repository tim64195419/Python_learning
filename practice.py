def fib(num):
    """生成器"""
    a, b = 0, 1
    while True:
        a, b = b, a + b

        yield a
        print(a)

fi = fib(12)
fi.send(None)
for x in range(12):
        fi.__next__()
