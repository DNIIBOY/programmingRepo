def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 111351602227707581067416344643048751626960926253551879945433066776126511936461
    q = 67722700071961988029846370299408511833514117774646239226239805715004968536019
    e = 65537
    ct = 7416559017732380714510020985419780493726289824818461938628854022948902779175432427219526599003916978168995567524860519149904946110153128594403636858898495

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    print( "n:  " + str(d) );

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print( "pt: " + str(pt) )

if __name__ == "__main__":
    main()
