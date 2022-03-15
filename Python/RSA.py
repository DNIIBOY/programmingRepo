b'04 04 1c>\t 10}\t% 1a i 1a 03 .k 01 4'

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

    p = 160390912114499758109275030312460194685863931436864531742691
    q = 460374952936305732755303497312183367004304494680683253666831
    ct = 20110717990345687898226853609420384981656622084193266947150834445506719164043911436839039345613213247227489425483411000
    e = 3

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
    out = convert_to_text(pt)
    print("Output:  " + str(out)) 



if __name__ == "__main__":
    main()
