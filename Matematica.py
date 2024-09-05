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

        # Verificar se a é igual a zero
        if a == 0:
            print("a can not be zero")

        # Caso a for diferente de 0  calcula delta
        elif a != 0:
            delta = b**2 - 4 * a * c

            # Se delta for menor que zero não tem solução
            if delta < 0:
                print("This equation doesnt have solution")

            # Senão tem solução
            else:
                x1 = (-b + (delta ** 0.5)) / (2 * a)
                x2 = (-b - (delta ** 0.5)) / (2 * a)
                response = f" As raízes são: x1 = {x1} ^ x2 = {x2}"
                return response

    def eq_linear(self, a, b):
       try:
         x = -b / a
         return x

       except ZeroDivisionError as e:
           print(f"Division by Zero\nCan not be {a}")

    def sen(self, ang):
        pass

    def cos(self, ang):
        pass






