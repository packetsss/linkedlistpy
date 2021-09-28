def sqrt(x: float, threshold: float = 0.000001) -> float:
    last_guess = x / 2.0

    while True:
        guess = (last_guess + x / last_guess) / 2
        if abs(guess - last_guess) < threshold:  # example threshold
            return guess
        last_guess = guess


def remainder(x: float, divisor: float) -> float:
    return x - divisor * (x // divisor)


def root(x: float, root: float) -> float:
    return x ** (1 / root)


