from src.utils.input_validator import validate_input
from src.game_logic.number_generator import generate_number


def main():
    randnum = generate_number(1 , 100)
    score = 100

    while True:
        user_guess = validate_input(1 , 100)
        if randnum > user_guess :
            print('your guess is lower than random number')

        elif randnum < int(user_guess):
                print('your guess is higher than random number')
        else:
                print(f'{"\033[34m"}Congratulation! you Guess the Number{"\033[0m"}')
                print(f'your score is {score}')
                wanna_play = input('do you want to play again?[y/n]')
                if wanna_play.lower() == 'n':
                  break
                else:
                     randnum = generate_number(1 , 100)
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
