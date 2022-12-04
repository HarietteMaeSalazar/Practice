def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 4:
        print("The Correct answer is ",answer )
    
score = 0
print("Mathematics Quiz")
guess1 = input("45+45= ?\nType your Ans. = ")
check_guess(guess1, "90")

guess2 = input("\n124 * 2 = ?\nType your Ans. = ")
check_guess(guess2, "248")

guess3 = input("\n170/2= ?\nType your Ans. = ")
check_guess(guess3, "85")

guess4 = input("\n750 - 250= ?\n Type your Ans. = ")
check_guess(guess4, "500")
