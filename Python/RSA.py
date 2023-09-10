def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y


def convert_to_text(pt: int) -> str:
    hex_code = hex(pt)[2:]
    bytes_object = bytes.fromhex(hex_code)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string


def main():

    p = 23
    q = 29
    e = 3
    ct = 137

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    # Decrypt ciphertext
    pt = pow(ct, d, n)


    print("n:  " + str(n))
    print("d:  " + str(d))

    print("pt:  " + str(pt))

    # Convert the number to a string of text
    try:
        out = convert_to_text(pt)
    except:
        out = "Could not convert to ASCII"
    print("Output:  " + str(out)) 



if __name__ == "__main__":
    main()
