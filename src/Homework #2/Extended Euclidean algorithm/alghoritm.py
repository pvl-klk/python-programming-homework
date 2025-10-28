def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    x_previous, x = 1, 0
    y_previous, y = 0, 1

    while b != 0:
        q = a // b
        r = a % b

        x_previous, x = x, x_previous - q * x
        y_previous, y = y, y_previous - q * y

        a, b = b, r

    return a, x_previous, y_previous


d, x, y = extended_gcd(54, 30)

print(f"GCD(54, 30) = {d}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Factorization: 54*({x}) + 30*({y}) = {54 * x + 30 * y}")
