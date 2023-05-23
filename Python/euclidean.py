def extended_gcd(a, b) -> tuple:
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def display(items: dict) -> None:
    for key, val in items.items():
        print(f"{key} = {val}")


def diofantic(a: int, b: int, c: int) -> None:
    gcd, s, t = extended_gcd(a, b)
    if c % gcd != 0:
        print("lmao no way")
        return

    am, bm, cm = a//gcd, b//gcd, c//gcd

    print("Equation:")
    print(f"{a}x + {b}y = c")

    print(f"(x, y) = ({cm*s} - {bm}k, {cm*t} + {am}k)")


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = input("c: ")

    gcd, s, t = extended_gcd(a, b)
    result = {"D": gcd, "s": s, "t": t}
    display(result)

    if c == "":
        return

    diofantic(a, b, int(c))


if __name__ == "__main__":
    main()
