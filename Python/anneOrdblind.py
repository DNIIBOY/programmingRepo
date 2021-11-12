import discord

client = discord.Client()


def run(annein: str, correct: str) -> str:
    wrongcount = 0
    annewords = annein.split()
    correctwords = correct.split()
    for word in range(len(annewords)):
        try:
            for let in range(len(annewords)):
                if annewords[word][let] != correctwords[word][let]:
                    wrongcount += 1
        except IndexError:
            pass


    return f"Anne tager {round((wrongcount/len(annein.replace(' ', '')))*100, 1)}% fejl"


def main():
    client.run("mfa._ggoVAkvKg1Z50z62hc8zTbqYyFTUhTdE_RgRWb0xRWQynGQpiR9wtM2TRmpjRFLXaeRWTCSW_UD46piG5R3", bot=False)
    annein = input("Indtast Anne's indtastning: ")
    correct = input("Indtast korrekt indtastning: ")
    print(run(annein, correct))


@client.event
async def on_message(message):
    print(message)
    if message.guild.name == "Burker's Diktatoriske Monarki":
        print("on burker")


if __name__ == '__main__':
    main()
