class Math:
    def __init__(self, number= 0):
        self.number = number

    def pow(self, base, exponent):
        result = 1
        for c in range(exponent):
            result *= base
        return result

    def root(self, num,div ):
        result = num ** (1/div)
        return result

    def eq_quadratic(self, a, b, c):

        delta = b**2 - 4 * a * c
        x1 = -b + delta ** 1 / 2 / 2 * a
        x2 = -b - delta ** 1 / 2 / 2 * a
        response = f"As raízes são: x1 = {x1} ^ x2 = {x2}"
        return response

    def eq_linear(self, a, b):
       try:
         x = -b / a
         return x

       except ZeroDivisionError as e:
           print(f"Division by Zero\nCan not be {a}")

