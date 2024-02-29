def computegrade(score) :
    try:
        fscore = float(score)
    except:
        print("Bad score")
        quit()

    if fscore > 1.0 :
        print("Bad score")
    elif fscore >= 0.9 :
        print("A")
    elif fscore >= 0.8 :
        print("B")
    elif fscore >= 0.7 :
        print("C")
    elif fscore >= 0.6 :
        print("D")
    elif fscore < 0.6 :
        print("F")

userscore = input("Enter score between 0.0 and 1.0: ")
computegrade(userscore)
