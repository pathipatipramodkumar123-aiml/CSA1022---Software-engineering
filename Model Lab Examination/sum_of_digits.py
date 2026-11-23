def sum_of_digits(n: int) -> int:
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print("Sum of digits =", sum_of_digits(number))
