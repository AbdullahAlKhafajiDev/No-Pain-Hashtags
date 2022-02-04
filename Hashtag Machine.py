tries = 1
bur = "brrrrrr"
spacer = " "
sentence = ""
def brprinter():
    for i in range (7):       
        print(bur)
        print(spacer)
while (tries == 1):
    texts = input(str("Hashtag go brrr? "))
    Splitter = texts.split()
    print(spacer)
    for word in Splitter:
        sentence = sentence + "#" + word + " "
    brprinter()
    print(sentence)
    print(spacer)
    q1 = input("Done? ")
    if (q1 == "no" or q1 == "No" or q1 == "NO" or q1 == "N" or q1 == "n"):
        sentence = ""
    else:
        tries = 0

    
