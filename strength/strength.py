import random

element=["hello", "python", "happy", "world"]
word=random.choice(element)
chances=6
letter=[]
win=False

while True:
    for l in word:
        if l.lower() in letter:
            print("",l, end=" ")
        else:
            print("_", end=" ")
    print("")
    print("you have",chances, "chances")
    tentativa=input("type a letter: ")
    letter.append(tentativa.lower())
    if tentativa.lower() not in word.lower():
        chances -= 1

    if chances == 0:
        print("You Lost!\n The word is:", word)
        break

    win = True
    for l in word:
        if l.lower() not in letter:
            win=False
            break

    if chances == 1:
        print("CAREFULLLLL!!!\nYOU ONLY HAVE ONE CHANCE\n")

    if win:
        print("Congratulations, you win!!!\nThe word is: ", word)
        break