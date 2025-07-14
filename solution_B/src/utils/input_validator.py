def validate_input( start , end):
    while True:
        try:
          user_input = input('Enter A number:[q to quit]')
          if user_input.lower() == 'q':
            print('Thank you for playing, good bye')
            break
          user_input = int(user_input)
          if start <= user_input <= end:
             return user_input
          else:
             print(f'you must enter a number between {start} and {end}')
        except ValueError:
          print('Enter a number')
          continue

