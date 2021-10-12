import time
def dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start, 'seconds')
    return wrapper

@dec
def main():
    n = int(input())
    a, b = 1, 1

    for i in range(n):
        print(a)
        a, b = b, a + b
main()
