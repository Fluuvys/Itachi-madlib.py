title = 'Itachi Village and food madlib by \"Mei\" coded by me.'
secondline = 'hope you enjoy this madlib. good luck and have fun.'
endingline = 'Thank you for playing my game and I hope you have a wondeful day. '
print(title.upper())
print(secondline.upper())
sixwords = input("Enter in 6 letters: ")
while True:
    if len(sixwords) <= 6:
        foodyouate = input('Enter in the food you ate the latest: ')
        yourname = input('Enter in your name: ')
        print('In the Village of the ' + sixwords + ', Itachi loves ' + foodyouate + ' but hates ' + yourname + '.')
        print(endingline[5])
        print(endingline.upper())
        break
    else:
        print("You must put in 6 letters or less")
        sixwords = input("enter in 6 letters: ")
pass



