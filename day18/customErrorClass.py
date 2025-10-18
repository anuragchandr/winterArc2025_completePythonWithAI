class MyValueError(ValueError):
    def __init__(self, message="Input must be an integer or 'quit'.", code=None):
        super().__init__(message)
        self.code = code

def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

while True:
    user_input = input("Enter an integer (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Exiting gracefully.")
        break

    try:
        x = float(user_input)
        if x % 1 != 0:
            raise MyValueError("Decimal numbers are not allowed.", code=1001)
        number = int(x)
        print(isPrime(number))
    except ValueError:
        raise MyValueError("Invalid input. Please enter an integer or 'quit'.", code=1002)
