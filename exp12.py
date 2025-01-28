x=int(input("enter the wikipedia Mb consupmtion"))
y=int(input("enter the meme Mb consupmtion"))
totalWikipedia=x*0.10
totalMeme=y*0.05
totalconsupmtion=totalWikipedia+totalMeme
if totalconsupmtion>100:
    print("Too much consumption")
elif totalMeme>totalWikipedia:
    print("WOW MANY MEMES\n SUCH LOL")
    