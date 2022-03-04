import random
word_list = ["apple","pen","car","drive","fish","laptop","single","angry"]
hiden_word = random.choice(word_list)
string = list(len(hiden_word)*"_")
user_lp = 5
while user_lp > 0 and "_" in string:
    for i in range(len(string)):
        print(string[i],end = "")
    print()
    user_guess = input("What letters you guess? ")
    if user_guess in hiden_word:
        print("Correct!")
        for i in range(len(hiden_word)):
            if hiden_word[i] == user_guess:
                string[i] = hiden_word[i]
    else:
        print("Incorrect!")
        user_lp -=1
        print("Your LP is " + str(user_lp))
if user_lp == 0:
    print("Game over!")
else:
    string = "".join(string)
    print(string)
    print("You win!")       
    
