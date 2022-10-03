



def fibonacci_tail(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_tail(n - 1) + fibonacci_tail(n - 2)

def fibonacci_sum(n, sum):
    if n == 0:
        return 0

    if n == 1:
        return 1


def factorial_sum(n, sum):
    if n == 0:
        return 1

    sum = n * factorial(n-1, sum)

    print("sum", sum)

    return sum

def factorial(n):
    if n == 0:
        return 1

    sum = n * factorial(n-1)
    print("sum", sum)
    return sum


if __name__ == '__main__':

   result = fibonacci_tail(10)

   print(result)

   result2 = factorial(5)

   print(result2)
