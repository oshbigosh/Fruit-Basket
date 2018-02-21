fruit_basket = ['Apple','Lemon','Orange','Banana','Cherry']

user_guess = raw_input('Guess a fruit from the fruit basket: ')

if user_guess in fruit_basket:
    print 'Congrats! You guessed correctly!'
else:
    print 'Sorry try again'


