def provide_hint(user_guess , randnumber):
    if randnumber > user_guess :
            print('your guess is lower than random number')
    elif randnum < user_guess:
                print('your guess is higher than random number')
    else:
            print(f'{"\033[34m"}Congratulation! you Guess the Number{"\033[0m"}')
            print(f'your score is {score}')
            wanna_play = input('do you want to play again?[y/n]')
            if wanna_play.lower() == 'n':
                  return False
            else:
                   randnum = random.randint(1 , 100)
                   score = 100
                   return True
    return True