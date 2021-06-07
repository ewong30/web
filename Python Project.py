import random
import matplotlib.pyplot as plt

#Round 0: The setup
roundd = 0
#Roundd will keep track of our stages, which will be how we're going to navigate what we're doing at each turn

wins = 0
losses = 0
ties = 0

rocks = 0
rockwins = 0
rocklosses = 0
rockties = 0

papers = 0
paperwins = 0
paperlosses = 0
paperties = 0

scissors = 0
scissorwins = 0
scissorlosses = 0
scissorties = 0
#The counters for data later on

last = None
#How we'll be using the markov dictionary later on

last_result = None

if roundd == 0:
    print('Welcome to (a slightly smarter) game of Rock Paper Scissors!')
    name = input("To get started, what's your name?\n ")
    starting = input('Hello ' + name + '! Would you like to begin? y/n\n ')
    if starting == 'y':
        roundd += 1
    if starting != 'y':
        roundd = 6
    
#Round 1: The first move
#the rules/formal intro:
if roundd == 1:
    print("\nAlright! The rules of the game is simple:\nJust like every other game of rock paper scissors,\neyou will choose to play rock paper scissors against me,\nin a string that you will input. after every round,\nyou will be able to choose to play again, end, or graph the statistics of the game!\n\nWith the rules of the game out of the way, let's play!")

    #Round counter:
    counter = 1
    print("\n======Round " + str(counter) + "======")

    #The First Round:
    
    #Player's choice:
    choice0 = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')

    #Computer's choice:
    #The following probabilities will be generated based on a random choice from this list,
    #with a total of 101 terms to represent the probabilities (37.7, 34.5, 27.8)
    #each of them are rounded to the nearest whole number
    round1choices = []
    for i in range(38):
        round1choices.append('paper')
    for i in range(35):
        round1choices.append('scissors')
    for i in range(28):
        round1choices.append('rock')
    
    mychoice0 = random.choice(round1choices)
    
    #Rule conditions
    viable_rock = ['rock', 'Rock', 'r', 'R']
    viable_paper = ['paper', 'Paper', 'p', 'P']
    viable_scissors = ['scissors', 'Scissors', 's', 'S']
    if choice0 in viable_rock:
        if mychoice0 == 'scissors':
            wins += 1
            rocks += 1
            rockwins += 1
            counter += 1
            last_result = 'win'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'rock':
            ties += 1
            rocks += 1
            rockties += 1
            counter += 1
            last_result = 'tie'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'paper':
            losses += 1
            rocks += 1
            rocklosses += 1
            counter += 1
            last_result = 'loss'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice0 in viable_paper:
        if mychoice0 == 'rock':
            wins += 1
            papers += 1
            paperwins += 1
            counter += 1
            last_result = 'win'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'paper':
            ties += 1
            papers += 1
            paperties += 1
            counter += 1
            last_result = 'tie'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'scissors':
            losses += 1
            papers += 1
            paperlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice0 in viable_scissors:
        if mychoice0 == 'paper':
            wins += 1
            scissors += 1
            scissorwins += 1
            counter += 1
            last_result = 'win'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'scissors':
            ties += 1
            scissors += 1
            scissorties += 1
            counter += 1
            last_result = 'tie'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'rock':
            losses += 1
            scissors += 1
            scissorlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    
    
#Round 2: Play again?
if roundd == 2:
    again = input('\nWould you like to start the second round? y/n\n ' )
    
    if again == 'y':
        roundd += 1
    if again == 'n':
        roundd = 6
    if ((again != 'y') and (again != 'n')):
        print("\nUhhh this is awkward, I don't think you did that right.")
        exit()
    
    
    
#Building a markov dictionary:
#The two items that we will be using will be if the last game was a win/loss and the last played thing
#I'm going to semi-manually put in these values... because... there's no way to justify the amount of time this took.
#In the beginning, it will start out with the statistics and ideas set by the website:
#How To Win At Rock Paper Scissors (Using Data From 120,000 Games), linked in the project proposal
d = {}

#FOR TIES:
#Rock Ties:
d['rock tie'] = ['scissors']
for i in range(27):
    d['rock tie'] += ['scissors']
for i in range(35):
    d['rock tie'] += ['paper']
for i in range(37):
    d['rock tie'] += ['rock']
#Paper Ties:
d['paper tie'] = ['rock']
for i in range(29):
    d['paper tie'] += ['paper']
for i in range(36):
    d['paper tie'] += ['scissors']
for i in range(34):
    d['paper tie'] += ['rock']
#Scissor Ties:
d['scissors tie'] = ['scissors']
for i in range(27):
    d['scissors tie'] += ['scissors']
for i in range(37):
    d['scissors tie'] += ['paper']
for i in range(35):
    d['scissors tie'] += ['rock']
    
#FOR WINS:
#Rock wins:
d['rock win'] = ['paper']
for i in range(29):
    d['rock win'] += ['paper']
for i in range(37):
    d['rock win'] += ['scissors']
for i in range(33):
    d['rock win'] += ['rock']
#Paper wins:
d['paper win'] = ['paper']
for i in range(36):
    d['paper win'] += ['paper']
for i in range(29):
    d['paper win'] += ['scissors']
for i in range(34):
    d['paper win'] += ['rock']
#Scissors wins:
d['scissors win'] = ['paper']
for i in range(37):
    d['scissors win'] += ['paper']
for i in range(36):
    d['scissors win'] += ['scissors']
for i in range(26):
    d['scissors win'] += ['rock']

#FOR LOSSES:
#Rock losses:
d['rock loss'] = ['paper']
for i in range(36):
    d['rock loss'] += ['paper']
for i in range(32):
    d['rock loss'] += ['scissors']
for i in range(31):
    d['rock loss'] += ['rock']
#Paper losses:
d['paper loss'] = ['paper']
for i in range(32):
    d['paper loss'] += ['paper']
for i in range(33):
    d['paper loss'] += ['scissors']
for i in range(28):
    d['paper loss'] += ['rock']
#Scissor losses:
d['scissors loss'] = ['paper']
for i in range(33):
    d['scissors loss'] += ['paper']
for i in range(35):
    d['scissors loss'] += ['scissors']
for i in range(31):
    d['scissors loss'] += ['rock']

lastlast = last
lastlastresult = last_result
#lastlast will be for keeping track of things later on.

#Round 3: Things get smarter
if roundd == 3:
    counter = 2
    print("\n======Round" + str(counter) + "======")
    #Making a marker to pull from our Markov Dictionary
    key = last + ' ' + last_result
    lastlast = last
    lastlastresult = last_result
    
    #Copying and pasting round 1, but adding in the markov dictionary
    choice1 = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')
    
    #Using the Markov Dictionary to make the computer's choice:
    mychoice1 = random.choice(d[key])
    
    #Adding (copy and pasting) in the rules:
    viable_rock = ['rock', 'Rock', 'r', 'R']
    viable_paper = ['paper', 'Paper', 'p', 'P']
    viable_scissors = ['scissors', 'Scissors', 's', 'S']
    if choice1 in viable_rock:
        if mychoice1 == 'scissors':
            wins += 1
            rocks += 1
            rockwins += 1
            counter += 1
            last_result = 'win'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'rock':
            ties += 1
            rocks += 1
            rockties += 1
            counter += 1
            last_result = 'tie'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'paper':
            losses += 1
            rocks += 1
            rocklosses += 1
            counter += 1
            last_result = 'loss'
            last = 'rock'
            roundd += 1
            print('You chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice1 in viable_paper:
        if mychoice1 == 'rock':
            wins += 1
            papers += 1
            paperwins += 1
            counter += 1
            last_result = 'win'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'paper':
            ties += 1
            papers += 1
            paperties += 1
            counter += 1
            last_result = 'tie'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'scissors':
            losses += 1
            papers += 1
            paperlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'paper'
            roundd += 1
            print('You chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice1 in viable_scissors:
        if mychoice1 == 'paper':
            wins += 1
            scissors += 1
            scissorwins += 1
            counter += 1
            last_result = 'win'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'scissors':
            ties += 1
            scissors += 1
            scissorties += 1
            counter += 1
            last_result = 'tie'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'rock':
            losses += 1
            scissors += 1
            scissorlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'scissors'
            roundd += 1
            print('You chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))

#Round 4: The loop
#Since there's not much else to do, round 4 will just be a loop that goes as long as the player wants.

counter = 3

while roundd == 4:
    
    #Play Again? Graph? Stop?
    future = input('\nWould you like to start the next round? y(play again)/ n(stop the game)/ g(graph)\n ')
    
    stopp = ['no', 'No', 'n', 'N', 'stop the game', 'Stop the game']
    if future in stopp:
        roundd = 6
    
    graphh = ['graph', 'Graph', 'g', 'G']
    if future in graphh:
        roundd += 1
    
    
    againn = ['yes','Yes', 'y', 'Y', 'play again', 'Play again']
    
    if ((future not in stopp) and (future not in graphh)) and (future not in againn):
        print("\nUhhh I think you did something wrong there.")
        exit()
    
    if future in againn:
        print("\n======Round " + str(counter) + "======")
        
        #Making a marker to pull from our Markov Dictionary
        updatingkey = lastlast + ' ' + lastlastresult
        key = last + ' ' + last_result
        
        #WHAT'S NEW: here, we'll be adding in a "learning" aspect to this game.
        
        if last == 'rock':
            for i in range(5):
                d[updatingkey] += ['paper']
        if last == 'paper':
            for i in range(5):
                d[updatingkey] += ['scissors']
        if last == 'scissors':
            for i in range(5):
                d[updatingkey] += ['rock']
        
        #Copying and pasting round 1, but adding in the markov dictionary
        choice = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')
        
        #Using the Markov Dictionary to make the computer's choice:
        mychoice = random.choice(d[key])
        
        lastlast = last
        lastlastresult = last_result
        
        #Copying in the rules:
        viable_rock = ['rock', 'Rock', 'r', 'R']
        viable_paper = ['paper', 'Paper', 'p', 'P']
        viable_scissors = ['scissors', 'Scissors', 's', 'S']
        if choice in viable_rock:
            if mychoice == 'scissors':
                wins += 1
                rocks += 1
                rockwins += 1
                counter += 1
                last_result = 'win'
                last = 'rock'
                print('You chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'rock':
                ties += 1
                rocks += 1
                rockties += 1
                counter += 1
                last_result = 'tie'
                last = 'rock'
                print('You chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'paper':
                losses += 1
                rocks += 1
                rocklosses += 1
                counter += 1
                last_result = 'loss'
                last = 'rock'
                print('You chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if choice in viable_paper:
            if mychoice == 'rock':
                wins += 1
                papers += 1
                paperwins += 1
                counter += 1
                last_result = 'win'
                last = 'paper'
                print('You chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'paper':
                ties += 1
                papers += 1
                paperties += 1
                counter += 1
                last_result = 'tie'
                last = 'paper'
                print('You chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'scissors':
                losses += 1
                papers += 1
                paperlosses += 1
                counter += 1
                last_result = 'loss'
                last = 'paper'
                print('You chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if choice in viable_scissors:
            if mychoice == 'paper':
                wins += 1
                scissors += 1
                scissorwins += 1
                counter += 1
                last_result = 'win'
                last = 'scissors'
                print('You chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'scissors':
                ties += 1
                scissors += 1
                scissorties += 1
                counter += 1
                last_result = 'tie'
                last = 'scissors'
                print('You chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'rock':
                losses += 1
                scissors += 1
                scissorlosses += 1
                counter += 1
                last_result = 'loss'
                last = 'scissors'
                print('You chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))

#Round 5: The graphing
if roundd == 5:
    
    #Prepping the data sets
    geninfo = ['Rock', 'Paper', 'Scissors']
    gendata = [rocks, papers, scissors]
    
    rockinfo = ['Times won', 'Times lost', 'Times tied']
    rockdata = [rockwins, rocklosses, rockties]
        
    paperinfo = ['Times won', 'Times lost', 'Times tied']
    paperdata = [paperwins, paperlosses, paperties]
    
    scissorsinfo = ['Times won', 'Times lost', 'Times tied']
    scissorsdata = [scissorwins, scissorlosses, scissorties]
    
    winsvlosses = ['Wins', 'Losses', 'Ties']
    winsvlossesdata = [wins, losses, ties]
    
    #Bar Graph Request
    request = input('\nWhat data do you want graphed?\n\n• Typing gen will return the number of times you played rock, paper, or scissors\n• Typing rock, paper, or scissors will show your information on your wins, losses, and ties by choosing the given item\n• Finally, winsvlossesvties gives you a ratio of your wins to losses to ties in a bar graph.\nMultiple inputs allowed as long as they are spaced apart.\n ')
    
    if 'gen' in request:
        plt.title('General Info')
        plt.ylabel('Amount of Times Played')
        plt.xlabel('Type of Item (Rock, Paper, Scissors)')
        plt.bar(geninfo, gendata)
        plt.show()
        roundd = 6
    
    if 'rock' in request:
        plt.title('Rock Info')
        plt.ylabel('Frequency/Amount of Times the Event Occured')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(rockinfo, rockdata)
        plt.show()
        roundd = 6
    
    if 'paper' in request:
        plt.title('Paper Info')
        plt.ylabel('Frequency/Amount of Times the Event Occured')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(paperinfo, paperdata)
        plt.show()
        roundd = 6
    
    if 'scissors' in request:
        plt.title('Scissors Info')
        plt.ylabel('Frequency/Amount of Times the Event Occured')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(scissorsinfo, scissorsdata)
        plt.show()
        roundd = 6
    
    if 'winsvlossesvties' in request:
        plt.title('Wins vs. Losses vs. Ties Data')
        plt.ylabel('Number of Wins/Losses')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(winsvlosses, winsvlossesdata)
        plt.show()
        roundd = 6

#Round 6: the end
if roundd == 6:
    print('Thanks for playing!')
    exit()