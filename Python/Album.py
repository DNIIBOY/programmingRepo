albumDict = {}
def lav_album():
    album = []
    band = input("Nævn et band: ")
    while True:
        sang = input("Tilføj en sang til Albummet: ")
        if sang == "q":
            albumDict[band] = album
            return albumDict
            break
        else:
            album.append(sang)

while True:
    user = input("(T)ilføj, (V)is eller (q)uit: ")
    if user.lower() == "t":
        albummet = lav_album()
        print(albummet)
    elif user.lower() == "v":
        if albumDict == {}:
            print("Listen er tom")
        else:
            print(albumDict)
    elif user.lower() == "q":
        print("Prøver at skrive til fil")
        try:
            fil = open("albums.txt", "w")
            fil.write(str(albummet))
            fil.close()
            print("Succes!")
            break
        except:
            print("Kunne ikke skrive til fil")
            raise
    else:
        print("Ugyldigt bogstav")