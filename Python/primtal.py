primtal = []
def prim(n):
    for maybePrime in range(2, int(n)):
        isPrime = True
        for x in range(2, maybePrime):
            if maybePrime%x==0:
                isPrime = False
        if isPrime:
            primtal.append(maybePrime)
    return primtal


while True:
    user = input("""--------Primtals Generator---------
    Hvad er det højeste primtal du vil se?: """)
    print(prim(user))
