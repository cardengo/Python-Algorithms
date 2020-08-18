class Fibonacci:
    """
    Finds n's element of Fibonacci sequence
    """

    def __fib(self, n):
        if n < 2:
            return n
        return self.__fib(n - 1) + self.__fib(n - 2)

    def find(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        n += 1
        a = n // 2
        b = n - a
        if n < 25:
            return self.__fib(a) * self.__fib(b) + self.__fib(a - 1) * self.__fib(b - 1)
        return self.find(a) * self.find(b) + self.find(a - 1) * self.find(b - 1)
