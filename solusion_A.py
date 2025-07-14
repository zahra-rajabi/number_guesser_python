import random 

def validate_input(guess):
        if not guess.isdigit():
            print('enter a valid input')
            return False
        
        guess = int(guess)
        if guess > 100 or guess < 1:
            print('your number is out of the range. enter a number between 1 and 100')
            return False
        
        return True


def main():
    randnum = random.randint(1 , 100)
    score = 100


    #! -----------------------------------------------------------

    while True:
        user_guess = input(f'{"\033[32m"}enter a number between 1 and 100 [enter q to quit the game]{"\033[0m"}')
        
        if user_guess.lower() == 'q':
            print('Thank you for playing, good bye')
            break
        if not validate_input(user_guess):
            continue
        user_guess = int(user_guess)
        if randnum > user_guess :
            print('your guess is lower than random number')

        elif randnum < user_guess:
                print('your guess is higher than random number')
        else:
                print(f'{"\033[34m"}Congratulation! you Guess the Number{"\033[0m"}')
                print(f'your score is {score}')
                wanna_play = input('do you want to play again?[y/n]')
                if wanna_play.lower() == 'n':
                  break
                else:
                     randnum = random.randint(1 , 100)
                     score = 100
                     continue

        score -= 10
        score = max(score , 0)
        print('your score is ' , score)
        if score == 0 :
            print(f'{"\033[31m"}you lost and your score is 0{"\033[0m"}')
            break
    
if __name__ == '__main__':
    main()
