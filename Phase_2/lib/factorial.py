def factorial (n):
    product = 1
    while n > 0:
        n -= 1

    product *= n
    return product


print(f"""Running: factorial(5)
    Expected: 120
Actual: {factorial (5)}""")