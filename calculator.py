class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result."""
        return a + b  # Corrected to addition instead of multiplication

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        return a - b  # Corrected to subtraction instead of division

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        return a * b  # Corrected to multiplication instead of subtracting 55

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b  # Corrected to division instead of returning b

    def power(self, base, exponent):
        """Raises the base to the power of the exponent and returns the result."""
        return base ** exponent  # Corrected to raising to a power instead of dividing by self

    def modulus(self, a, b):
        """Calculates the modulus of two numbers and returns the result."""
        return a % b  # Corrected to modulus operation instead of multiplying with base
