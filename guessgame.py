import random
x = int(input("An evil demon asks you to guess the number he is thinking of between 1 and 10, inclusive of course. He threatens to eat your soul if you cannot get it correctly in 3 attempts.:"))

y = int(random.randint(1,10))

if  x==y:
    print("The demon is surprised by your correct guess. He admits the number was indeed", y, ". He slinks away in shame leaving behind a mysterious pouch. You take the pouch.")
else:
    print("\"Nay! Guess again! Thou have 2 more tries!\" laughs the demon.")
    a = int(input("What could it be? :"))
    if a==y:
        print("\"Hurmph\" the demon lets out a sigh of disappointment. ", y, " was the number. The demon disappears with a poof of red smoke. Leaving behind a rusty dagger. You take the dagger.")
    else:
        print("\"Ha! Guess again, mortal! You have 1 more try!\" screams the demon.")
        b = int(input("This is your last chance! Correctly, guess the number between 1 and 10, including 1 and 10. :"))
        if b==y:
            print(" \"Kekeke\" crackles the demon. He disappears without any sign of hesitation. The correct number was", y, ". As you prepare to leave the scene in haste, you realise the demon has left behind a strange looking bottle. The bottle gets inside your bag on its own.")
        else:
            print("The demon, without a second of hesitation or remorse, stretches his mouth, revealing terrible and putrid sharp teeth. As your soul is grinded by his unholy jaw, the demon laughs. Savouring every second of it.", y, "was the correct number. YOU DIED. ")

input("Press Enter to quit")