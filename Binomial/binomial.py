class BinomialCoefficient:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def factorial(self, num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def calculate_binomial_coefficient(self):
        if self.r < 0 or self.r> self.n:
            return 0
        return self.factorial(self.n) // (self.factorial(self.r) * self.factorial(self.n - self.r))

# Example usage
n_value = int(input("Enter the value of coefficient which comes success probability: "))
print("\n")
r_value = int(input("Enter the coefficient for term which you want to perform :"))

# Create an instance of the BinomialCoefficientCalculator class
obj = BinomialCoefficient(n_value, r_value)

# Calculate and print the binomial coefficient
result = obj.calculate_binomial_coefficient()
print('\n')
print(f"The binomial coefficient of C({n_value}, {r_value}) is: {result}")


